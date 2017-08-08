class InvalidUserException(Exception):
    """
    This exception is raised when screen name
    entered by user doesn't exists.
    """
    pass


class MaximumLimitCrossedException(Exception):
    """
    Raised when maximum limit for making request is reached.
    Request count will reset after 15 minutes.
    """
    pass
