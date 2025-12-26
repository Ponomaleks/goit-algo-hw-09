import time
from statistics import mean


def find_coins_greedy(change, coins):
    change_dict = {}
    while change > 0:
        for coin in coins:
            if coin <= change:
                change_dict[coin] = change_dict.get(coin, 0) + 1
                change -= coin
                break
    return change_dict


def find_min_coins(change, coins):
    n = len(coins)
    dp = [float("inf")] * (change + 1)
    dp[0] = 0
    coin_used = [-1] * (change + 1)

    for i in range(1, change + 1):
        for j in range(n):
            if coins[j] <= i:
                if dp[i - coins[j]] + 1 < dp[i]:
                    dp[i] = dp[i - coins[j]] + 1
                    coin_used[i] = coins[j]

    if dp[change] == float("inf"):
        return {}

    change_dict = {}
    while change > 0:
        coin = coin_used[change]
        change_dict[coin] = change_dict.get(coin, 0) + 1
        change -= coin

    return change_dict


def benchmark(func, change_values, coins, runs=5):
    """
    Benchmark function execution time.

    :param func: function to benchmark
    :param change_values: list of change amounts
    :param coins: coin denominations
    :param runs: number of runs per test
    :return: dict {change: avg_time}
    """
    results = {}

    for change in change_values:
        times = []

        for _ in range(runs):
            start = time.perf_counter()
            func(change, coins)
            end = time.perf_counter()
            times.append(end - start)

        results[change] = mean(times)

    return results


if __name__ == "__main__":
    print("Testing coin change algorithms where greedy gives optimal result:\n")

    coins = [50, 25, 10, 5, 2, 1]
    change = 113
    result = find_coins_greedy(change, coins)
    print(result)  # Expected output: {50: 2, 10: 1, 2: 1, 1: 1}

    optimal_result = find_min_coins(change, coins)
    print(optimal_result)  # Expected output: {50: 2, 10: 1, 2: 1, 1: 1}

    print("\nTesting coin change algorithms where greedy fails:\n")
    coins = [4, 3, 1]
    change = 6
    result = find_coins_greedy(change, coins)
    print(result)  # Expected output: {4: 1, 1: 2}

    optimal_result = find_min_coins(change, coins)
    print(optimal_result)  # Expected output: {3: 2}

    # Benchmarking
    print("\nBenchmarking Greedy vs Dynamic Programming:\n")
    coins = [50, 25, 10, 5, 2, 1]
    change_values = [10, 50, 100, 500, 1_000, 5_000, 10_000]

    greedy_times = benchmark(find_coins_greedy, change_values, coins)
    dp_times = benchmark(find_min_coins, change_values, coins)

    print("Change | Greedy time (s) | DP time (s)")
    print("-" * 40)

    for change in change_values:
        print(
            f"{change:6} | "
            f"{greedy_times[change]:14.8f} | "
            f"{dp_times[change]:10.8f}"
        )
