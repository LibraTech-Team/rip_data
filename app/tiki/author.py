__all__ = ['TikiAuthor']

from ..base import Author


class TikiAuthor(Author):
    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')
