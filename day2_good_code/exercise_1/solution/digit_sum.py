def digit_sum(num):
    # a recursive function 
    """Calculate the digit sum of a natural number"""
    if num < 0:
        raise ValueError("Input must be a natural number")
    elif num == 0:
        return 0
    else:
        return num % 10 + digit_sum(num // 10)