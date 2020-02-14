import re

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""


    return re.search(r'^(.{1,20})(?<!\s)(?!\w)', text).span()[1]

t = text_to_columns('My house is small but cosy.')
print(t)

