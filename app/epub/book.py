__all__ = ['EpubBook']

from .category import EpubCategory
from ..base import Book, Status


class EpubBook(Book):
    no_cover_url = '/static/assets/no-cover.png'

    @staticmethod
    def all(api, category, **kwargs):
        def fetch():
            if isinstance(category, EpubCategory):
                return api.get(f'categories/{category.slug}', params=kwargs).json().get('data', [])

        return map(EpubBook, fetch())

    @property
    def id(self):
        return self.data.get('_id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def author(self):
        return self.data.get('author')

    @property
    def image(self):
        if self.data.get('cover') == self.no_cover_url:
            return None
        return self.data.get('cover')

    @property
    def language(self):
        return self.data.get('language')

    @property
    def category_id(self):
        return self.data.get('category')

    @property
    def rating(self):
        return float(self.data.get('averageRating'))

    @property
    def status(self):
        return Status.Publish if self.data.get('enable') else Status.Disabled

    @property
    def price(self):
        return int(self.data.get('price'))

    @property
    def slug(self):
        return self.data.get('slug')
