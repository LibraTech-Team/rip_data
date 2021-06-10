__all__ = ['EpubUser']

from ..base import User, generator_id, generator_username


class EpubUser(User):
    @property
    def id(self):
        return generator_id(self.name)

    @property
    def name(self):
        return self.data.get('name')

    @property
    def username(self):
        return generator_username(self.name)

    @property
    def avatar(self):
        return None

    @property
    def vendor_id(self):
        return 'epub'
