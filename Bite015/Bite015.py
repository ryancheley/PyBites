names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    lines = []
    for i, (n, c) in enumerate(zip(names, countries), 1):
        lines.append(f'{i}. {n.ljust(10)} {c}'.ljust(0))
    print(lines)