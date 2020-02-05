def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    read_file = open(file_, 'r').read()
    lines = str(len(read_file.splitlines()))
    words = str(len(read_file.split()))
    characters = str(len(read_file))
    file_name = str(file_)
    result = lines+' '+words+' '+characters+' '+file_name
    return result




if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))