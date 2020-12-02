import utils.read_input as inp

lst = inp.to_origin_list()


def count_valid(arr, is_valid):
    count = 0
    for ele in arr:
        if is_valid(ele):
            count += 1
    return count


def is_valid(ele):
    low, hi, char, string = parse_ele(ele)
    num_of_char = 0
    for s in string:
        if s == char:
            num_of_char += 1
    return low <= num_of_char <= hi


def is_valid_two(ele):
    pos0, pos1, char, string = parse_ele(ele)
    return (string[pos0 - 1] == char) ^ (string[pos1 - 1] == char) == 1


def parse_ele(ele):
    parts = ele.split(' ')
    part0 = parts[0].split('-')
    num0, num1 = int(part0[0]), int(part0[1])
    char = parts[1][:1]
    string = parts[2]
    return num0, num1, char, string


print(f'Part 1: {count_valid(lst, is_valid)}')


print(f'Part 2: {count_valid(lst, is_valid_two)}')
