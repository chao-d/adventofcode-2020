import os

curr_basename = os.path.basename(os.getcwd())
input_name = curr_basename + "in"


def to_num_list():
    lst = []
    with open(input_name, 'r') as f:
        for line in f:
            lst.append(int(line.strip()))
    return lst


def to_origin_list():
    lst = []
    with open(input_name, 'r') as f:
        for line in f:
            lst.append(line.strip())
    return lst
