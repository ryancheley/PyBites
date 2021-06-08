STAR = '*'


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    for i in range(1, width+1, 1):
        if i % 2 == 1:
            padding = int((width - i) / 2)
            padding_char = ' '
            yield padding * padding_char + STAR * i + padding * padding_char

    for i in range(width-1, 0, -1):
        if i % 2 == 1:
            padding = int((width - i) / 2)
            padding_char = ' '
            yield padding * padding_char + STAR * i + padding * padding_char

gen = gen_rhombus(5)
for row in gen:
   print(row)

