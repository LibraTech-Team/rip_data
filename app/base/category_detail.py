__all__ = ['CategoryDetail']

from abc import abstractmethod
from typing import List

from .api import Api
from .category import Category


class CategoryDetail(Category):
    @staticmethod
    @abstractmethod
    def detail_of(api: 'Api', book: 'Category', **kwargs) -> List['CategoryDetail']:
        pass

    @property
    @abstractmethod
    def parent(self) -> 'CategoryDetail':
        pass

    @property
    def parent_id(self) -> str:
        if self.parent:
            return self.parent.id

    @property
    def __dict__(self):
        return {
            **super().__dict__,
            'parent': self.parent,
        }
