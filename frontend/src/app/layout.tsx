import React from "react";

export const metadata = {
  title: "GENAI Summit — Proactive Agent Mission Control",
  description: "Next.js + FastAPI Proactive End-to-End Agent Starter",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ margin: 0, backgroundColor: "#090d16", color: "#f1f5f9", fontFamily: "system-ui, sans-serif" }}>
        {children}
      </body>
    </html>
  );
}
