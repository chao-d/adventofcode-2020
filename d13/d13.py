import utils.read_input as inp

lst = inp.to_origin_list()

earliest = int(lst[0])
timestamps = [int(n) for n in lst[1:][0].split(',') if n != 'x']
timestamps.sort()


def lowest_greater(earliest, timestamps):
    smallest_no_smaller = float('inf')
    bus_id = 0
    for ts in timestamps:
        curr = 1
        while curr * ts < earliest:
            curr += 1
        if curr * ts == earliest:
            return 0, ts
        if curr * ts < smallest_no_smaller:
            smallest_no_smaller = curr * ts
            bus_id = ts
    return smallest_no_smaller, bus_id


if __name__ == "__main__":
    time_stamp, bus_id = lowest_greater(earliest, timestamps)
    if time_stamp == 0:
        print('Part 1: 0')
    else:
        print(f'Part 1: {(time_stamp - earliest) * bus_id}')
