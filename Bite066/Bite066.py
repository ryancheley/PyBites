from statistics import mean


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    return_list = []
    for idx, val in enumerate(sequence):
        result = sequence[0:idx+1]
        runninng_sum = 0
        for r in result:
            runninng_sum = r + runninng_sum
        return_list.append(float("{0:.2f}".format(runninng_sum / (idx+1))))
    return return_list


rm = running_mean([2, 6, 10, 8, 11, 10])
print(rm)