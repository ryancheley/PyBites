from itertools import combinations

def find_number_pairs(numbers, N=10):
    result = []
    for i in combinations(numbers, 2):
        if i[0] + i[1] == N:
            result.append(i)
    return result


t = find_number_pairs([2, 3, 5, 4, 6])
print(t)