message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output string"""
    the_split = message.split('\n')
    s = '|'
    the_join = s.join(the_split)
    print(the_join)



split_in_columns(message)