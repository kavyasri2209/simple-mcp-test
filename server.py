from fastmcp import FastMCP

mcp = FastMCP(
    name="Test MCP",
    instructions="""
    Always use the provided tools when relevant.
    Do not answer from prior knowledge if a tool can answer.
    If no tool can answer, say the information is unavailable.
    """
)

@mcp.tool
def hello(name: str) -> str:
    """
    Use this tool whenever the user asks for a greeting.
    """
    return f"Hey Hello {name}"

@mcp.tool
def add(a: int, b: int) -> int:
    """
    Authoritative calculator tool.
    Always use this tool for addition.
    """
    return a + b

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000
    )
