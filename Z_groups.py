def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_multiplicative_group(n):
    if n <= 0:
        return "n must be a positive integer"

    group = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            group.append(i)

    return group

def populate_circular_subgroups(group):
    subgroups = []
    n = group[-1] + 1
    for unit in group:
        cycle = [unit]
        cur_product = unit
        while cur_product != 1:
            cur_product *= unit
            cur_product %= n
            cycle.append(cur_product)
        subgroups.append(cycle)
    return subgroups


if __name__ == "__main__":
    n = 25
    Zn_star = generate_multiplicative_group(n)
    print(Zn_star)
    print(populate_circular_subgroups(Zn_star))