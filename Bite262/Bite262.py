test_sequence = 'AAAAAAAATTTTTTGGGGCC'

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    sequence = sequence.upper()
    count_A = sequence.count('A')
    count_C = sequence.count('C')
    count_G = sequence.count('G')
    count_T = sequence.count('T')

    result = ((count_C + count_G) / (count_C + count_G + count_A + count_T)) * 100

    return round(result, 2)

d = calculate_gc_content(test_sequence)
print(d)