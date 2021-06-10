__all__ = ['EpubCategory']

from ..base import Category, Status


class EpubCategory(Category):
    @staticmethod
    def all(api, **kwargs):
        def fetch():
            return api.get('categories', params=kwargs).json().get('data', [])

        return map(EpubCategory, fetch())

    @property
    def id(self):
        return self.data.get('_id')

    @property
    def parent_id(self):
        return self.data.get('parent')

    @property
    def name(self):
        return self.data.get('title')

    @property
    def image(self):
        return None

    @property
    def description(self):
        return None

    @property
    def status(self):
        return Status.Publish if self.data.get('enable') else Status.Disabled

    @property
    def slug(self):
        return self.data.get('slug')
