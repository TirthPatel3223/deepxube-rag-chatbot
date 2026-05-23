# Skipped (trivial) functions

**Total skipped:** 394

*Triviality rule: ≤3 statements AND no control flow AND no calls to project functions.*

## `deepxube._cli`

- L45: `deepxube._cli.get_immediate_mixins` — ≤3 stmts, no control flow, no project calls
- L210: `deepxube._cli._viz_state_goal_update` — ≤3 stmts, no control flow, no project calls
- L367: `deepxube._cli._parser_domain_info` — ≤3 stmts, no control flow, no project calls
- L373: `deepxube._cli._parser_heur_info` — ≤3 stmts, no control flow, no project calls
- L379: `deepxube._cli._parser_pathfind_info` — ≤3 stmts, no control flow, no project calls
- L420: `deepxube._cli._parse_train_summary` — ≤3 stmts, no control flow, no project calls

## `deepxube.base.domain`

- L30: `deepxube.base.domain.State.__hash__` — ≤3 stmts, no control flow, no project calls
- L37: `deepxube.base.domain.State.__eq__` — ≤3 stmts, no control flow, no project calls
- L52: `deepxube.base.domain.Action.__hash__` — ≤3 stmts, no control flow, no project calls
- L59: `deepxube.base.domain.Action.__eq__` — ≤3 stmts, no control flow, no project calls
- L86: `deepxube.base.domain.Domain.__init__` — ≤3 stmts, no control flow, no project calls
- L91: `deepxube.base.domain.Domain.sample_problem_instances` — ≤3 stmts, no control flow, no project calls
- L101: `deepxube.base.domain.Domain.sample_state_action` — ≤3 stmts, no control flow, no project calls
- L110: `deepxube.base.domain.Domain.next_state` — ≤3 stmts, no control flow, no project calls
- L120: `deepxube.base.domain.Domain.is_solved` — ≤3 stmts, no control flow, no project calls
- L169: `deepxube.base.domain.Domain.get_nnet_pars` — ≤3 stmts, no control flow, no project calls
- L173: `deepxube.base.domain.Domain.set_nnet_fns` — ≤3 stmts, no control flow, no project calls
- L184: `deepxube.base.domain.StateGoalVizable.visualize_state_goal` — ≤3 stmts, no control flow, no project calls
- L194: `deepxube.base.domain.StringToAct.string_to_action` — ≤3 stmts, no control flow, no project calls
- L202: `deepxube.base.domain.StringToAct.string_to_action_help` — ≤3 stmts, no control flow, no project calls
- L214: `deepxube.base.domain.ActsFixed.sample_action` — ≤3 stmts, no control flow, no project calls
- L228: `deepxube.base.domain.ActsRev.rev_action` — ≤3 stmts, no control flow, no project calls
- L242: `deepxube.base.domain.ActsEnum.get_state_actions` — ≤3 stmts, no control flow, no project calls
- L306: `deepxube.base.domain.ActsEnumFixed.get_actions_fixed` — ≤3 stmts, no control flow, no project calls
- L319: `deepxube.base.domain.GoalSampleable.sample_goals` — ≤3 stmts, no control flow, no project calls
- L329: `deepxube.base.domain.GoalStateSampleable.sample_goal_states` — ≤3 stmts, no control flow, no project calls
- L339: `deepxube.base.domain.GoalSampleableFromState.sample_goal_from_state` — ≤3 stmts, no control flow, no project calls
- L352: `deepxube.base.domain.StateSampleableFromGoal.sample_state_from_goal` — ≤3 stmts, no control flow, no project calls
- L365: `deepxube.base.domain.GoalFixed.get_goal` — ≤3 stmts, no control flow, no project calls
- L379: `deepxube.base.domain.GoalStateGoalPairSampleable.sample_goalstate_goal_pairs` — ≤3 stmts, no control flow, no project calls
- L406: `deepxube.base.domain.StartGoalWalkable.sample_start_states` — ≤3 stmts, no control flow, no project calls
- L462: `deepxube.base.domain.GoalStartRevWalkable.random_walk_rev` — ≤3 stmts, no control flow, no project calls
- L522: `deepxube.base.domain.NextStateNP._states_to_np` — ≤3 stmts, no control flow, no project calls
- L527: `deepxube.base.domain.NextStateNP._np_to_states` — ≤3 stmts, no control flow, no project calls
- L532: `deepxube.base.domain.NextStateNP._sample_state_np_action` — ≤3 stmts, no control flow, no project calls
- L537: `deepxube.base.domain.NextStateNP._next_state_np` — ≤3 stmts, no control flow, no project calls
- L616: `deepxube.base.domain.SupportsPDDL.get_pddl_domain` — ≤3 stmts, no control flow, no project calls
- L621: `deepxube.base.domain.SupportsPDDL.prob_inst_to_pddl_inst` — ≤3 stmts, no control flow, no project calls
- L626: `deepxube.base.domain.SupportsPDDL.pddl_action_to_action` — ≤3 stmts, no control flow, no project calls
- L636: `deepxube.base.domain.GoalGrndAtoms.state_to_model` — ≤3 stmts, no control flow, no project calls
- L641: `deepxube.base.domain.GoalGrndAtoms.model_to_state` — ≤3 stmts, no control flow, no project calls
- L650: `deepxube.base.domain.GoalGrndAtoms.goal_to_model` — ≤3 stmts, no control flow, no project calls
- L655: `deepxube.base.domain.GoalGrndAtoms.model_to_goal` — ≤3 stmts, no control flow, no project calls
- L688: `deepxube.base.domain.GoalGrndAtoms.get_bk` — ≤3 stmts, no control flow, no project calls
- L696: `deepxube.base.domain.GoalGrndAtoms.get_ground_atoms` — ≤3 stmts, no control flow, no project calls
- L704: `deepxube.base.domain.GoalGrndAtoms.on_model` — ≤3 stmts, no control flow, no project calls
- L713: `deepxube.base.domain.GoalGrndAtoms.start_state_fixed` — ≤3 stmts, no control flow, no project calls

## `deepxube.base.factory`

- L31: `deepxube.base.factory.Parser.parse` — ≤3 stmts, no control flow, no project calls
- L42: `deepxube.base.factory.Parser.help` — ≤3 stmts, no control flow, no project calls
- L66: `deepxube.base.factory.Factory.__init__` — ≤3 stmts, no control flow, no project calls
- L174: `deepxube.base.factory.Factory.get_all_class_names` — ≤3 stmts, no control flow, no project calls

