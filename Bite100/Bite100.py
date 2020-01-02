def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    f = open(filepath)
    l = f.readlines()
    return [s.rstrip('\n') for s in l][-n:]

t = tail('Bite100_content.txt', 3)
print(t)