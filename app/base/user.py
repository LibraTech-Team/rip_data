__all__ = ['User']

from abc import abstractmethod
from typing import List

from .api import Api
from .avatar import Avatar


class User(Avatar):
    @staticmethod
    @abstractmethod
    def all(api: 'Api', **kwargs) -> List['User']:
        pass

    def __init__(self, data: dict = None):
        super().__init__()
        self.data = data

    def __str__(self):
        return self.name

    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def username(self) -> str:
        pass

    @property
    @abstractmethod
    def vendor_id(self) -> str:
        pass

    @property
    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'avatar': self.avatar,
            'avatar_base64': self.avatar_base64,
            'vendor_id': self.vendor_id,
        }
