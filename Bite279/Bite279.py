def is_armstrong(n: int) -> bool:
    input_int_list = [int(i) for i in str(n)]
    output_int_list = []
    for i in input_int_list:
        output_int_list.append(i ** len(input_int_list))

    return sum(output_int_list) == n