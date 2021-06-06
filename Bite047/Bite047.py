import string

# has at least 1 digit [0-9]
# has at least two lowercase chars [a-z]
# has at least one uppercase char [A-Z]
# has at least one punctuation char (use: PUNCTUATION_CHARS)
# Has not been used before (use: used_passwords)

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if not 6 <= len(password) <= 12:
        return False
    if sum([char.islower() for char in password]) < 2:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char for char in password if char in PUNCTUATION_CHARS):
        return False
    if password in list(used_passwords):
        return False
    used_passwords.add(password)
    return True


print(validate_password('PassWord@1'))
print(validate_password('PyBit$s9'))
