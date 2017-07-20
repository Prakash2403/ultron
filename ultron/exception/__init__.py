# NotAbsolutePathException: This exception is raised when
# address of destination directory is not an absolute address.


class NotAbsolutePathException(Exception):
    pass

# UnknownException: This exception is raised when everything went smoothly,
# but your python interpreter decides to f**k you anyways.


class UnknownException(Exception):
    pass
