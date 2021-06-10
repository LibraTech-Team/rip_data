__all__ = ['Tag']

from abc import abstractmethod
from typing import List

from .api import Api


class Tag:
    @staticmethod
    @abstractmethod
    def all(api: 'Api', **kwargs) -> List['Tag']:
        pass

    def __init__(self, data: dict = None):
        super().__init__()
        self.data = data

    def __str__(self):
        return self.name

    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
        }
