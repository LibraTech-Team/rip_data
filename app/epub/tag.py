__all__ = ['EpubTag']

from ..base import Tag


class EpubTag(Tag):
    @property
    def id(self):
        return self.data.get('_id')

    @property
    def name(self):
        return self.data.get('title')
