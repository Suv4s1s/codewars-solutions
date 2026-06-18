def product_fib(_prod):
    current_fib = 0
    next_fib = 1
    
    while current_fib * next_fib < _prod:
        old_current = current_fib
        current_fib = next_fib
        next_fib = old_current + next_fib
        
    is_exact_match = (current_fib * next_fib == _prod)
    
    return [current_fib, next_fib, is_exact_match]
​