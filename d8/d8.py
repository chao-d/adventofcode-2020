import utils.read_input as inp

lst = inp.to_origin_list()


nop_jmp_index = []


def get_acc_value_before_loop(instrs):
    line_visited = set()
    acc = 0

    index = 0
    while index not in line_visited:
        line_visited.add(index)
        op = instrs[index][0]
        num = instrs[index][1]
        if op == 'nop':
            nop_jmp_index.append(index)
            index += 1
        elif op == 'acc':
            acc += num
            index += 1
        else:
            nop_jmp_index.append(index)
            index += num
    return acc


def parse_instructions(ins):
    instrs = []
    for n in ins:
        eles = n.split(' ')
        instrs.append((eles[0], int(eles[1])))
    return instrs


def find_bad_instruction(instrs, nums):
    for to_change in nums:
        line_visited = set()
        acc = 0
        index = 0
        while index not in line_visited:
            line_visited.add(index)
            op = instrs[index][0]
            num = instrs[index][1]
            if index == to_change:
                if op == 'nop':
                    op = 'jmp'
                else:
                    op = 'nop'
            if op == 'nop':
                index += 1
            elif op == 'acc':
                acc += num
                index += 1
            else:
                index += num
            if index >= len(instrs):
                return acc
    return -1


if __name__ == "__main__":
    instrs = parse_instructions(lst)
    print(f'Part 1: {get_acc_value_before_loop(instrs)}')

    print(f"Part 2: {find_bad_instruction(instrs, sorted(nop_jmp_index))}")
