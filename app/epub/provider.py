__all__ = ['EpubProvider']

from .api import EpubApi
from .book import EpubBook
from .book_detail import EpubBookDetail
from .category import EpubCategory
from .rating import EpubRating
from ..base import Provider


class EpubProvider(Provider):
    def _get_api(self):
        return EpubApi()

    @property
    def categories(self):
        for category in EpubCategory.all(self.api):
            yield category

    @property
    def books(self):
        for category in self.categories:
            for book in EpubBook.all(self.api, category):
                yield book

    @property
    def detail_books(self):
        for book in self.books:
            yield EpubBookDetail.detail_of(self.api, book)

    @property
    def ratings(self):
        for book in self.books:
            for rating in EpubRating.all(self.api, book):
                yield rating

    @property
    def users(self):
        for rating in self.ratings:
            yield rating.user
