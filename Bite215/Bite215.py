from string import ascii_uppercase, digits
import random
import re

ALPHABET = ascii_uppercase + digits

def _create_license():
    return 'PB-' + '-'.join(
        [''.join(random.sample(ALPHABET, 8))
         for _ in range(4)]
    )

def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    match = re.search('^PB(\-\w{8}){4}$', key)
    # match = re.search('^PB', key).span()
    if match:
        return True
    else:
        return False



pool = [_create_license() for _ in range(5)]
longer_key = pool[2] + 'A'

key = 'AB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4'

print(pool[2])
print(longer_key)

t = validate_license(longer_key)

print(t)