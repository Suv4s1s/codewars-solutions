def tower_builder(n):
    x = []
    for i in range(n):
        x.append(("*" * (2 * i + 1)).center(2 * n - 1))
    return x
​