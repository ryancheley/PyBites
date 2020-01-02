import textwrap

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

INDENTS = 4


def print_hanging_indents(poem):
    result = textwrap.dedent(poem).split('\n')
    for previous, current in zip(result, result[1:]):
        if not previous:
            print(current)
        else:
            if current:
                print(' '*INDENTS+current)

t = print_hanging_indents(shakespeare_unformatted)