__all__ = ['TikiCategoryDetail']

from .category import TikiCategory
from ..base import CategoryDetail


class TikiCategoryDetail(CategoryDetail, TikiCategory):
    pass
