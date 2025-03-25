from typing import Any
from mcp.server.fastmcp import FastMCP
import subprocess
import sys
from log_config import _logger
import os
import glob
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

@mcp.tool()
async def search_and_show_img(img_name: str) -> str:
    dir = "/Users/chenpeng/Desktop/img"
    # Search for files starting with img_name
    pattern = os.path.join(dir, f"{img_name}*")
    matches = glob.glob(pattern)
    
    if matches:
        # Return first match as markdown image
        return f"![](file://{matches[0]})"
    else:
        return "没有找到匹配的图片"

if __name__ == "__main__":
    mcp.run(transport="stdio")

