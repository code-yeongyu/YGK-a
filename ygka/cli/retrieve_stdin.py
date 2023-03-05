import sys

_stdin = None if sys.stdin.isatty() else sys.stdin.read()


def retrieve_stdin():
    return _stdin
