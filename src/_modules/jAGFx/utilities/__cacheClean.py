# ==================================================================================
import shutil

# ==================================================================================
from pathlib import Path

# ==================================================================================
CLEARNER_TARGET = ["__pycache__", "eNuts.egg-info"]

# ==================================================================================
def PyCacheClean(directory=".") -> tuple[int, int]:
    """
    Removes all .pyc and .pyo files, as well as all CLEARNER_TARGETS directories
    from the given directory.

    Parameters
    ----------
    directory : str, optional
        The directory to clean. Defaults to ".".

    Returns
    -------
    None

    Notes
    -----
    This function is intended to be called from the command line, and
    will not return any value.
    """
    lPath = Path(directory)

    lFolderDeleted: int = 0
    lFileDeleted: int = 0

    for file in lPath.rglob("*.py[co]"):
        file.unlink()
        lFileDeleted += 1

    lTargets = CLEARNER_TARGET
    for pattern in lTargets:
        for cacheDir in lPath.rglob(pattern):
            if cacheDir.is_dir():
                shutil.rmtree(cacheDir)
                lFolderDeleted += 1

    return lFolderDeleted, lFileDeleted
