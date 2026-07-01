def alphabet_position(text):
    result = []
    
    for char in text:
        if char.isalpha():
            lowercase_char = char.lower()
            position = ord(lowercase_char) - 96
            result.append(str(position))
            
    return " ".join(result)
​