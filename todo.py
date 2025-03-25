from typing import Any
from mcp.server.fastmcp import FastMCP
import subprocess
import sys
from log_config import _logger

mcp = FastMCP("Todo")


@mcp.tool()
async def get_todo_in_markdown() -> str:
    with open("todo.txt", "r") as f:
        return f.read()

@mcp.tool()
async def set_todo_in_markdown(text: str) -> str:
    with open("todo.txt", "w") as f:
        f.write(text)
    _logger.info(f"set todo {text}")
    return f"OK"


if __name__ == "__main__":
    mcp.run(transport="stdio")

