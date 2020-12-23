import utils.read_input as inp

lst = inp.to_origin_list()

earliest = int(lst[0])


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


def earliest_timestamp(timestamps, minutes):
    time, step = 0, 1
    for i in range(len(minutes)):
        t, m = timestamps[i], minutes[i]
        while (time + m) % t != 0:
            time += step
        step *= t
    return time


if __name__ == "__main__":
    time_stamp, bus_id = lowest_greater(earliest, sorted([int(n) for n in
                                        lst[1:][0].split(',') if n != 'x']))
    if time_stamp == 0:
        print('Part 1: 0')
    else:
        print(f'Part 1: {(time_stamp - earliest) * bus_id}')

    timestamps = []
    minutes = []
    for i, n in enumerate(lst[1:][0].split(',')):
        if n != 'x':
            timestamps.append(int(n))
            minutes.append(i)

    print(f'Part 2: {earliest_timestamp(timestamps, minutes)}')
