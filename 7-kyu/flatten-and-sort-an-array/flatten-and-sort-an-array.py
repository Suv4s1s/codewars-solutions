def flatten_and_sort(array):
    x = []
    for nums in array:
        for elements in nums:
            x.append(elements)
    
    return sorted(x)