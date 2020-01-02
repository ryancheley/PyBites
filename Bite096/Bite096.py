def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    file = open(file_, 'r')
    lines = 0
    num_words = 0
    characters = 0
    for f in file:
        lines += 1
        words = f.split()
        num_words += len(words)
        characters = characters + len(f)
    result = str(lines - 1)+'\t'+str(num_words)+'\t'+str(characters)+'\t'+file_
    return result

w = wc('Bite096.py')
print(w)

# if __name__ == '__main__':
#     # make it work from cli like original unix wc
#     import sys
#     print(wc(sys.argv[1]))