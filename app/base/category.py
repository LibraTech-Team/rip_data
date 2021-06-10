__all__ = ['Category']

from abc import abstractmethod
from typing import List, Optional

from .api import Api
from .status import Status


class Category:
    def __init__(self, data: dict = None):
        super().__init__()
        self.data = data

    @staticmethod
    @abstractmethod
    def root(api: 'Api', **kwargs) -> List['Category']:
        pass

    @staticmethod
    @abstractmethod
    def all(api: 'Api', **kwargs) -> List['Category']:
        pass

    @staticmethod
    @abstractmethod
    def children_of(api: 'Api', category: 'Category', **kwargs) -> List['Category']:
        pass

    def __str__(self):
        return self.name

    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
    def parent_id(self) -> Optional[str]:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
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
    def status(self) -> Status:
        pass

    @property
    def __dict__(self):
        return {
            'id': self.id,
            'parent_id': self.parent_id,
            'name': self.name,
            'image': self.image,
            'description': self.description,
            'status': self.status.value,
        }
