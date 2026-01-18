# ==================================================================================
import builtins

# ==================================================================================
from jAGFx.utilities import ProcessArguments, PyCacheClean, RebuildArguments

# ==================================================================================
# GLOBAL default value
# ==================================================================================
setattr(builtins, "EMPTY", "")
setattr(builtins, "EMPTYLIST", [])

# ==================================================================================
# GLOBAL function
# ==================================================================================
setattr(builtins, "PyCacheClean", PyCacheClean)
setattr(builtins, "ProcessArguments", ProcessArguments)
setattr(builtins, "RebuildArguments", RebuildArguments)