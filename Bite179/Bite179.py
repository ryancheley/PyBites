import re

single_comment = '''
def hello_world():
    # A simple comment preceding a simple print statement
    print("Hello World")
'''

single_docstring = '''
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
'''

class_with_method = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')
'''

def strip_comments(code):
    result_list = []
    simple_search = re.compile(r'\#.*\n|\"{3}.*\"{3}\n')
    simple_comment = re.findall(simple_search, code)
    for i in code.split('\n'):
        for j in simple_comment:
            if j.strip() != i.strip():
                result_list.append(i)
    return '\n'.join(result_list)



s = strip_comments(class_with_method)
print(s)