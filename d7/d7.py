import utils.read_input as inp

lst = inp.to_origin_list()


def count_one_color(color):
    count = 0
    mapping = {}
    visited = {}

    for ele in lst:
        rule = parse_entry(ele)
        mapping[rule[0]] = rule[1]

    for k, v in mapping.items():
        for m, _ in v.items():
            if m == color:
                visited[k] = True
                break

    for k, v in mapping.items():
        if dfs(color, mapping, visited, k, v):
            count += 1
    return count


def dfs(color, mapping, visited, curr_k, curr_v):
    if curr_k in visited:
        return visited[curr_k]

    if curr_k == color or len(curr_v) == 0:
        visited[curr_k] = False
        return False
    found_one = False
    for m, _ in curr_v.items():
        if m == color:
            visited[curr_k] = True
            return True
        else:
            if m in mapping:
                res = dfs(color, mapping, visited, m, mapping[m])
                visited[m] = res
                found_one = found_one or res

    visited[curr_k] = found_one
    return found_one


# (blue, {red: 1, green: 2}
# (yellow, {})
def parse_entry(entry):
    tmp = entry.split(' contain ')
    if tmp[1].startswith('no'):
        return tmp[0][:-5], {}
    else:
        if tmp[1].find(',') == -1:
            if tmp[1].endswith('bag.'):
                pair = split_bag_count(tmp[1][:-5])
            else:
                pair = split_bag_count(tmp[1][:-6])
            return tmp[0][:-5], {pair[0]: pair[1]}
        else:
            curr = tmp[1].removesuffix('.')
            ctns = curr.split(', ')
            dic = {}
            for ctn in ctns:
                if ctn.endswith('bag'):
                    pair = split_bag_count(ctn[:-4])
                else:
                    pair = split_bag_count(ctn[:-5])
                dic[pair[0]] = pair[1]
            return tmp[0][:-5], dic


def split_bag_count(entry):
    index = 0
    for c in entry:
        if c == ' ':
            break
        index += 1

    return entry[index + 1:], int(entry[:index])


print(f'Part 1: {count_one_color("shiny gold")}')
