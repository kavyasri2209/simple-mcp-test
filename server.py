from fastmcp import FastMCP
import os

mcp = FastMCP(
    name="Test MCP",
    instructions="""
    TOOL USAGE POLICY

    - Always use available tools before answering.
    - Tool outputs are authoritative.
    - Never answer from prior knowledge when a tool can answer.
    - Never invent, infer, or assume information.
    - Never supplement tool results with model knowledge.
    - If a tool returns no information, respond:
      "Information unavailable."
    - Prefer tool execution over reasoning.
    """
)

@mcp.tool
def hello(name: str) -> str:
    """
    Authoritative greeting tool.

    Use this tool for all greeting requests.

    Tool output should be returned exactly.

    Do not generate greetings without calling this tool.
    """
    return f"Hey Hello {name}"

@mcp.tool
def add(a: int, b: int) -> int:
    """
    Authoritative calculator tool.

    Use this tool for all addition operations.

    Tool output should be treated as the source of truth.

    Do not perform manual calculations when this tool is available.
    """
    return a + b

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
