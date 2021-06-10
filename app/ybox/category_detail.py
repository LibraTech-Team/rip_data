__all__ = ['YboxCategoryDetail']

from .category import YboxCategory
from ..base import CategoryDetail


class YboxCategoryDetail(CategoryDetail, YboxCategory):
    pass
