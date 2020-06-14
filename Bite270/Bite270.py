from collections import Counter


def freq_digit(num: int) -> int:
    digit_list = []
    for i in str(num):
        digit_list.append(i)

    digit_counter = Counter(digit_list)
    most_common_digit = digit_counter.most_common(1)[0][0]
    return int(most_common_digit)