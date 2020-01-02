from string import ascii_lowercase

text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""


def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []
    the_split = text.split('\n')
    for line in range(len(the_split)):
        the_line = the_split[line].strip()
        if len(the_line)>0:
            if the_line[0].islower():
                mod_the_line = the_line.split(' ')[-1]
                mod_the_line = mod_the_line.strip('.').strip('!')
                the_line = mod_the_line
                results.append(the_line)

    print(results)

slice_and_dice()