from hashlib import md5
from re import sub
from unicodedata import normalize

from .json import JSON


def write_json(path, data):
    with open(path, 'w+') as f:
        f.write(JSON.dumps(data))
        f.close()


def generator_id(name: str) -> str:
    return md5(name.encode()).hexdigest()


def generator_variant(name: str) -> str:
    raw = sub(r'[^0-9]', '', generator_id(name))
    length = int(raw[-1]) % 5
    return raw[:length]


def simple_unicode(raw: str) -> str:
    return normalize('NFKD', raw).encode('ASCII', 'ignore').decode()


def generator_username(name: str) -> str:
    username = simple_unicode(name).lower()
    username = sub(r'[^a-z0-9]', '.', username)

    variant = generator_variant(username)
    if variant:
        username += f'.{variant}'
    return username
