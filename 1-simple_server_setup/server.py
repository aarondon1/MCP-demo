from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

#load_dotenv(".env")

# Create a MCP server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0", # used for SSE transport (Local host)
    port=8050 # also used for SSE transport (set to any port)
)

# Add a tool to the MCP server, which in this case is the calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


# Run the server
if __name__ == "__main__":
    transport = "sse"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    elif transport == "streamable-http":
        print("Running server with Streamable HTTP transport")
        mcp.run(transport="streamable-http")
    else:
        raise ValueError(f"Unknown transport: {transport}")