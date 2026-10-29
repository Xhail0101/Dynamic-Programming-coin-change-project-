def coin_change(coins, amount):

    dp = [float('inf')] * (amount + 1)
    parent = [-1] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):

        for coin in coins:

            if coin <= i:

                if dp[i - coin] + 1 < dp[i]:

                    dp[i] = dp[i - coin] + 1
                    parent[i] = coin


    if dp[amount] == float('inf'):
        return -1, [], dp


    used_coins = []
    current = amount

    while current > 0:

        coin = parent[current]
        used_coins.append(coin)
        current -= coin

    return dp[amount], used_coins, dp



coins = [1, 3, 4]
amount = 6

minimum, selected, dp_table = coin_change(coins, amount)

print("Coins:", coins)
print("Amount:", amount)
print("Minimum Coins:", minimum)
print("Selected Coins:", selected)
print("DP Table:", dp_table)
