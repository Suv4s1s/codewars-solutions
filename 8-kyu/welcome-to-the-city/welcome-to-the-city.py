def say_hello(name, city, state):
    x=''
    for i in range(0,len(name)):
        x+=name[i]+ " "
    return f"Hello, {x.strip()}! Welcome to {city}, {state}!"