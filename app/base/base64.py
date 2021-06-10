__all__ = ['Base64']

from base64 import encodebytes

from requests import get

_cache_ = {}


class Base64:
    @staticmethod
    def download_and_encode(url) -> str:
        return
        if _cache_.get(url):
            return _cache_.get(url)
        try:
            res = get(url)
            assert res.ok
            raw = encodebytes(res.content).decode()
            _cache_.setdefault(url, raw)
            return raw
        except Exception as e:
            print(e)
