def fibonacci_nth(n):
    # if it is index 0 return 0 (we dont have two numbers to add for algorithm)
    if n == 0:
        return 0
    # otherwise use fib algorithm
    else:
        # two numbers used to sum for next
        num_1 = 0
        num_2 = 1
        # iterate though n-1 times (starts at zero)
        for i in range(0, n-1):
            # store second numbers value for setting to num1
            store = num_2
            # set num2 to sum of previous (next num in sequence)
            num_2 = num_1 + num_2
            # set num1 to old num 2
            num_1 = store
        # return most recently calculated num2
        return num_2


print(fibonacci_nth(5))


def fibonacci_nth_top_down(n):
    memo = {0: 0, 1: 1, 2: 1}

    return fib_recursive(n+1, memo)


def fib_recursive(n, memo):
    sum_1 = 0
    sum_2 = 0

    if n >= 1:
        if n-1 in memo:
            sum_1 = memo[sum_1]
        else:
            sum_1 = fib_recursive(n-1, memo)
            memo[n-1] = sum_1

    if n >= 2:
        if n-2 in memo:
            sum_2 = memo[n-2]
        else:
            sum_2 = fib_recursive(n-2, memo)
            memo[n-2] = sum_2

    return sum_1 + sum_2


print(fibonacci_nth_top_down(5))
