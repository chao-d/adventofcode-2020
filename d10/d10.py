import utils.read_input as inp

lst = inp.to_num_list()


lst.sort()


def count_diff(lst):
    res = {1: 0, 2: 0, 3: 1}
    curr = 0
    for num in lst:
        curr_diff = num - curr
        res[curr_diff] += 1
        curr = num
    return res


def product_of_1_3_diff(diffs):
    return diffs[1] * diffs[3]


def num_of_comb(lst):
    dp = [0] * (len(lst) + 1)
    dp[0] = dp[1] = dp[2] = dp[3] = 1
    if lst[1] == 2:
        dp[2] = 2
    if lst[2] == 3:
        dp[3] = 4

    for i in range(3, len(lst)):
        if lst[i - 1] == lst[i] - 3:
            dp[i + 1] += dp[i]
        elif lst[i - 1] == lst[i] - 2:
            dp[i + 1] += dp[i]
            if i - 2 >= 0 and lst[i - 2] == lst[i] - 3:
                dp[i + 1] += dp[i - 1]
        else:
            dp[i + 1] += dp[i]
            if i - 2 >= 0:
                if lst[i - 2] == lst[i] - 3 or lst[i - 2] == lst[i] - 2:
                    dp[i + 1] += dp[i - 1]
                if lst[i - 2] == lst[i] - 2 and (i - 3 >= 0 and
                                                 lst[i - 3] == lst[i] - 3):
                    dp[i + 1] += dp[i - 2]

    return dp[len(dp) - 1]


if __name__ == "__main__":
    print(f'Part 1: {product_of_1_3_diff(count_diff(lst))}')

    print(f'Part 2: {num_of_comb(lst)}')