## `deepxube.base.heuristic`

- L37: `deepxube.base.heuristic.DeepXubeNNet.nnet_input_type` — ≤3 stmts, no control flow, no project calls
- L50: `deepxube.base.heuristic.DeepXubeNNet.forward` — ≤3 stmts, no control flow, no project calls
- L71: `deepxube.base.heuristic.HeurNNet.__init__` — ≤3 stmts, no control flow, no project calls
- L92: `deepxube.base.heuristic.HeurNNet._forward` — ≤3 stmts, no control flow, no project calls
- L105: `deepxube.base.heuristic.PolicyNNet.forward` — ≤3 stmts, no control flow, no project calls
- L114: `deepxube.base.heuristic.PolicyNNet.train_fprop` — ≤3 stmts, no control flow, no project calls
- L166: `deepxube.base.heuristic.PolicyVAE.latent_shape` — ≤3 stmts, no control flow, no project calls
- L171: `deepxube.base.heuristic.PolicyVAE.encode` — ≤3 stmts, no control flow, no project calls
- L180: `deepxube.base.heuristic.PolicyVAE.decode` — ≤3 stmts, no control flow, no project calls
- L195: `deepxube.base.heuristic.PolicyVAE.__repr__` — dunder one-liner
- L205: `deepxube.base.heuristic.HeurFnV.__call__` — ≤3 stmts, no control flow, no project calls
- L214: `deepxube.base.heuristic.HeurFnQ.__call__` — ≤3 stmts, no control flow, no project calls
- L226: `deepxube.base.heuristic.PolicyFn.__call__` — ≤3 stmts, no control flow, no project calls
- L244: `deepxube.base.heuristic.HeurNNetPar.get_nnet` — ≤3 stmts, no control flow, no project calls
- L249: `deepxube.base.heuristic.HeurNNetPar.get_nnet_fn` — ≤3 stmts, no control flow, no project calls
- L254: `deepxube.base.heuristic.HeurNNetPar.get_nnet_par_fn` — ≤3 stmts, no control flow, no project calls
- L293: `deepxube.base.heuristic.HeurNNetParV.to_np` — ≤3 stmts, no control flow, no project calls
- L302: `deepxube.base.heuristic.HeurNNetParQ.get_nnet_fn` — ≤3 stmts, no control flow, no project calls
- L307: `deepxube.base.heuristic.HeurNNetParQ.get_nnet_par_fn` — ≤3 stmts, no control flow, no project calls
- L312: `deepxube.base.heuristic.HeurNNetParQ.to_np` — ≤3 stmts, no control flow, no project calls
- L347: `deepxube.base.heuristic.HeurNNetParQFixOut._to_np_fixed_acts` — ≤3 stmts, no control flow, no project calls
- L368: `deepxube.base.heuristic.HeurNNetParQFixOut._check_same_num_acts` — ≤3 stmts, no control flow, no project calls
- L405: `deepxube.base.heuristic.HeurNNetParQIn._to_np_one_act` — ≤3 stmts, no control flow, no project calls
- L476: `deepxube.base.heuristic.PolicyNNetPar.__init__` — ≤3 stmts, no control flow, no project calls
- L519: `deepxube.base.heuristic.PolicyNNetPar.get_nnet` — ≤3 stmts, no control flow, no project calls
- L524: `deepxube.base.heuristic.PolicyNNetPar.to_np_fn` — ≤3 stmts, no control flow, no project calls
- L529: `deepxube.base.heuristic.PolicyNNetPar.to_np_train` — ≤3 stmts, no control flow, no project calls
- L534: `deepxube.base.heuristic.PolicyNNetPar._nnet_out_to_actions` — ≤3 stmts, no control flow, no project calls
- L565: `deepxube.base.heuristic.PolicyNNetPar.__repr__` — dunder one-liner

## `deepxube.base.nnet_input`

- L29: `deepxube.base.nnet_input.NNetInput.__init__` — ≤3 stmts, no control flow, no project calls
- L34: `deepxube.base.nnet_input.NNetInput.get_input_info` — ≤3 stmts, no control flow, no project calls
- L39: `deepxube.base.nnet_input.NNetInput.to_np` — ≤3 stmts, no control flow, no project calls
- L48: `deepxube.base.nnet_input.FlatIn.get_input_info` — ≤3 stmts, no control flow, no project calls
- L61: `deepxube.base.nnet_input.TwoDIn.get_input_info` — ≤3 stmts, no control flow, no project calls
- L74: `deepxube.base.nnet_input.StateGoalIn.to_np` — ≤3 stmts, no control flow, no project calls
- L83: `deepxube.base.nnet_input.StateGoalActFixIn.to_np` — ≤3 stmts, no control flow, no project calls
- L92: `deepxube.base.nnet_input.StateGoalActIn.to_np` — ≤3 stmts, no control flow, no project calls
- L101: `deepxube.base.nnet_input.PolicyNNetIn.to_np` — ≤3 stmts, no control flow, no project calls
- L106: `deepxube.base.nnet_input.PolicyNNetIn.to_np_fn` — ≤3 stmts, no control flow, no project calls
- L111: `deepxube.base.nnet_input.PolicyNNetIn.nnet_out_to_actions` — ≤3 stmts, no control flow, no project calls
- L116: `deepxube.base.nnet_input.PolicyNNetIn.states_goals_actions_split_idx` — ≤3 stmts, no control flow, no project calls
- L133: `deepxube.base.nnet_input.DynamicNNetInput.__init_subclass__` — ≤3 stmts, no control flow, no project calls
- L140: `deepxube.base.nnet_input.DynamicNNetInput.register_nnet_input` — ≤3 stmts, no control flow, no project calls
- L145: `deepxube.base.nnet_input.DynamicNNetInput.get_dynamic_nnet_inputs` — ≤3 stmts, no control flow, no project calls
- L176: `deepxube.base.nnet_input.HasFlatSGIn.get_input_info_flat_sg` — ≤3 stmts, no control flow, no project calls
- L185: `deepxube.base.nnet_input.HasFlatSGIn.to_np_flat_sg` — ≤3 stmts, no control flow, no project calls
- L194: `deepxube.base.nnet_input.HasActsEnumFixedIn.actions_to_indices` — ≤3 stmts, no control flow, no project calls
- L252: `deepxube.base.nnet_input.HasFlatSGAIn.get_input_info_flat_sga` — ≤3 stmts, no control flow, no project calls
- L257: `deepxube.base.nnet_input.HasFlatSGAIn.to_np_flat_sga` — ≤3 stmts, no control flow, no project calls
- L288: `deepxube.base.nnet_input.HasTwoDSGIn.get_input_info_2d_sg` — ≤3 stmts, no control flow, no project calls
- L297: `deepxube.base.nnet_input.HasTwoDSGIn.to_np_2d_sg` — ≤3 stmts, no control flow, no project calls

