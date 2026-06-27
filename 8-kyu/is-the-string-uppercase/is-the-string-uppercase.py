def is_uppercase(inp):
    y = inp.replace(" ","")
    flag = True
​
        
    for i in y:
        if i.islower():
            flag=False
    return flag