def array_diff(a, b):
    x = []
    for item in a:
        if item not in b:
            x.append(item)
    return x
​