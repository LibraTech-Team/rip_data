__all__ = ['TikiApi']

from ..base import Api


class TikiApi(Api):
    origin: str = 'https://tiki.vn'

    def _get_base_url(self):
        return 'https://tiki.vn/api/v2'

    def _prepare_headers(self, headers: dict):
        super()._prepare_headers(headers)
        headers.update({
            'origin': self.origin,
            'referer': f'{self.origin}/',
        })

    def _pre_resource(self, resource):
        super()._pre_resource(resource)
        res = resource.json()
        assert not res.get('errors')
