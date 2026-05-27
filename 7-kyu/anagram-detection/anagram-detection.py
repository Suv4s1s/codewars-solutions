# write the function is_anagram
def is_anagram(test, original):
    return True if sorted([i for i in test.lower()]) == sorted([j for j in original.lower()]) else False