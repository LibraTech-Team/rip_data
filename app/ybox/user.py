__all__ = ['YboxUser']

from ..base import User

publisher_gql = '''
{
  _id
  username
  fullName
  avatar
}
'''

post_gql = '''
{
  count
  edges {
    publisher %(publisher_gql)s
  }
}
''' % {'publisher_gql': publisher_gql}

gql = '''
{
  AllPosts {
    NewestPosts(limit: %(limit)s, page: %(page)s) %(post_gql)s
    HighlightPosts(limit: %(limit)s, page: %(page)s) %(post_gql)s
    SelectivePosts(limit: %(limit)s, page: %(page)s) %(post_gql)s
  }
}
''' % {'post_gql': post_gql, 'limit': '%(limit)s', 'page': '%(page)s'}


class YboxUser(User):
    @staticmethod
    def all(api, **kwargs):
        def fetch(page, limit=10):
            try:
                res = api.get('', params={
                    'query': gql % {
                        'limit': limit,
                        'page': page,
                    }
                })
            except Exception as e:
                print(e)
                return fetch(page, limit)
            data = res.json().get('data', {})
            for results in data.values():
                for result in results.values():
                    for edge in result.get('edges', []):
                        publisher = edge.get('publisher', {})
                        if publisher:
                            yield YboxUser(publisher)

        p = 1
        while 1:
            print(f'---> Page: {p}')
            yield from fetch(p)
            p += 1

    @property
    def id(self):
        return self.data.get('_id')

    @property
    def name(self):
        return self.data.get('fullName')

    @property
    def username(self):
        return self.data.get('username')

    @property
    def avatar(self):
        url = self.data.get('avatar', '')
        if url:
            if url.startswith('//'):
                return 'https:' + url
        return url

    @property
    def vendor_id(self):
        return 'ybox'
