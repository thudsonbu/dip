# Hi, here's your problem today. This problem was recently asked by Uber:

# Given a list of possible coins in cents, and an amount (in cents) n, return the minimum number of coins needed to 
# create the amount n. If it is not possible to create the amount using the given coin denomination, return None.

# Here's an example and some starter code:

def make_change(coins, n):
    coins, change_used = sorted(coins, reverse=True), 0
    while coins:
        current_coin = coins.pop(0)
        while n >= current_coin:
            n -= current_coin
            change_used += 1
    if n > 0:
        return None
    else:
        return change_used

def make_change2(coins, n):
    min_coins = [None] * (n + 1)
    min_coins[0] = [0]

    for i in range(n):
        for c in coins:
            if i + c <= n:
                if min_coins[i+c] is not None:
                    min_coins[i+c] = min(min_coins[i] + 1, min_coins[i+c])
                else:
                    min_coins[i+c] = min_coins[i] + 1


print(make_change([1, 5, 10, 25], 36))
print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)
