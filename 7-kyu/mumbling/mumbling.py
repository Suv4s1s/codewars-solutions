def accum(st):
    y = []
    for index,item in enumerate(st):
        y.append((item*(index+1)).strip().capitalize())
​
    a = "-".join(y)
    return (str(a))