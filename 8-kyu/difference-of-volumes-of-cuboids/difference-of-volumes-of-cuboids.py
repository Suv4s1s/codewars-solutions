def find_difference(a, b):
    aa=1
    bb=1
    for i in a:
        aa*=i
    for j in b:
        bb*=j
    return abs(aa-bb)