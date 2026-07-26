def replace_exclamation(st):
    v = "AEIOUaeiou"
    a = "".join("!" if i in v else i for i in st )
    return a