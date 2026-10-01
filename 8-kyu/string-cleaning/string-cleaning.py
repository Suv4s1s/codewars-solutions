def string_clean(s):
    a=''
    for i in s:
        if not i.isdigit():
            a+=i
    return ''.join(a)
​