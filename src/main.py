from os import getenv
from sys import argv


def _programs(clean: bool = False, *args, **kwargs) -> None:
    print(getenv("PYTHONPATH"))
    print(argv)
    print(F"Printing Empty {EMPTY}" )

    if clean:
        lFolders, lFiles = PyCacheClean()
        print(f"Deleted {lFolders} folders and {lFiles} files")


def main(args=argv):
    lArgs, lKWArgs = ProcessArguments(args)
    _programs(*lArgs, **lKWArgs)    

if __name__ == "__main__":
    main()