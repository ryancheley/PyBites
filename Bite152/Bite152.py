from functools import wraps

DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """

    def mydeco(func):
        @wraps(func)
        def wrapper(text):
            if start > end:
                return text
            else:
                return text.replace(text[max(start, 0):min(len(text), end)], DOT * (min(len(text), end) - max(start, 0)))
        return wrapper
    return mydeco


@strip_range(-1, 3)
def gen_output(text):
    return text

g = gen_output('Welcome to PyBites')
print(g)