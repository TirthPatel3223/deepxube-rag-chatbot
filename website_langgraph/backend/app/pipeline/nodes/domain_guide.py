# ============================================================================
# Node: domain_guide
# ============================================================================
# Multi-turn domain creation guide flow.
#
# This node manages a stateful conversation where the chatbot walks the
# user through creating a new puzzle domain for DeepXube. It loads context
# files progressively to minimize token usage:
#
#   Stage "none" → "overview":
#     Load ADDING_NEW_DOMAIN.md overview → brief summary + "want to start?"
#
#   Stage "overview" → "template":
#     Load full ADDING_NEW_DOMAIN.md → guide through 3 decisions → serve template
#
#   Stage "template" → "examples":
#     Load matching section from EXAMPLES.md → show real-world example
#
#   Stage "examples" → "training":
#     Load TRAINING_GUIDE.md → guide through training decisions
#
#   Stage "training" → "none":
#     Done — clear domain guide state, return to normal routing
# ============================================================================

import logging
from pathlib import Path
from app.models.state import PipelineState
from app.config import settings

logger = logging.getLogger(__name__)


def _load_file(filename: str) -> str:
    """
    Load a context file from the context_files directory.

    Args:
        filename: Name of the file (e.g. "ADDING_NEW_DOMAIN.md").

    Returns:
        The file content as a string.
    """
    path = settings.context_files_abs / filename
    if not path.exists():
        logger.error(f"Context file not found: {path}")
        return f"[ERROR: Context file '{filename}' not found]"
    return path.read_text(encoding="utf-8")


def _extract_overview(full_content: str) -> str:
    """
    Extract just the overview and quick-reference table from
    ADDING_NEW_DOMAIN.md, skipping the full templates.

    This is used for the initial "overview" stage to keep token usage low.
    """
    lines = full_content.split("\n")
    overview_lines = []
    for line in lines:
        overview_lines.append(line)
        # Stop before the first template section
        if line.strip().startswith("## TEMPLATE A:"):
            break
    return "\n".join(overview_lines[:-1])  # Remove the template header line


def _extract_example_section(full_content: str, template_letter: str) -> str:
    """
    Extract the example section matching the user's chosen template.

    Args:
        full_content: Full EXAMPLES.md content.
        template_letter: "A", "B", "C", "D", or "E".

    Returns:
        The matching example section, or a fallback message.
    """
    # Map template letters to example headings
    template_to_example = {
        "A": "Example 1: Rubik's Cube",
        "B": "Example 3: LightsOut",
        "C": "Example 4: Grid Navigation",
        "D": "Example 5: Sokoban",
        "E": "Example 5: Sokoban",  # Closest match for logic templates
    }

    target_heading = template_to_example.get(template_letter, "Example 1")
    lines = full_content.split("\n")
    capturing = False
    section_lines = []

    for line in lines:
        if target_heading in line:
            capturing = True
        elif capturing and line.startswith("## Example") and target_heading not in line:
            break  # Hit the next example section
        elif capturing and line.startswith("# PART"):
            break  # Hit the next part

        if capturing:
            section_lines.append(line)

    if section_lines:
        return "\n".join(section_lines)
    return f"[No specific example found for Template {template_letter}]"


