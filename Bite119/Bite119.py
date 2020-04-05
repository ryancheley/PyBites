default_tree = """
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
"""

def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    result = []
    for row in range(rows):
        result.append(' '*(rows-row-1) + '*'*(2*(row+1) - 1))

    return '\n'.join(result)

g = generate_xmas_tree()
print(g.count('*'))
print(len(g.split('\n')))
print(g)
print(default_tree)