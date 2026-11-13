"use client";

import React, { useState } from "react";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export default function HomePage() {
  const [goal, setGoal] = useState("");
  const [result, setResult] = useState<any | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleRun(e: React.FormEvent) {
    e.preventDefault();
    if (!goal.trim()) return;

    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/api/agent/run`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ goal }),
      });
      const data = await res.json();
      setResult(data);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main style={{ maxWidth: 800, margin: "48px auto", padding: "0 20px" }}>
      <h1 style={{ fontSize: 28, marginBottom: 8 }}>GENAI Summit — Agent Starter</h1>
      <p style={{ color: "#94a3b8", marginBottom: 24 }}>
        Give the agent a goal to plan, execute tools, and deliver an end-to-end result.
      </p>

      <form onSubmit={handleRun} style={{ display: "flex", gap: 12, marginBottom: 32 }}>
        <input
          type="text"
          value={goal}
          onChange={(e) => setGoal(e.target.value)}
          placeholder="Enter a high-level goal..."
          style={{
            flex: 1,
            padding: "12px 16px",
            borderRadius: 10,
            border: "1px solid #334155",
            background: "#0f172a",
            color: "#f8fafc",
            fontSize: 15,
          }}
        />
        <button
          type="submit"
          disabled={loading}
          style={{
            padding: "12px 24px",
            borderRadius: 10,
            border: "none",
            background: "#38bdf8",
            color: "#090d16",
            fontWeight: 600,
            cursor: "pointer",
          }}
        >
          {loading ? "Running..." : "Run Agent"}
        </button>
      </form>

      {result && (
        <div style={{ display: "grid", gap: 20 }}>
          <section style={{ background: "#0f172a", padding: 20, borderRadius: 12, border: "1px solid #1e293b" }}>
            <h2 style={{ fontSize: 16, marginTop: 0 }}>1. Execution Plan & Tool Steps</h2>
            <ul style={{ paddingLeft: 20, margin: 0, lineHeight: 1.7 }}>
              {result.steps.map((s: any) => (
                <li key={s.step}>
                  <strong>[{s.tool}]</strong> {s.action} → <span style={{ color: "#38bdf8" }}>{s.output}</span>
                </li>
              ))}
            </ul>
          </section>

          <section style={{ background: "#0f172a", padding: 20, borderRadius: 12, border: "1px solid #1e293b" }}>
            <h2 style={{ fontSize: 16, marginTop: 0 }}>2. Final Deliverable</h2>
            <pre style={{ whiteSpace: "pre-wrap", margin: 0, color: "#e2e8f0" }}>{result.deliverable}</pre>
          </section>
        </div>
      )}
    </main>
  );
}
