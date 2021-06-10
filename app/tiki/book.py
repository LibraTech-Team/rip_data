__all__ = ['TikiBook']

from ..base import Book, Status


class TikiBook(Book):
    @staticmethod
    def all(api, category, **kwargs):
        def fetch(page, limit=10):
            try:
                res = api.get('products', params={
                    'page': page,
                    'limit': limit,
                    'category': category.id,
                })
                assert res.ok
                results = res.json().get('data')
            except Exception as e:
                print(e)
                return fetch(page, limit)
            for result in results:
                yield TikiBook({**result, 'category_id': category.id})

        p = 1
        while 1:
            print(f'---> Page: {p}')
            yield from fetch(p)
            p += 1

    @property
    def id(self):
        return self.data.get('id')

    @property
    def code(self):
        return self.data.get('sku')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def author(self):
        return [self.data.get('author_name')]

    @property
    def image(self):
        return self.data.get('thumbnail_url')

    @property
    def category_id(self):
        return self.data.get('category_id')

    @property
    def rating(self) -> float:
        return self.data.get('rating_average')

    @property
    def status(self) -> Status:
        return Status.Publish

    @property
    def price(self) -> int:
        return self.data.get('price')

    @property
    def description(self) -> int:
        return self.data.get('short_description')
