import utils.read_input as inp

lst = inp.to_list_by_emptyline()


def count_valid_passports(ps, is_valid):
    count = 0
    for p in ps:
        if is_valid(p):
            count += 1
    return count


def is_valid_passport_coarse(p):
    keys = set([pair.split(':')[0] for pair in p.split(' ')])
    return len(keys) == 8 or (len(keys) == 7 and 'cid' not in keys)


print(f'Part 1: {count_valid_passports(lst, is_valid_passport_coarse)}')


def is_valid_passport(p):
    mapping = {}
    for pair in p.split(' '):
        k, v = pair.split(':')
        mapping[k] = v

    if not (len(mapping) == 8 or
            (len(mapping) == 7 and 'cid' not in mapping)):
        return False

    if int(mapping['byr']) < 1920 or int(mapping['byr']) > 2002:
        return False

    if int(mapping['iyr']) < 2010 or int(mapping['iyr']) > 2020:
        return False

    if int(mapping['eyr']) < 2020 or int(mapping['eyr']) > 2030:
        return False

    hgt = mapping['hgt']
    if hgt.endswith('cm') or hgt.endswith('in'):
        num = hgt[:-2]
        try:
            num = int(num)
            if hgt.endswith('cm') and (num < 150 or num > 193):
                return False
            if hgt.endswith('in') and (num < 59 or num > 76):
                return False
        except ValueError:
            return False
    else:
        return False

    hcl = mapping['hcl']
    if not hcl.startswith('#') or len(hcl[1:]) != 6:
        return False

    for c in hcl[1:]:
        if not ('0' <= c <= '9' or 'a' <= c <= 'f'):
            return False

    ecl = mapping['ecl']
    ecl_set = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if ecl not in ecl_set:
        return False

    if not (mapping['pid'].isdigit() and len(mapping['pid']) == 9):
        return False

    return True


print(f'Part 2: {count_valid_passports(lst, is_valid_passport)}')
