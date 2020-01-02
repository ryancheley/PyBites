test = [
   ('string  ', 0),
   ('  string', 2),
   ('    string', 4),
   ('            string', 12),
   ('\t\tstring', 0),
   ('  str  ing', 2),
   ('  str  ', 2),
]

def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return len(text) - len(text.lstrip(' '))

i = 1
t = count_indents(test[i][0])
print(str(t) + ' versus ' + str(test[i][1]))