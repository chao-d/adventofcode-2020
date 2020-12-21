import utils.read_input as inp

lst = inp.to_origin_list()

ops = [(ele[0], int(ele[1:])) for ele in lst]


def dest_loc(ops):
    x, y = 0, 0
    face = 'E'
    for op in ops:
        if op[0] == 'L' or op[0] == 'R':
            face = face_after_turn(face, op[0], op[1])
        elif op[0] == 'F':
            if face == 'E':
                x += op[1]
            elif face == 'W':
                x -= op[1]
            elif face == 'N':
                y += op[1]
            else:
                y -= op[1]
        else:
            if op[0] == 'E':
                x += op[1]
            elif op[0] == 'W':
                x -= op[1]
            elif op[0] == 'N':
                y += op[1]
            else:
                y -= op[1]
    return x, y


def face_after_turn(curr_face, direction, degree):
    dirs = 'NESW'
    sign = 1 if direction == 'R' else -1
    steps = degree // 90
    index = dirs.index(curr_face)
    return dirs[(index + sign * steps) % 4]


if __name__ == "__main__":
    x, y = dest_loc(ops)
    print(f'Part 1: {abs(x) + abs(y)}')
