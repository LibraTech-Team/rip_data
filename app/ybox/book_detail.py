__all__ = ['YboxBookDetail']

from .book import YboxBook
from ..base import BookDetail


class YboxBookDetail(BookDetail, YboxBook):
    pass
