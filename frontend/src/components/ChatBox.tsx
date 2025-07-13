import React, { useState } from "react";
import askQuestion, { type AskResponse } from "../api/rag";

const ChatBox: React.FC = () => {
  const [query, setQuery] = useState<string>("");
  const [response, setResponse] = useState<AskResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handleAsk = async () => {
    if (!query.trim()) return;
    setLoading(true);
    const result = await askQuestion(query);
    setResponse(result);
    setLoading(false);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Ask your question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleAsk()}
        style={{ width: "80%", padding: "0.5rem" }}
      />
      <button onClick={handleAsk} style={{ marginLeft: "1rem" }}>
        Ask
      </button>

      {loading && <p>⏳ Thinking...</p>}

      {response && (
        <div style={{ marginTop: "1.5rem" }}>
          <h3>✅ Answer:</h3>
          <p>{response.answer}</p>

          {response.sources?.length > 0 && (
            <>
              <h4>📚 Source Chunks:</h4>
              <ul>
                {response.sources.map((src, idx) => (
                  <li key={idx}>
                    <pre style={{ whiteSpace: "pre-wrap" }}>{src}</pre>
                  </li>
                ))}
              </ul>
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default ChatBox;