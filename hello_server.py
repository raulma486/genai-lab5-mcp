from fastmcp import FastMCP

mcp = FastMCP("HelloMyServer")

@mcp.tool
def say_hello(name: str) -> str:
    """Retorna un saludo amistoso."""
    return f"Hola, {name}!"

if __name__ == "__main__":
    mcp.run()