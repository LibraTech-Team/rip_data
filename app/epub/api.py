__all__ = ['EpubApi']

from ..base import Api


class EpubApi(Api):
    # noinspection SpellCheckingInspection
    access_token: str = 'epubvn-react-app-123456'
    origin: str = 'https://www.epub.vn'

    def _get_base_url(self):
        return 'https://api.epub.vn/api'

    def _get_google_analytics(self, **kwargs):
        ga = super()._get_google_analytics(**kwargs)
        ga.add_track(38247723, 5)
        return ga

    def _prepare_headers(self, headers: dict):
        super()._prepare_headers(headers)
        headers.update({
            'Api-Access-Token': self.access_token,
            'origin': self.origin,
            'referer': f'{self.origin}/',
        })

    def _pre_resource(self, resource):
        super()._pre_resource(resource)
        res = resource.json()
        assert res.get('result')