## `deepxube.base.pathfinding`

- L50: `deepxube.base.pathfinding.Node.add_edge` — ≤3 stmts, no control flow, no project calls
- L143: `deepxube.base.pathfinding.EdgeQ.__init__` — ≤3 stmts, no control flow, no project calls
- L166: `deepxube.base.pathfinding.Instance.frontier_size` — ≤3 stmts, no control flow, no project calls
- L170: `deepxube.base.pathfinding.Instance.get_nodes` — ≤3 stmts, no control flow, no project calls
- L174: `deepxube.base.pathfinding.Instance.set_next_nodes` — ≤3 stmts, no control flow, no project calls
- L179: `deepxube.base.pathfinding.Instance.record_goal` — ≤3 stmts, no control flow, no project calls
- L183: `deepxube.base.pathfinding.Instance.add_nodes_popped` — ≤3 stmts, no control flow, no project calls
- L187: `deepxube.base.pathfinding.Instance.get_nodes_popped` — ≤3 stmts, no control flow, no project calls
- L191: `deepxube.base.pathfinding.Instance.add_edges_popped` — ≤3 stmts, no control flow, no project calls
- L195: `deepxube.base.pathfinding.Instance.get_edges_popped` — ≤3 stmts, no control flow, no project calls
- L215: `deepxube.base.pathfinding.Instance.finished` — ≤3 stmts, no control flow, no project calls
- L266: `deepxube.base.pathfinding.PathFind.domain_type` — ≤3 stmts, no control flow, no project calls
- L272: `deepxube.base.pathfinding.PathFind.functions_type` — ≤3 stmts, no control flow, no project calls
- L288: `deepxube.base.pathfinding.PathFind.make_instances` — ≤3 stmts, no control flow, no project calls
- L299: `deepxube.base.pathfinding.PathFind.add_instances` — ≤3 stmts, no control flow, no project calls
- L304: `deepxube.base.pathfinding.PathFind.expand_states` — ≤3 stmts, no control flow, no project calls
- L309: `deepxube.base.pathfinding.PathFind.get_state_actions` — ≤3 stmts, no control flow, no project calls
- L314: `deepxube.base.pathfinding.PathFind.step` — ≤3 stmts, no control flow, no project calls
- L363: `deepxube.base.pathfinding.PathFind._set_node_vals` — ≤3 stmts, no control flow, no project calls
- L406: `deepxube.base.pathfinding.InstanceNode.filter_expanded_nodes` — ≤3 stmts, no control flow, no project calls
- L411: `deepxube.base.pathfinding.InstanceNode.push_pop_nodes` — ≤3 stmts, no control flow, no project calls
- L423: `deepxube.base.pathfinding.InstanceEdge.filter_popped_nodes` — ≤3 stmts, no control flow, no project calls
- L428: `deepxube.base.pathfinding.InstanceEdge.push_pop_edges` — ≤3 stmts, no control flow, no project calls
- L576: `deepxube.base.pathfinding.PathFindNode._compute_costs` — ≤3 stmts, no control flow, no project calls
- L714: `deepxube.base.pathfinding.PathFindEdge._compute_costs` — ≤3 stmts, no control flow, no project calls
- L800: `deepxube.base.pathfinding.PathFindActsEnum.expand_states` — ≤3 stmts, no control flow, no project calls
- L804: `deepxube.base.pathfinding.PathFindActsEnum.get_state_actions` — ≤3 stmts, no control flow, no project calls
- L834: `deepxube.base.pathfinding.PathFindActsPolicy.get_state_actions` — ≤3 stmts, no control flow, no project calls
- L847: `deepxube.base.pathfinding.PathFindSup.functions_type` — ≤3 stmts, no control flow, no project calls
- L851: `deepxube.base.pathfinding.PathFindSup.make_instances` — ≤3 stmts, no control flow, no project calls
- L855: `deepxube.base.pathfinding.PathFindSup.expand_states` — ≤3 stmts, no control flow, no project calls
- L859: `deepxube.base.pathfinding.PathFindSup.get_state_actions` — ≤3 stmts, no control flow, no project calls
- L864: `deepxube.base.pathfinding.PathFindSup.make_instances_rw` — ≤3 stmts, no control flow, no project calls
- L870: `deepxube.base.pathfinding.PathFindSup._set_node_vals` — ≤3 stmts, no control flow, no project calls

## `deepxube.base.trainer`

- L104: `deepxube.base.trainer.DataBuffer.size` — ≤3 stmts, no control flow, no project calls
- L108: `deepxube.base.trainer.DataBuffer.clear` — ≤3 stmts, no control flow, no project calls
- L171: `deepxube.base.trainer.TrainSummary.__init__` — ≤3 stmts, no control flow, no project calls
- L206: `deepxube.base.trainer.Train.data_parallel` — ≤3 stmts, no control flow, no project calls
- L388: `deepxube.base.trainer.Train._train_itr` — ≤3 stmts, no control flow, no project calls
- L414: `deepxube.base.trainer.Train._add_post_up_info` — ≤3 stmts, no control flow, no project calls
- L419: `deepxube.base.trainer.Train._get_shapes_dtypes` — ≤3 stmts, no control flow, no project calls

## `deepxube.base.updater`

