# ==================================================================================
from sys import argv
from typing import Any

# ==================================================================================
# GLOBAL default value
# ==================================================================================
EMPTY: str 
EMPTYLIST: list = []

# ==================================================================================
# GLOBAL function
# ==================================================================================
def PyCacheClean(directory=".") -> tuple[int, int]: ...
def ProcessArguments(arguments: list[str] = argv) -> tuple[list[str], dict[str, Any]]: ...
def RebuildArguments(app: str = argv[0], *args, **kwargs) -> list[str]: ...