import utils.read_input as inp

lst = inp.to_origin_list()


def count_valid(arr):
    count = 0
    for ele in arr:
        if is_valid(ele):
            count += 1
    return count


def is_valid(ele):
    parts = ele.split(' ')
    part0 = parts[0].split('-')
    low, hi = int(part0[0]), int(part0[1])
    char = parts[1][:1]
    string = parts[2]
    num_of_char = 0
    for s in string:
        if s == char:
            num_of_char += 1
    if low <= num_of_char <= hi:
        return True
    return False


print(f'Part 1: {count_valid(lst)}')
