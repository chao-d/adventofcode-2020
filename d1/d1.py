import utils.read_input as inp

lst = inp.to_num_list()

target = 2020


def two_sum(nums, tar):
    seen_nums = set()
    for num in nums:
        if tar - num in seen_nums:
            return num * (tar - num)
        else:
            seen_nums.add(num)
    return -1


print(f"part 1: {two_sum(lst, target)}")


def three_sum(nums, tar):
    for i in range(len(nums) - 2):
        curr = nums[i]
        twosum = two_sum(nums[i + 1:], target - curr)
        if twosum != -1:
            return curr * twosum


print(f"part 2: {three_sum(lst, target)}")
