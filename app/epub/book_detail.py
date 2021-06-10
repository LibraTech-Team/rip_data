__all__ = ['EpubBookDetail']

from abc import abstractmethod

from .book import EpubBook
from .category_detail import EpubCategoryDetail
from .tag import EpubTag
from ..base import BookDetail


class EpubBookDetail(BookDetail, EpubBook):
    @staticmethod
    @abstractmethod
    def detail_of(api, book, **kwargs):
        if isinstance(book, EpubBook):
            return EpubBookDetail(api.get(f'books/{book.slug}', params=kwargs).json().get('data', []))

    @property
    def category(self):
        return EpubCategoryDetail(self.data.get('category'))

    @property
    def tags(self):
        return list(map(EpubTag, self.data.get('tags', [])))

    @property
    def description(self):
        return self.data.get('description')