- L77: `deepxube.base.updater.UpArgs.get_up_gen_itrs` — ≤3 stmts, no control flow, no project calls
- L111: `deepxube.base.updater.Update.domain_type` — ≤3 stmts, no control flow, no project calls
- L117: `deepxube.base.updater.Update.functions_type` — ≤3 stmts, no control flow, no project calls
- L123: `deepxube.base.updater.Update.pathfind_type` — ≤3 stmts, no control flow, no project calls
- L188: `deepxube.base.updater.Update.clear_nnet_fn_dict` — ≤3 stmts, no control flow, no project calls
- L192: `deepxube.base.updater.Update.add_nnet_par` — ≤3 stmts, no control flow, no project calls
- L197: `deepxube.base.updater.Update.set_nnet_file` — ≤3 stmts, no control flow, no project calls
- L370: `deepxube.base.updater.Update.set_targ_update_num` — ≤3 stmts, no control flow, no project calls
- L475: `deepxube.base.updater.Update._step` — ≤3 stmts, no control flow, no project calls
- L480: `deepxube.base.updater.Update._step_sync_main` — ≤3 stmts, no control flow, no project calls
- L485: `deepxube.base.updater.Update._get_pathfind_functions` — ≤3 stmts, no control flow, no project calls
- L497: `deepxube.base.updater.Update._get_instance_data_norb` — ≤3 stmts, no control flow, no project calls
- L502: `deepxube.base.updater.Update._get_instance_data_rb` — ≤3 stmts, no control flow, no project calls
- L507: `deepxube.base.updater.Update._make_instances` — ≤3 stmts, no control flow, no project calls
- L512: `deepxube.base.updater.Update._init_replay_buffer` — ≤3 stmts, no control flow, no project calls
- L516: `deepxube.base.updater.Update.__repr__` — dunder one-liner
- L524: `deepxube.base.updater.UpdateHER._step_sync_main` — ≤3 stmts, no control flow, no project calls
- L529: `deepxube.base.updater.UpdateHER._get_instance_data_norb` — ≤3 stmts, no control flow, no project calls
- L593: `deepxube.base.updater.UpdateHasHeur.heur_name` — ≤3 stmts, no control flow, no project calls
- L622: `deepxube.base.updater.UpdateHasPolicy.policy_name` — ≤3 stmts, no control flow, no project calls
- L654: `deepxube.base.updater.UpdateSup.functions_type` — ≤3 stmts, no control flow, no project calls
- L658: `deepxube.base.updater.UpdateSup._step` — ≤3 stmts, no control flow, no project calls
- L662: `deepxube.base.updater.UpdateSup._get_pathfind_functions` — ≤3 stmts, no control flow, no project calls
- L666: `deepxube.base.updater.UpdateSup._make_instances` — ≤3 stmts, no control flow, no project calls
- L670: `deepxube.base.updater.UpdateSup._step_sync_main` — ≤3 stmts, no control flow, no project calls
- L674: `deepxube.base.updater.UpdateSup._get_instance_data_rb` — ≤3 stmts, no control flow, no project calls
- L678: `deepxube.base.updater.UpdateSup._init_replay_buffer` — ≤3 stmts, no control flow, no project calls
- L701: `deepxube.base.updater.UpdateHeur.get_heur_train_shapes_dtypes` — ≤3 stmts, no control flow, no project calls

## `deepxube.domains.cube3`

- L20: `deepxube.domains.cube3.Cube3State.__init__` — ≤3 stmts, no control flow, no project calls
- L30: `deepxube.domains.cube3.Cube3State.__eq__` — dunder one-liner
- L39: `deepxube.domains.cube3.Cube3Goal.__init__` — ≤3 stmts, no control flow, no project calls
- L46: `deepxube.domains.cube3.Cube3Action.__init__` — ≤3 stmts, no control flow, no project calls
- L49: `deepxube.domains.cube3.Cube3Action.__hash__` — dunder one-liner
- L52: `deepxube.domains.cube3.Cube3Action.__eq__` — dunder one-liner
- L112: `deepxube.domains.cube3.Quaternion.__repr__` — dunder one-liner
- L404: `deepxube.domains.cube3.InteractiveCube.rotate` — ≤3 stmts, no control flow, no project calls
- L557: `deepxube.domains.cube3.Cube3.get_input_info_flat_sg` — ≤3 stmts, no control flow, no project calls
- L574: `deepxube.domains.cube3.Cube3.actions_to_indices` — ≤3 stmts, no control flow, no project calls
- L590: `deepxube.domains.cube3.Cube3.string_to_action_help` — ≤3 stmts, no control flow, no project calls
- L593: `deepxube.domains.cube3.Cube3.get_actions_fixed` — ≤3 stmts, no control flow, no project calls
- L711: `deepxube.domains.cube3.Cube3.__repr__` — dunder one-liner

## `deepxube.domains.grid`

- L29: `deepxube.domains.grid.GridState.__init__` — ≤3 stmts, no control flow, no project calls
- L33: `deepxube.domains.grid.GridState.__hash__` — dunder one-liner
- L36: `deepxube.domains.grid.GridState.__eq__` — dunder one-liner
- L45: `deepxube.domains.grid.GridGoal.__init__` — ≤3 stmts, no control flow, no project calls
- L53: `deepxube.domains.grid.GridAction.__init__` — ≤3 stmts, no control flow, no project calls
- L56: `deepxube.domains.grid.GridAction.__hash__` — dunder one-liner
- L59: `deepxube.domains.grid.GridAction.__eq__` — dunder one-liner
- L64: `deepxube.domains.grid.GridAction.__repr__` — dunder one-liner
- L81: `deepxube.domains.grid.Grid.is_solved` — ≤3 stmts, no control flow, no project calls
- L107: `deepxube.domains.grid.Grid.get_input_info_flat_sg` — ≤3 stmts, no control flow, no project calls
- L123: `deepxube.domains.grid.Grid.actions_to_indices` — ≤3 stmts, no control flow, no project calls
- L142: `deepxube.domains.grid.Grid.string_to_action_help` — ≤3 stmts, no control flow, no project calls
- L145: `deepxube.domains.grid.Grid.get_actions_fixed` — ≤3 stmts, no control flow, no project calls
- L148: `deepxube.domains.grid.Grid.__repr__` — dunder one-liner
- L156: `deepxube.domains.grid.GridParser.parse` — ≤3 stmts, no control flow, no project calls
- L159: `deepxube.domains.grid.GridParser.help` — ≤3 stmts, no control flow, no project calls
- L167: `deepxube.domains.grid.GridNNetInput.get_input_info` — ≤3 stmts, no control flow, no project calls
- L185: `deepxube.domains.grid.GridNet.nnet_input_type` — ≤3 stmts, no control flow, no project calls
- L227: `deepxube.domains.grid.GridNetParser.help` — ≤3 stmts, no control flow, no project calls

## `deepxube.domains.lightsout`

