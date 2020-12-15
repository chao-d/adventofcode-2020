import utils.read_input as inp

lst = inp.to_num_list()


def find_first_bad_number(window_size, nums):
    prev_n = set(nums[:window_size])
    for i in range(window_size, len(nums)):
        num = nums[i]
        if not two_sum_found(prev_n, num):
            return nums[i]
        prev_n.remove(nums[i - 25])
        prev_n.add(num)


def two_sum_found(numset, target):
    for k in numset:
        if (target - k) in numset:
            return True
    return False


#  0  1  2  3  4  5
# 35 20 15 25 47 40
# 0  1   2   3   4   5    6
# 0  35  55  70  95  142  182

def subarray_sum(nums, target):
    prefix_sum = [0]
    for i in range(len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i])

    for i in range(len(prefix_sum) - 1):
        for j in range(i + 1, len(prefix_sum)):
            if prefix_sum[j] - prefix_sum[i] == target:
                return nums[i] + nums[j - 1]


if __name__ == "__main__":
    bad_num = find_first_bad_number(25, lst)
    print(f'Part 1: {bad_num}')

    print(f'Part 2: {subarray_sum(lst, bad_num)}')