async def domain_guide(state: PipelineState) -> dict:
    """
    Handle the domain creation guide flow.

    This node is entered when:
    1. The route_classifier picks "domain_guide" (first entry), OR
    2. The session is already in a domain guide flow (continuation).

    Based on the current stage, it loads the appropriate context file
    and sets up the system prompt for the generate node.

    Args:
        state: Pipeline state with domain_guide_stage and query.

    Returns:
        State updates: domain_guide_stage, domain_guide_context,
        system_prompt, context_for_llm.
    """
    current_stage = state.get("domain_guide_stage", "none")
    query = state["query"]
    user_choices = state.get("domain_guide_user_choices", {})

    logger.info(f"Domain guide: current_stage={current_stage}, query={query[:60]}")

    # ── Stage transitions ───────────────────────────────────────────────

    if current_stage == "none":
        # First entry → show overview
        full_content = _load_file("ADDING_NEW_DOMAIN.md")
        overview = _extract_overview(full_content)

        system_prompt = (
            "You are a helpful assistant guiding a user through adding a new "
            "puzzle domain to DeepXube. You have been given the overview of the "
            "domain creation process.\n\n"
            "TASK: Present a brief, clear summary of the 5 things they need to "
            "create (State, Goal, Action, Domain, Parser class) and the 3 decisions "
            "they need to make (state representation, action space, reversibility). "
            "Keep it concise — just the high-level steps.\n\n"
            "Then ask: 'Would you like me to guide you through this step-by-step "
            "with code templates and examples?'"
        )

        return {
            "domain_guide_stage": "overview",
            "domain_guide_context": overview,
            "system_prompt": system_prompt,
            "context_for_llm": overview,
        }

    elif current_stage == "overview":
        # User responded to overview → load full template guide
        full_content = _load_file("ADDING_NEW_DOMAIN.md")

        system_prompt = (
            "You are guiding the user through creating a new puzzle domain for "
            "DeepXube. You have the full domain creation guide.\n\n"
            "TASK: Walk the user through the 3 decisions in order:\n"
            "1. State Representation (1D flat, 2D grid, custom, or logic)\n"
            "2. Action Space (fixed or variable per state)\n"
            "3. Reversibility (can moves be undone?)\n\n"
            "Based on their answers, identify the matching template (A/B/C/D/E) "
            "and provide the complete code template.\n\n"
            "The user's message is their response to your overview. They may "
            "answer all three questions at once or one at a time. Adapt accordingly.\n\n"
            "IMPORTANT: After providing the template, tell them to verify it with "
            "the 5 verification steps listed in the guide, then ask if they want "
            "to see a real-world example."
        )

        return {
            "domain_guide_stage": "template",
            "domain_guide_context": full_content,
            "system_prompt": system_prompt,
            "context_for_llm": full_content,
        }

    elif current_stage == "template":
        # User has the template → show matching example
        template_letter = user_choices.get("template", "A")
        examples_content = _load_file("EXAMPLES.md")
        example_section = _extract_example_section(examples_content, template_letter)

        system_prompt = (
            "You are helping the user implement their puzzle domain. They have "
            "already received a code template.\n\n"
            "TASK: Show them the real-world example that matches their chosen "
            "template pattern. Explain how the example implements each required "
            "method and how they should adapt it for their puzzle.\n\n"
            "After showing the example, ask if they've verified their domain "
            "works (using domain_info, time, etc.) and if they're ready to "
            "learn about training."
        )

        return {
            "domain_guide_stage": "examples",
            "domain_guide_context": example_section,
            "system_prompt": system_prompt,
            "context_for_llm": example_section,
        }

    elif current_stage == "examples":
        # User is ready for training → load training guide
        training_content = _load_file("TRAINING_GUIDE.md")

        system_prompt = (
            "You are guiding the user through training their newly created "
            "puzzle domain in DeepXube. You have the full training guide.\n\n"
            "TASK: Walk them through:\n"
            "1. Choosing network output type (V, QFix, or QIn)\n"
            "2. Supervised initialization (which pathfinder to use)\n"
            "3. RL refinement (A* vs Beam Search)\n\n"
            "Provide the exact CLI commands they need to run, customized for "
            "their domain name and template type.\n\n"
            "After providing the training commands, congratulate them and let "
            "them know they can ask any follow-up questions."
        )

        return {
            "domain_guide_stage": "training",
            "domain_guide_context": training_content,
            "system_prompt": system_prompt,
            "context_for_llm": training_content,
        }

    elif current_stage == "training":
        # Training guide delivered → reset and return to normal flow
        logger.info("Domain guide flow completed. Resetting to normal routing.")

        return {
            "domain_guide_stage": "none",
            "domain_guide_context": "",
            "domain_guide_user_choices": {},
        }

    # Fallback — should not reach here
    logger.warning(f"Unexpected domain guide stage: {current_stage}")
    return {"domain_guide_stage": "none"}
