__all__ = ['BookDetail']

from abc import abstractmethod
from typing import List

from .api import Api
from .author import Author
from .base64 import Base64
from .book import Book
from .category_detail import CategoryDetail
from .tag import Tag


class BookDetail(Book):
    @staticmethod
    @abstractmethod
    def detail_of(api: 'Api', book: 'Book', **kwargs) -> 'BookDetail':
        pass

    @property
    def summary(self) -> 'Book':
        return self.data.get('summary')

    @property
    @abstractmethod
    def publisher(self) -> 'Author':
        pass

    @property
    @abstractmethod
    def category(self) -> 'CategoryDetail':
        pass

    @property
    def category_id(self):
        if self.category:
            return self.category.id

    @property
    @abstractmethod
    def tags(self) -> List['Tag']:
        pass

    @property
    def image_base64(self):
        return Base64.download_and_encode(self.image)

    @property
    @abstractmethod
    def images(self) -> List[str]:
        pass

    @property
    def images_base64(self):
        return list(map(Base64.download_and_encode, self.images))

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def attributes(self) -> dict:
        pass

    @property
    def __dict__(self):
        return {
            **super().__dict__,
            'publisher': self.publisher,
            'category': self.category,
            'image_base64': self.image_base64,
            'images': self.images,
            'images_base64': self.images_base64,
            'tags': self.tags,
            'summary_description': self.summary.description,
            'description': self.description,
            'attributes': self.attributes,
            'category_id': self.category_id or self.summary.category_id,
        }
