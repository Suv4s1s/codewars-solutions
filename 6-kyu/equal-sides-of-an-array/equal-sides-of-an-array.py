def find_even_index(arr):
    left_sum = 0
    right_sum = sum(arr)
    for i, val in enumerate(arr):
        right_sum -= val
        if left_sum == right_sum:
            return i
        left_sum += val
    return -1
​