import logging

_logger = logging.getLogger("mcp")
_logger.setLevel(logging.INFO)
_handler = logging.FileHandler("mcp.log")
_handler.setLevel(logging.INFO)
_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