- L18: `deepxube.domains.lightsout.LOState.__init__` — ≤3 stmts, no control flow, no project calls
- L29: `deepxube.domains.lightsout.LOState.__eq__` — dunder one-liner
- L38: `deepxube.domains.lightsout.LOGoal.__init__` — ≤3 stmts, no control flow, no project calls
- L45: `deepxube.domains.lightsout.LOAction.__init__` — ≤3 stmts, no control flow, no project calls
- L48: `deepxube.domains.lightsout.LOAction.__hash__` — dunder one-liner
- L51: `deepxube.domains.lightsout.LOAction.__eq__` — dunder one-liner
- L98: `deepxube.domains.lightsout.LightsOut.rev_action` — ≤3 stmts, no control flow, no project calls
- L101: `deepxube.domains.lightsout.LightsOut.get_input_info_flat_sg` — ≤3 stmts, no control flow, no project calls
- L116: `deepxube.domains.lightsout.LightsOut.get_input_info_2d_sg` — ≤3 stmts, no control flow, no project calls
- L124: `deepxube.domains.lightsout.LightsOut.actions_to_indices` — ≤3 stmts, no control flow, no project calls
- L127: `deepxube.domains.lightsout.LightsOut.get_actions_fixed` — ≤3 stmts, no control flow, no project calls
- L153: `deepxube.domains.lightsout.LightsOut.__repr__` — dunder one-liner
- L161: `deepxube.domains.lightsout.LightsOutParser.parse` — ≤3 stmts, no control flow, no project calls
- L164: `deepxube.domains.lightsout.LightsOutParser.help` — ≤3 stmts, no control flow, no project calls

## `deepxube.domains.npuzzle`

- L24: `deepxube.domains.npuzzle.NPState.__init__` — ≤3 stmts, no control flow, no project calls
- L28: `deepxube.domains.npuzzle.NPState.__hash__` — dunder one-liner
- L33: `deepxube.domains.npuzzle.NPState.__eq__` — dunder one-liner
- L42: `deepxube.domains.npuzzle.NPGoal.__init__` — ≤3 stmts, no control flow, no project calls
- L49: `deepxube.domains.npuzzle.NPAction.__init__` — ≤3 stmts, no control flow, no project calls
- L52: `deepxube.domains.npuzzle.NPAction.__hash__` — dunder one-liner
- L55: `deepxube.domains.npuzzle.NPAction.__eq__` — dunder one-liner
- L160: `deepxube.domains.npuzzle.NPuzzle.get_actions_fixed` — ≤3 stmts, no control flow, no project calls
- L184: `deepxube.domains.npuzzle.NPuzzle.get_input_info_flat_sg` — ≤3 stmts, no control flow, no project calls
- L232: `deepxube.domains.npuzzle.NPuzzle.string_to_action_help` — ≤3 stmts, no control flow, no project calls
- L353: `deepxube.domains.npuzzle.NPuzzle.__repr__` — dunder one-liner
- L361: `deepxube.domains.npuzzle.GridParser.parse` — ≤3 stmts, no control flow, no project calls
- L364: `deepxube.domains.npuzzle.GridParser.help` — ≤3 stmts, no control flow, no project calls

## `deepxube.domains.sokoban`

- L59: `deepxube.domains.sokoban.SkGoal.__init__` — ≤3 stmts, no control flow, no project calls
- L65: `deepxube.domains.sokoban.SkAction.__init__` — ≤3 stmts, no control flow, no project calls
- L68: `deepxube.domains.sokoban.SkAction.__hash__` — dunder one-liner
- L71: `deepxube.domains.sokoban.SkAction.__eq__` — dunder one-liner
- L228: `deepxube.domains.sokoban.Sokoban.get_actions_fixed` — ≤3 stmts, no control flow, no project calls
- L269: `deepxube.domains.sokoban.Sokoban.string_to_action_help` — ≤3 stmts, no control flow, no project calls
- L337: `deepxube.domains.sokoban.Sokoban.__getstate__` — ≤3 stmts, no control flow, no project calls
- L343: `deepxube.domains.sokoban.Sokoban.__repr__` — dunder one-liner
- L351: `deepxube.domains.sokoban.SkNNetInput.get_input_info` — ≤3 stmts, no control flow, no project calls

## `deepxube.factories.heuristic_factory`

- L154: `deepxube.factories.heuristic_factory.HeurNNetParFacClass.__getstate__` — ≤3 stmts, no control flow, no project calls
- L211: `deepxube.factories.heuristic_factory.PolicyNNetParFacClass.__getstate__` — ≤3 stmts, no control flow, no project calls
- L226: `deepxube.factories.heuristic_factory.HeurNNetParVConcrete.__init__` — ≤3 stmts, no control flow, no project calls
- L246: `deepxube.factories.heuristic_factory.HeurNNetParVConcrete._get_nnet_input` — ≤3 stmts, no control flow, no project calls
- L261: `deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete.__init__` — ≤3 stmts, no control flow, no project calls
- L283: `deepxube.factories.heuristic_factory.HeurNNetParQFixOutConcrete._get_nnet_input` — ≤3 stmts, no control flow, no project calls
- L299: `deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete.__init__` — ≤3 stmts, no control flow, no project calls
- L321: `deepxube.factories.heuristic_factory.HeurNNetParQActInConcrete._get_nnet_input` — ≤3 stmts, no control flow, no project calls

## `deepxube.factories.nnet_input_factory`

- L40: `deepxube.factories.nnet_input_factory.get_domain_nnet_input_keys` — ≤3 stmts, no control flow, no project calls
- L50: `deepxube.factories.nnet_input_factory.get_nnet_input_t` — ≤3 stmts, no control flow, no project calls

## `deepxube.heuristics.resnet_2d`

- L23: `deepxube.heuristics.resnet_2d.Resnet2D.nnet_input_type` — ≤3 stmts, no control flow, no project calls
- L105: `deepxube.heuristics.resnet_2d.ResnetFCParser.help` — ≤3 stmts, no control flow, no project calls

## `deepxube.heuristics.resnet_fc`

