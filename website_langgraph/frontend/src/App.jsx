// ============================================================================
// App Component — Root of the React application
// ============================================================================
// Sets up React Router with two pages: Chat (main) and Graph (placeholder).
// ============================================================================

import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Layout/Header";
import ChatWindow from "./components/Chat/ChatWindow";
import GraphExplorer from "./components/GraphExplorer/GraphExplorer";
import "./index.css";

export default function App() {
  return (
    <BrowserRouter>
      <div className="page-layout">
        <Header />
        <main className="page-content">
          <Routes>
            <Route path="/" element={<ChatWindow />} />
            <Route path="/graph" element={<GraphExplorer />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}
