import re
def strip_comments(code):
    # see Bite description
    regex = re.compile(r'    (\#( .*)\n)|\s*\"{3}.*\n')
    regex_find = re.findall(regex, code)
    return regex_find
    # return code.replace(re.search(regex, code).group(), '')

code = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')
'''

s = strip_comments(code)
print(s)