- L23: `deepxube.heuristics.resnet_fc.ResnetFCHeur.nnet_input_type` — ≤3 stmts, no control flow, no project calls
- L67: `deepxube.heuristics.resnet_fc.ResnetFCPolicy.nnet_input_type` — ≤3 stmts, no control flow, no project calls
- L108: `deepxube.heuristics.resnet_fc.ResnetFCPolicy.latent_shape` — ≤3 stmts, no control flow, no project calls
- L152: `deepxube.heuristics.resnet_fc.ResnetFCParserHeur.help` — ≤3 stmts, no control flow, no project calls
- L190: `deepxube.heuristics.resnet_fc.ResnetFCParserPolicy.help` — ≤3 stmts, no control flow, no project calls

## `deepxube.logic.asp`

- L22: `deepxube.logic.asp.on_model_var_vals` — ≤3 stmts, no control flow, no project calls
- L141: `deepxube.logic.asp.Solver.get_num_ground_rules` — ≤3 stmts, no control flow, no project calls

## `deepxube.logic.logic_objects`

- L42: `deepxube.logic.logic_objects.Literal.get_pred_arity_pos_id` — ≤3 stmts, no control flow, no project calls
- L46: `deepxube.logic.logic_objects.Literal.__str__` — dunder one-liner
- L49: `deepxube.logic.logic_objects.Literal.__repr__` — dunder one-liner
- L56: `deepxube.logic.logic_objects.VarNode.__init__` — ≤3 stmts, no control flow, no project calls
- L60: `deepxube.logic.logic_objects.VarNode.add_neighbor` — ≤3 stmts, no control flow, no project calls
- L77: `deepxube.logic.logic_objects.LitNode.prop_up` — ≤3 stmts, no control flow, no project calls
- L223: `deepxube.logic.logic_objects.Clause.__repr__` — dunder one-liner

## `deepxube.logic.logic_utils`

- L108: `deepxube.logic.logic_utils.atom_to_str` — ≤3 stmts, no control flow, no project calls

## `deepxube.nnet.nnet_utils`

- L237: `deepxube.nnet.nnet_utils.NNetPar.get_nnet_fn` — ≤3 stmts, no control flow, no project calls
- L243: `deepxube.nnet.nnet_utils.NNetPar.get_nnet_par_fn` — ≤3 stmts, no control flow, no project calls
- L248: `deepxube.nnet.nnet_utils.NNetPar.get_nnet` — ≤3 stmts, no control flow, no project calls
- L252: `deepxube.nnet.nnet_utils.NNetPar.__repr__` — dunder one-liner

## `deepxube.nnet.pytorch_models`

- L15: `deepxube.nnet.pytorch_models.OneHot.__init__` — ≤3 stmts, no control flow, no project calls
- L104: `deepxube.nnet.pytorch_models.SPLASH1.forward` — ≤3 stmts, no control flow, no project calls
- L113: `deepxube.nnet.pytorch_models.LinearAct.__init__` — ≤3 stmts, no control flow, no project calls
- L117: `deepxube.nnet.pytorch_models.LinearAct.forward` — ≤3 stmts, no control flow, no project calls

## `deepxube.pathfinding.beam_search`

- L31: `deepxube.pathfinding.beam_search.InstanceBeam.set_beam_size` — ≤3 stmts, no control flow, no project calls
- L36: `deepxube.pathfinding.beam_search.InstanceBeam.set_temp` — ≤3 stmts, no control flow, no project calls
- L41: `deepxube.pathfinding.beam_search.InstanceBeam.set_eps` — ≤3 stmts, no control flow, no project calls
- L46: `deepxube.pathfinding.beam_search.InstanceBeam.frontier_size` — ≤3 stmts, no control flow, no project calls
- L121: `deepxube.pathfinding.beam_search.BeamSearch.__repr__` — dunder one-liner
- L128: `deepxube.pathfinding.beam_search.InstanceNodeBeam.filter_expanded_nodes` — ≤3 stmts, no control flow, no project calls
- L141: `deepxube.pathfinding.beam_search.InstanceEdgeBeam.__init__` — ≤3 stmts, no control flow, no project calls
- L146: `deepxube.pathfinding.beam_search.InstanceEdgeBeam.filter_popped_nodes` — ≤3 stmts, no control flow, no project calls
- L162: `deepxube.pathfinding.beam_search.BeamSearchPolicy.domain_type` — ≤3 stmts, no control flow, no project calls
- L167: `deepxube.pathfinding.beam_search.BeamSearchPolicy.functions_type` — ≤3 stmts, no control flow, no project calls
- L245: `deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsEnum.domain_type` — ≤3 stmts, no control flow, no project calls
- L250: `deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsEnum.functions_type` — ≤3 stmts, no control flow, no project calls
- L260: `deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsEnum.domain_type` — ≤3 stmts, no control flow, no project calls
- L265: `deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsEnum.functions_type` — ≤3 stmts, no control flow, no project calls
- L275: `deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsPolicy.domain_type` — ≤3 stmts, no control flow, no project calls
- L280: `deepxube.pathfinding.beam_search.BeamSearchHeurNodeActsPolicy.functions_type` — ≤3 stmts, no control flow, no project calls
- L290: `deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsPolicy.domain_type` — ≤3 stmts, no control flow, no project calls
- L295: `deepxube.pathfinding.beam_search.BeamSearchHeurEdgeActsPolicy.functions_type` — ≤3 stmts, no control flow, no project calls
- L327: `deepxube.pathfinding.beam_search.BeamSearchParser._alg_name` — ≤3 stmts, no control flow, no project calls
- L336: `deepxube.pathfinding.beam_search.BeamSearchPolicyParser._alg_name` — ≤3 stmts, no control flow, no project calls
- L344: `deepxube.pathfinding.beam_search.BeamSearchNodeParser._alg_name` — ≤3 stmts, no control flow, no project calls
- L352: `deepxube.pathfinding.beam_search.BeamSearchEdgeParser._alg_name` — ≤3 stmts, no control flow, no project calls
- L360: `deepxube.pathfinding.beam_search.BeamSearchNodeHasPolicyParser._alg_name` — ≤3 stmts, no control flow, no project calls
- L368: `deepxube.pathfinding.beam_search.BeamSearchEdgeHasPolicyParser._alg_name` — ≤3 stmts, no control flow, no project calls

## `deepxube.pathfinding.graph_search`

