__all__ = ['EpubRating']

from .book import EpubBook
from .user import EpubUser
from ..base import Rating


class EpubRating(Rating):
    @staticmethod
    def all(api, book, **kwargs):
        def fetch():
            if isinstance(book, EpubBook):
                return api.get(f'rating/{book.slug}', params=kwargs).json().get('data', {}).get('recentReviews', [])

        return map(EpubRating, fetch())

    @property
    def id(self):
        return self.data.get('_id')

    @property
    def user(self):
        if self.data.get('name'):
            return EpubUser({
                'name': self.data.get('name'),
            })

    @property
    def comment(self):
        return self.data.get('comment')

    @property
    def rating(self):
        return int(self.data.get('stars'))
