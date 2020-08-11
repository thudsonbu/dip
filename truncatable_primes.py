# A left-truncatable prime is a prime number that contains no 0 digits and, when the first digit 
# is successively removed, the result is always prime.

# A right-truncatable prime is a prime number that contains no 0 digits and, when the last digit 
# is successively removed, the result is always prime.

# Create a function that takes an integer as an argument and:

# If the integer is only a left-truncatable prime, return "left".
# If the integer is only a right-truncatable prime, return "right".
# If the integer is both, return "both".
# Otherwise, return False.

def truncatable(n):
    numbers = [n for n in str(n)]
    if "0" in numbers:
        return False
    left = True
    for i in range(0,len(numbers)):
        if is_prime(int("".join(numbers[i::]))):
            continue
        else:
            left = False
    right = True
    for i in reversed(range(1,len(numbers))):
        if is_prime(int("".join(numbers[0:i]))):
            continue
        else:
            right = False
    if left and right:
        return "both"
    elif left:
        return "left"
    elif right: 
        return "right"
    else:
        return False


def is_prime(n):
    if n == 1:
        return False
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
    return prime

print(truncatable(79))