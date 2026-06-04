from fastmcp import FastMCP

mcp = FastMCP("Test MCP")

@mcp.tool
def hello(name: str) -> str:
    """
    Use this tool whenever the user asks for a greeting.
    Do not generate greetings from model knowledge when this tool is available.
    """
    return f"Hey Hello {name}"

@mcp.tool
def add(a: int, b: int) -> int:
    """
    Authoritative calculator tool.
    Use this tool for addition operations.
    Always call this tool instead of calculating manually.
    """
    return a + b

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000
    )
