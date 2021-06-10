__all__ = ['EpubCategoryDetail']

from .category import EpubCategory
from ..base import CategoryDetail


class EpubCategoryDetail(CategoryDetail, EpubCategory):
    @property
    def parent(self):
        if self.data.get('parent'):
            return EpubCategoryDetail(self.data.get('parent'))
