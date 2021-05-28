from typing import List  # not needed when we upgrade to 3.9

names = 'Bob Julian Tim Sara Eva Ana Jake Maria'.split()


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    times_to_loop = round(len(names) / cols)
    for item in range(times_to_loop):
        short_list = [f'| {i.ljust((10))}' for i in names if cols * (item) <= names.index(i) < cols * (item + 1)]
        print(''.join(short_list))

print_names_to_columns(names)