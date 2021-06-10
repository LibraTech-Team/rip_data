__all__ = ['JSON']

from json import JSONEncoder, dumps


class JSON:
    class Encoder(JSONEncoder):
        def default(self, o):
            return getattr(o, '__dict__')

    @staticmethod
    def dumps(*args, **kwargs):
        kwargs.setdefault('ensure_ascii', False)
        kwargs.setdefault('indent', 2)
        kwargs.setdefault('cls', JSON.Encoder)
        return dumps(*args, **kwargs)
