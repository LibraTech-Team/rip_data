__all__ = ['TryAgainLater', 'TooManyRequest']


class TryAgainLater(BaseException):
    wait_time: int = 10


class TooManyRequest(Exception, TryAgainLater):
    pass
