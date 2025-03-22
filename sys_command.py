from typing import Any
from mcp.server.fastmcp import FastMCP
import subprocess
import sys
from log_config import _logger

mcp = FastMCP("System Command")

# 打开网易云
@mcp.tool()
async def open_wangyiyun(music_name: str) -> str:
    # subprocess.run(["open", "-a", "Visual Studio Code"])
    x = subprocess.run(["open", "-a", "NeteaseMusic"])
    _logger.info(x)
    return f"OK"

# 使用系统语音播放语音
@mcp.tool()
async def say_voice(text: str) -> str:
    subprocess.run(["say", text])
    _logger.info(f"say {text}")
    return f"OK"


if __name__ == "__main__":
    mcp.run(transport="stdio")

