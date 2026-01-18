from os import getenv
from sys import argv


def main(args=argv):
    print(getenv("PYTHONPATH"), argv)
    print(EMPTY)

if __name__ == "__main__":
    main()