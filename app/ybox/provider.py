__all__ = ['YboxProvider']

from .api import YboxApi
from .user import YboxUser
from ..base import Provider


class YboxProvider(Provider):
    def _get_api(self):
        return YboxApi()

    @property
    def users(self):
        for user in YboxUser.all(self.api):
            yield user
