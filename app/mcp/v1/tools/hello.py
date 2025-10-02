from fastmcp import FastMCP

hello_router = FastMCP(name="Hello MCP")


@hello_router.tool
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@hello_router.tool
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first number."""
    return a - b
