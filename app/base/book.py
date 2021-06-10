__all__ = ['Book']

from abc import abstractmethod
from typing import List

from .api import Api
from .author import Author
from .category import Category
from .status import Status


class Book:
    def __init__(self, data: dict = None):
        super().__init__()
        self.data = data

    @staticmethod
    @abstractmethod
    def all(api: 'Api', category: 'Category', **kwargs) -> List['Book']:
        pass

    def __str__(self):
        return self.name

    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
    def code(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def author(self) -> List[Author]:
        pass

    @property
    @abstractmethod
    def image(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def language(self):
        pass

    @property
    @abstractmethod
    def category_id(self) -> str:
        pass

    @property
    @abstractmethod
    def rating(self) -> float:
        pass

    @property
    @abstractmethod
    def status(self) -> Status:
        pass

    @property
    @abstractmethod
    def price(self) -> int:
        pass

    @property
    def __dict__(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'author': self.author,
            'image': self.image,
            'description': self.description,
            'language': self.language,
            'category_id': self.category_id,
            'rating': self.rating,
            'status': self.status.value,
        }
