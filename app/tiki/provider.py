__all__ = ['TikiProvider']

from .api import TikiApi
from .book import TikiBook
from .book_detail import TikiBookDetail
from .category import TikiCategory
from ..base import Provider


class TikiProvider(Provider):
    def _get_api(self):
        return TikiApi()

    @property
    def categories(self):
        for category in TikiCategory.all(self.api):
            yield category

    @property
    def books(self):
        for category in self.categories:
            yield from self.books_in(category)

    def books_in(self, category):
        for book in TikiBook.all(self.api, category):
            yield book

    def detail_book_of(self, book):
        return TikiBookDetail.detail_of(self.api, book)
