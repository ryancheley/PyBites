from functools import wraps


def make_html(element):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper():
            return f"<{element}>{func()}</{element}>"
        return func_wrapper
    return tags_decorator


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text

t = get_text()
print(t)