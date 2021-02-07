from _typeshed import NoneType
from typing import IO


class FileDidNotClose(Exception):
    def __init__(self):
        pass


class ErrorClearFile(Exception):
    def __init__(self):
        pass


class ErrorExitFile(Exception):
    def __init__(self):
        pass


def file_read(f):
    try:  # The file is read:
        f.read()
        return False  # Answer: The file is there, and it has been read.

    except:  # file not read:
        return None  # Answer: The file is present, but not readable.


def file_close(f: IO, error_code: str) -> NoneType:
    try:  # Closes the file:
        f.close()

    except:  # The file didn't close:
        print(f"error: {error_code}")
        raise FileDidNotClose  # Answer: The file won't close! We
        # throw in the program: "Exception".