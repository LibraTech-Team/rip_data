__all__ = ['Provider']

from abc import abstractmethod
from random import choice
from typing import List

from .api import Api
from .book import Book
from .book_detail import BookDetail
from .category import Category
from .rating import Rating
from .user import User


class Provider:
    @abstractmethod
    def _get_api(self) -> 'Api':
        pass

    def __init__(self):
        super().__init__()
        self.api = self._get_api()

    @property
    @abstractmethod
    def categories(self) -> List['Category']:
        pass

    @property
    @abstractmethod
    def books(self) -> List['Book']:
        pass

    @abstractmethod
    def books_in(self, category: 'Category') -> List['Book']:
        pass

    @property
    def books_random(self):
        print('Feting category ...')
        categories = list(map(self.books_in, self.categories))
        print(f'{len(categories)} Categories !')
        while 1:
            category = choice(categories)
            yield next(category)

    @property
    @abstractmethod
    def detail_books(self) -> List['BookDetail']:
        pass

    @abstractmethod
    def detail_book_of(self, book: 'Book') -> List['BookDetail']:
        pass

    @property
    @abstractmethod
    def ratings(self) -> List['Rating']:
        pass

    @property
    @abstractmethod
    def users(self) -> List['User']:
        pass
