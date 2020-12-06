import utils.read_input as inp

lst = inp.to_list_by_emptyline()


def count_yes(ans, count_one_group):
    count = 0
    for group_ans in ans:
        count += count_one_group(group_ans)
    return count


def count_anyone_yes(ans):
    char_set = set()
    for n in ans.split(' '):
        for c in n:
            char_set.add(c)
    return len(char_set)


def count_everyone_yes(ans):
    each_ans = ans.split(' ')
    if len(each_ans) == 1:
        return len(each_ans[0])

    count = 0
    char_set = [0] * 26
    for i, n in enumerate(each_ans):
        for c in n:
            curr = char_set[ord(c) - ord('a')]
            curr += 1
            if (i == len(each_ans) - 1 and
                    curr == len(each_ans)):
                count += 1
            char_set[ord(c) - ord('a')] = curr
    return count


print(f'Part 1: {count_yes(lst, count_anyone_yes)}')


print(f'Part 2: {count_yes(lst, count_everyone_yes)}')
