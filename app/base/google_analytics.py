__all__ = ['GoogleAnalytics']

from random import randint


class GoogleAnalytics:
    def __init__(self, **kwargs):
        self.user_id = kwargs.pop('user_id', self._generator_id())
        self.ga_id = kwargs.pop('ga_id', self._generator_id())
        self.g_id = kwargs.pop('g_id', self._generator_id())
        self.tracks = {}

    # noinspection PyMethodMayBeStatic
    def _generator_id(self):
        return randint(1000000000, 9999999999)

    def add_track(self, gtag_ns: int, gtag_seq, value: int = 1):
        self.tracks.update({f'{gtag_ns}_{gtag_seq}': value})

    @property
    def prefix(self) -> str:
        return 'GA1.2'

    @property
    def cookies(self) -> dict:
        cookies = {
            '_ga': f'{self.prefix}.{self.ga_id}.{self.user_id}',
            '_gid': f'{self.prefix}.{self.g_id}.{self.user_id}',
        }
        for key, val in self.tracks.items():
            cookies.setdefault(f'_gat_gtag_UA_{key}', val)
        return cookies
