import utils.read_input as inp

lst = inp.to_origin_list()

all_ids = []


def highest_seatid(seats):
    high_id = -1
    for seat in seats:
        curr_id = gen_seatid(seat)
        high_id = max(high_id, curr_id)
        all_ids.append(curr_id)
    return high_id


def find_my_id():
    length = len(all_ids)
    all_ids.sort()
    for i in range(1, length):
        if all_ids[i] != all_ids[i - 1] + 1:
            return all_ids[i - 1] + 1


def gen_seatid(seat):
    low, high = 0, 127
    for i in range(7):
        mid = (low + high) // 2
        curr = seat[i]
        if curr == 'F':
            high = mid
        else:
            low = mid + 1

    c_low, c_hi = 0, 7
    for j in range(7, len(seat)):
        mid = (c_low + c_hi) // 2
        curr = seat[j]
        if curr == 'L':
            c_hi = mid
        else:
            c_low = mid + 1

    return 8 * low + c_low


print(f'Part 1: {highest_seatid(lst)}')

print(f'Part 2: {find_my_id()}')
