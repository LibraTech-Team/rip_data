__all__ = ['Avatar']

from abc import abstractmethod

from .base64 import Base64


class Avatar:
    @property
    @abstractmethod
    def avatar(self) -> str:
        pass

    @property
    def avatar_base64(self) -> str:
        return Base64.download_and_encode(self.avatar)
