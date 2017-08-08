class NotAbsolutePathException(Exception):
    """
    This exception is raised when address of destination directory
    is not an absolute address.
    """
    pass


class UnknownException(Exception):
    """
    This exception is raised when everything went smoothly,
    but your interpreter or OS decides to screw you anyways,
    """

    pass


class NoSecretFileException(Exception):
    """
    This exception is raised when file containing secret key for a
    service(like twitter) doesn't exists.
    """
    pass


class InvalidAPIException(Exception):
    """
    This exception is raised when API key(s) used for authentication
    is invalid.
    """
    pass
