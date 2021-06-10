__all__ = ['Author']

from abc import abstractmethod


class Author:
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
    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
        }
