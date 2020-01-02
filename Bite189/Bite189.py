IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


list = ['barry', 'tim', 'amber', 'ana', 'cindy', 'sara', 'molly', 'henry']
# list = ['12', 'bas']

def filter_names(names):
    result = []
    list = names
    for l in list:
        if l[0:1] != IGNORE_CHAR and l.isalpha():
            if l[0:1] == QUIT_CHAR:
                break
            else:
                result.append(l)
    return result[:MAX_NAMES]

f = filter_names(list)
print(f)
