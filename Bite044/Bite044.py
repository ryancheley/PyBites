import secrets
import string

def gen_key(*, parts=4, chars_per_part=8):
    key = []
    alphabet = string.ascii_uppercase + string.digits
    for p in range(parts):
        part = ''.join(secrets.choice(alphabet) for i in range(chars_per_part))
        key.append(part)
    return '-'.join(key)


t = gen_key(parts=3, chars_per_part=4)
print(t)