- L39: `deepxube.pathfinding.graph_search.InstanceGraph.set_batch_size` — ≤3 stmts, no control flow, no project calls
- L44: `deepxube.pathfinding.graph_search.InstanceGraph.set_weight` — ≤3 stmts, no control flow, no project calls
- L49: `deepxube.pathfinding.graph_search.InstanceGraph.set_eps` — ≤3 stmts, no control flow, no project calls
- L54: `deepxube.pathfinding.graph_search.InstanceGraph.frontier_size` — ≤3 stmts, no control flow, no project calls
- L67: `deepxube.pathfinding.graph_search.InstanceGraph.finished` — ≤3 stmts, no control flow, no project calls
- L143: `deepxube.pathfinding.graph_search.GraphSearch.__repr__` — dunder one-liner
- L150: `deepxube.pathfinding.graph_search.InstanceNodeGraph.__init__` — ≤3 stmts, no control flow, no project calls
- L232: `deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsEnum.domain_type` — ≤3 stmts, no control flow, no project calls
- L237: `deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsEnum.functions_type` — ≤3 stmts, no control flow, no project calls
- L247: `deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsEnum.domain_type` — ≤3 stmts, no control flow, no project calls
- L252: `deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsEnum.functions_type` — ≤3 stmts, no control flow, no project calls
- L262: `deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsPolicy.domain_type` — ≤3 stmts, no control flow, no project calls
- L267: `deepxube.pathfinding.graph_search.GraphSearchHeurNodeActsPolicy.functions_type` — ≤3 stmts, no control flow, no project calls
- L277: `deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsPolicy.domain_type` — ≤3 stmts, no control flow, no project calls
- L282: `deepxube.pathfinding.graph_search.GraphSearchHeurEdgeActsPolicy.functions_type` — ≤3 stmts, no control flow, no project calls
- L314: `deepxube.pathfinding.graph_search.GraphSearchParser._alg_name` — ≤3 stmts, no control flow, no project calls
- L323: `deepxube.pathfinding.graph_search.GraphSearchNodeParser._alg_name` — ≤3 stmts, no control flow, no project calls
- L331: `deepxube.pathfinding.graph_search.GraphSearchEdgeParser._alg_name` — ≤3 stmts, no control flow, no project calls
- L339: `deepxube.pathfinding.graph_search.GraphSearchNodeHasPolicyParser._alg_name` — ≤3 stmts, no control flow, no project calls
- L347: `deepxube.pathfinding.graph_search.GraphSearchEdgeHasPolicyParser._alg_name` — ≤3 stmts, no control flow, no project calls

## `deepxube.pathfinding.supervised_q`

- L17: `deepxube.pathfinding.supervised_q.InstanceEdgeSup.filter_popped_nodes` — ≤3 stmts, no control flow, no project calls
- L21: `deepxube.pathfinding.supervised_q.InstanceEdgeSup.push_pop_edges` — ≤3 stmts, no control flow, no project calls
- L25: `deepxube.pathfinding.supervised_q.InstanceEdgeSup.frontier_size` — ≤3 stmts, no control flow, no project calls
- L29: `deepxube.pathfinding.supervised_q.InstanceEdgeSup.record_goal` — ≤3 stmts, no control flow, no project calls
- L33: `deepxube.pathfinding.supervised_q.InstanceEdgeSup.__init__` — ≤3 stmts, no control flow, no project calls
- L39: `deepxube.pathfinding.supervised_q.InstanceEdgeSup.finished` — ≤3 stmts, no control flow, no project calls
- L66: `deepxube.pathfinding.supervised_q.PathFindEdgeSup._compute_costs` — ≤3 stmts, no control flow, no project calls
- L88: `deepxube.pathfinding.supervised_q.PathFindEdgeSup.__repr__` — dunder one-liner
- L97: `deepxube.pathfinding.supervised_q.PathFindEdgeSupRW.domain_type` — ≤3 stmts, no control flow, no project calls
- L137: `deepxube.pathfinding.supervised_q.PathFindEdgeSupRWRev.domain_type` — ≤3 stmts, no control flow, no project calls

## `deepxube.pathfinding.supervised_v`

- L16: `deepxube.pathfinding.supervised_v.InstanceNodeSup.filter_expanded_nodes` — ≤3 stmts, no control flow, no project calls
- L20: `deepxube.pathfinding.supervised_v.InstanceNodeSup.frontier_size` — ≤3 stmts, no control flow, no project calls
- L24: `deepxube.pathfinding.supervised_v.InstanceNodeSup.record_goal` — ≤3 stmts, no control flow, no project calls
- L28: `deepxube.pathfinding.supervised_v.InstanceNodeSup.push_pop_nodes` — ≤3 stmts, no control flow, no project calls
- L32: `deepxube.pathfinding.supervised_v.InstanceNodeSup.__init__` — ≤3 stmts, no control flow, no project calls
- L37: `deepxube.pathfinding.supervised_v.InstanceNodeSup.finished` — ≤3 stmts, no control flow, no project calls
- L64: `deepxube.pathfinding.supervised_v.PathFindNodeSup._compute_costs` — ≤3 stmts, no control flow, no project calls
- L83: `deepxube.pathfinding.supervised_v.PathFindNodeSup.__repr__` — dunder one-liner
- L92: `deepxube.pathfinding.supervised_v.PathFindNodeSupRW.domain_type` — ≤3 stmts, no control flow, no project calls
- L119: `deepxube.pathfinding.supervised_v.PathFindNodeSupRWRev.domain_type` — ≤3 stmts, no control flow, no project calls

## `deepxube.trainers.train_heur`

- L22: `deepxube.trainers.train_heur.TrainHeur.data_parallel` — ≤3 stmts, no control flow, no project calls
- L51: `deepxube.trainers.train_heur.TrainHeur._get_shapes_dtypes` — ≤3 stmts, no control flow, no project calls

## `deepxube.trainers.train_policy`

- L20: `deepxube.trainers.train_policy.TrainPolicy.data_parallel` — ≤3 stmts, no control flow, no project calls
- L35: `deepxube.trainers.train_policy.TrainPolicy._add_post_up_info` — ≤3 stmts, no control flow, no project calls
- L38: `deepxube.trainers.train_policy.TrainPolicy._get_shapes_dtypes` — ≤3 stmts, no control flow, no project calls

## `deepxube.trainers.utils.train_loop`

- L40: `deepxube.trainers.utils.train_loop.TestArgs.__repr__` — dunder one-liner

## `deepxube.updaters.updater_policy_rl`

