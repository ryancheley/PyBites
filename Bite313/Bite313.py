import re
from urllib.parse import urlparse


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        self.name = name
        if not re.search(r'.*\.[a-z]{2,3}$', name):
            raise DomainException

    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively

    @classmethod
    def parse_url(cls, name):
        result = cls(urlparse(name).netloc)
        return result

    @classmethod
    def parse_email(cls, name):
        result = cls(name[name.index("@")+1 : ])
        return result

    def __str__(self):
        return self.name
