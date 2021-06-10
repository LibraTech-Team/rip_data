__all__ = ['TikiBookDetail']

from .author import TikiAuthor
from .book import TikiBook
from ..base import BookDetail


class TikiBookDetail(BookDetail, TikiBook):
    @staticmethod
    def detail_of(api, book, **kwargs):
        res = api.get(f'products/{book.id}', params={
            'platform': 'web',
            'include': 'tag,images',
        })
        assert res.ok
        data = res.json()
        return TikiBookDetail({**data, 'summary': book})

    @property
    def author(self):
        return list(map(TikiAuthor, self.data.get('authors', [])))

    @property
    def publisher(self):
        return [self.data.get('publisher')]

    @property
    def category(self):
        pass

    @property
    def tags(self):
        pass

    @property
    def images(self):
        return list(map(lambda x: x.get('large_url'), self.data.get('images')))

    @property
    def description(self):
        return self.data.get('description')

    @property
    def specifications(self):
        return self.data.get('specifications')

    @property
    def attributes(self):
        attributes = {}
        for specification in self.specifications:
            attrs = specification.get('attributes')
            if attrs:
                for attr in attrs:
                    attributes.setdefault(attr.get('name'), attr.get('value'))
        return attributes
