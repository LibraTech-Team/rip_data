__all__ = ['YboxApi']

from ..base import Api


class YboxApi(Api):
    origin: str = 'https://ybox.vn'

    def _get_base_url(self):
        return 'https://api.ybox.vn/graphql'

    def _generator_cookie(self, **kwargs):
        kwargs.setdefault('google_analytics', False)
        return super()._generator_cookie(**kwargs)

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
