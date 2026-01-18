# ==================================================================================
import sys
from typing import Any


# ==================================================================================
def RebuildArguments(app: str = sys.argv[0], *args, **kwargs):
    """
    Rebuilds the sys.argv list into a new list with the given positional and keyword arguments.

    Args:
        app (str): The application name to prepend to the result.
        *args: Positional arguments to include in the result.
        **kwargs: Keyword arguments to include in the result.

    Returns:
        list: A new list containing the application name and the given positional and keyword arguments.
    """
    lResult = list(args)
    for key, val in kwargs.items():
        lResult.extend([f"--{key}", str(val)])

    lResult.insert(0, app)
    return lResult

# ==================================================================================
def ProcessArguments(arguments: list[str] = sys.argv) -> tuple[list[str], dict[str, Any]]:
    """
    Processes the given command line arguments into a tuple of positional and keyword arguments.

    Args:
        arguments (list[str], optional): The list of command line arguments to process. Defaults to sys.argv.

    Returns:
        tuple[list[str], dict[str, Any]]: A tuple containing the positional arguments and keyword arguments.
    """
    lArguments = arguments[1:]
    lArgs = []
    lKwargs = {}
    lIndex = 0

    while lIndex < len(lArguments):
        lArg = lArguments[lIndex]
        if lArg.startswith(('--', '-')):
            # It's a kwarg
            lKey = lArg.lstrip('-')
            lValues = []
            lIndex += 1
            while lIndex < len(lArguments) and not lArguments[lIndex].startswith(('--', '-')):
                lValues.append(lArguments[lIndex])
                lIndex += 1

            if not lValues:
                lKwargs[lKey] = True

            elif len(lValues) == 1:
                lKwargs[lKey] = lValues[0]

            else:
                lKwargs[lKey] = lValues

        else:
            # It's an arg, but only if no kwargs seen yet
            if lKwargs: break

            lArgs.append(lArg)
            lIndex += 1

    return lArgs, lKwargs
