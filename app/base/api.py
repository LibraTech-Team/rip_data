__all__ = ['Api']

from abc import abstractmethod
from time import sleep

from requests import Session, Response

from .exceptions import TooManyRequest, TryAgainLater
from .google_analytics import GoogleAnalytics


class Api(Session):
    @abstractmethod
    def _get_base_url(self, **kwargs) -> str:
        pass

    def _get_google_analytics(self, **kwargs) -> 'GoogleAnalytics':
        return GoogleAnalytics()

    def __init__(self, **kwargs):
        super().__init__()
        self.base_url = self._get_base_url(**kwargs)
        self.google_analytics = self._get_google_analytics(**kwargs)

    def _generator_cookie(self, google_analytics=True) -> dict:
        items = {}

        if google_analytics:
            items.update(self.google_analytics.cookies)

        return items

    def _prepare_headers(self, headers: dict):
        # noinspection SpellCheckingInspection
        headers.update({
            'Accept': 'application/json',
            'Accept-Language': 'vi,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Cookie': '; '.join([f'{key}={val}' for key, val in self._generator_cookie().items()]),
            'DNT': '1',
            'Pragma': 'no-cache',
            'Sec-CH-UA': '"Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'Sec-CH-UA-Mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'WithCredentials': 'true',
        })

    # noinspection PyMethodMayBeStatic
    def _pre_request(self, request: dict):
        if not request.get('method') or not request.get('url'):
            raise ValueError

    # noinspection PyMethodMayBeStatic
    def _pre_resource(self, resource: 'Response'):
        if resource.status_code == 429 and resource.reason == 'Too Many Requests':
            raise TooManyRequest
        assert resource.ok

    def request(self, method: str, url: str, **kwargs) -> 'Response':
        try:
            return self._request(method, url, **kwargs)
        except TryAgainLater as e:
            print(e.__class__)
            sleep(e.wait_time)
            return self.request(method, url, **kwargs)

    def _request(self, method: str, url: str, **kwargs) -> 'Response':
        url = f'{self.base_url}/{url}'

        headers = kwargs.get('headers', {})
        self._prepare_headers(headers)

        kwargs.update({
            'method': method,
            'url': url,
            'headers': headers,
        })

        while 1:
            try:
                self._pre_request(kwargs)
                res = super().request(**kwargs)
                self._pre_resource(res)
                return res
            except Exception as e:
                print(e)
                continue
