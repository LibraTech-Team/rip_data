__all__ = ['Rating']

from abc import abstractmethod
from typing import List

from .api import Api
from .book import Book
from .user import User


class Rating:
    @staticmethod
    @abstractmethod
    def all(api: 'Api', book: 'Book', **kwargs) -> List['Rating']:
        pass

    def __init__(self, data: dict = None):
        super().__init__()
        self.data = data

    def __str__(self):
        return self.comment

    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
    def user(self) -> 'User':
        pass

    @property
    @abstractmethod
    def comment(self) -> str:
        pass

    @property
    @abstractmethod
    def rating(self) -> int:
        pass

    @property
    def __dict__(self):
        return {
            'id': self.id,
            'user': self.user,
            'comment': self.comment,
            'starting': self.rating,
        }
