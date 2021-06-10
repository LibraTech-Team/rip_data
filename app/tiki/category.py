__all__ = ['TikiCategory']

from ..base import Category, Status


class TikiCategory(Category):
    BOOK_CATEGORY: int = 8322

    @staticmethod
    def all(api, **kwargs):
        def fetch(categories):
            if isinstance(categories, list):
                for category in categories:
                    yield from fetch(category)
                return
            category = categories
            yield category
            yield from fetch(TikiCategory.children_of(api, category))

        yield from fetch(TikiCategory.root(api))

    @staticmethod
    def root(api, **kwargs):
        return TikiCategory.children_of(api, TikiCategory({
            'query_value': TikiCategory.BOOK_CATEGORY,
        }))

    @staticmethod
    def children_of(api, category, **kwargs):
        res = api.get(f'products', params={
            'limit': 1,
            'category': category.id,
        })
        assert res.ok
        data = res.json()
        categories_filters = list(filter(lambda x: x.get('query_name') == 'category', data.get('filters')))
        if categories_filters:
            return list(map(TikiCategory, map(lambda x: {**x, 'parent_id': category.id}, categories_filters.pop().get('values'))))
        return []

    @property
    def id(self):
        return self.data.get('query_value')

    @property
    def parent_id(self):
        value = self.data.get('parent_id')
        if value == self.BOOK_CATEGORY:
            return None
        return value

    @property
    def name(self):
        return self.data.get('display_value')

    @property
    def status(self):
        return Status.Publish
