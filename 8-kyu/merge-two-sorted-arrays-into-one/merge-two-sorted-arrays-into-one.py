def merge_arrays(arr1, arr2):
    arr3 = set(arr1+arr2)
    return sorted(list(arr3))