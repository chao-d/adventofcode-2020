import utils.read_input as inp

lst = inp.to_origin_list()


def count_trees(nums, right, down):
    hori_len = len(nums[0])
    x, y = 0, 0
    count = 0
    while y < len(nums):
        if nums[y][x] == '#':
            count += 1
        x, y = (x + right) % hori_len, y + down
    return count


print(f'Part 1: {count_trees(lst, 3, 1)}')


def product_of_trees(nums, slopes):
    count = 1
    for slope in slopes:
        count *= count_trees(lst, slope[0], slope[1])
    return count


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(f'Part 2: {product_of_trees(lst, slopes)}')