- L22: `deepxube.updaters.updater_policy_rl._pathfind_step` — ≤3 stmts, no control flow, no project calls
- L48: `deepxube.updaters.updater_policy_rl.UpdatePolicyRL.pathfind_type` — ≤3 stmts, no control flow, no project calls
- L104: `deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalABC.domain_type` — ≤3 stmts, no control flow, no project calls
- L163: `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERABC.domain_type` — ≤3 stmts, no control flow, no project calls
- L201: `deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoal.functions_type` — ≤3 stmts, no control flow, no project calls
- L215: `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHER.functions_type` — ≤3 stmts, no control flow, no project calls
- L230: `deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalHeurV.functions_type` — ≤3 stmts, no control flow, no project calls
- L244: `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurV.functions_type` — ≤3 stmts, no control flow, no project calls
- L259: `deepxube.updaters.updater_policy_rl.UpdatePolicyRLKeepGoalHeurQ.functions_type` — ≤3 stmts, no control flow, no project calls
- L273: `deepxube.updaters.updater_policy_rl.UpdatePolicyRLHERHeurQ.functions_type` — ≤3 stmts, no control flow, no project calls

## `deepxube.updaters.updater_q_rl`

- L21: `deepxube.updaters.updater_q_rl._pathfind_q_step` — ≤3 stmts, no control flow, no project calls
- L58: `deepxube.updaters.updater_q_rl.UpdateHeurQRL.pathfind_type` — ≤3 stmts, no control flow, no project calls
- L123: `deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalABC.domain_type` — ≤3 stmts, no control flow, no project calls
- L203: `deepxube.updaters.updater_q_rl.UpdateHeurQRLHERABC.domain_type` — ≤3 stmts, no control flow, no project calls
- L253: `deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoal.functions_type` — ≤3 stmts, no control flow, no project calls
- L267: `deepxube.updaters.updater_q_rl.UpdateHeurQRLHER.functions_type` — ≤3 stmts, no control flow, no project calls
- L281: `deepxube.updaters.updater_q_rl.UpdateHeurQRLKeepGoalPolicy.functions_type` — ≤3 stmts, no control flow, no project calls
- L295: `deepxube.updaters.updater_q_rl.UpdateHeurQRLHERPolicy.functions_type` — ≤3 stmts, no control flow, no project calls

## `deepxube.updaters.updater_sup`

- L31: `deepxube.updaters.updater_sup.UpdatePolicySup.domain_type` — ≤3 stmts, no control flow, no project calls
- L36: `deepxube.updaters.updater_sup.UpdatePolicySup.pathfind_type` — ≤3 stmts, no control flow, no project calls
- L68: `deepxube.updaters.updater_sup.UpdateHeurVSup.domain_type` — ≤3 stmts, no control flow, no project calls
- L73: `deepxube.updaters.updater_sup.UpdateHeurVSup.pathfind_type` — ≤3 stmts, no control flow, no project calls
- L104: `deepxube.updaters.updater_sup.UpdateHeurQSup.domain_type` — ≤3 stmts, no control flow, no project calls
- L109: `deepxube.updaters.updater_sup.UpdateHeurQSup.pathfind_type` — ≤3 stmts, no control flow, no project calls

## `deepxube.updaters.updater_v_rl`

- L22: `deepxube.updaters.updater_v_rl._pathfind_v_step` — ≤3 stmts, no control flow, no project calls
- L52: `deepxube.updaters.updater_v_rl.UpdateHeurVRL.pathfind_type` — ≤3 stmts, no control flow, no project calls
- L128: `deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalABC.domain_type` — ≤3 stmts, no control flow, no project calls
- L203: `deepxube.updaters.updater_v_rl.UpdateHeurVRLHERABC.domain_type` — ≤3 stmts, no control flow, no project calls
- L242: `deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoal.functions_type` — ≤3 stmts, no control flow, no project calls
- L256: `deepxube.updaters.updater_v_rl.UpdateHeurVRLHER.functions_type` — ≤3 stmts, no control flow, no project calls
- L270: `deepxube.updaters.updater_v_rl.UpdateHeurVRLKeepGoalPolicy.functions_type` — ≤3 stmts, no control flow, no project calls
- L284: `deepxube.updaters.updater_v_rl.UpdateHeurVRLHERPolicy.functions_type` — ≤3 stmts, no control flow, no project calls

## `deepxube.updaters.utils.replay_buffer_utils`

- L44: `deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.add` — ≤3 stmts, no control flow, no project calls
- L63: `deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.size` — ≤3 stmts, no control flow, no project calls
- L70: `deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer.max_size` — ≤3 stmts, no control flow, no project calls
- L81: `deepxube.updaters.utils.replay_buffer_utils.ReplayBuffer._elems_to_ret` — ≤3 stmts, no control flow, no project calls

## `deepxube.utils.data_utils`

- L31: `deepxube.utils.data_utils.Logger.__init__` — ≤3 stmts, no control flow, no project calls
- L54: `deepxube.utils.data_utils.Logger.flush` — ≤3 stmts, no control flow, no project calls
- L206: `deepxube.utils.data_utils.SharedNDArray.name` — ≤3 stmts, no control flow, no project calls
- L213: `deepxube.utils.data_utils.SharedNDArray.close` — ≤3 stmts, no control flow, no project calls
- L217: `deepxube.utils.data_utils.SharedNDArray.unlink` — ≤3 stmts, no control flow, no project calls
- L223: `deepxube.utils.data_utils.SharedNDArray.__reduce__` — ≤3 stmts, no control flow, no project calls
- L234: `deepxube.utils.data_utils.SharedNDArray.__setitem__` — ≤3 stmts, no control flow, no project calls
- L237: `deepxube.utils.data_utils.SharedNDArray.__array__` — ≤3 stmts, no control flow, no project calls
- L240: `deepxube.utils.data_utils.SharedNDArray.__repr__` — dunder one-liner

## `deepxube.utils.timing_utils`

- L187: `deepxube.utils.timing_utils.Times.__str__` — dunder one-liner
- L190: `deepxube.utils.timing_utils.Times.__repr__` — dunder one-liner

## `tests.test_domains`

- L57: `tests.test_domains.test_get_start_goal_pairs` — ≤3 stmts, no control flow, no project calls
- L65: `tests.test_domains.test_get_start_goal_pairs_0steps` — ≤3 stmts, no control flow, no project calls
- L72: `tests.test_domains.test_goalsamp` — ≤3 stmts, no control flow, no project calls
