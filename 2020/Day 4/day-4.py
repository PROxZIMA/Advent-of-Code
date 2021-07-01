import re
import os


# keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def valid_field(l, keys):
    return (('cid' in keys) and l == 8) or ('cid' not in keys) and l == 7

def validhgt(hgt):
    if hgt[-2:] == 'cm' and (150 <= int(hgt[:-2]) <= 193):
        return True

    elif hgt[-2:] == 'in' and (59 <= int(hgt[:-2]) <= 76):
        return True

    return False


def validhcl(hcl):
    return re.match(r'^#[0-9a-f]{6}$', hcl)


def validecl(ecl):
    l = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in l


def validpid(pid):
    return re.match(r'^[0-9]{9}$', pid)


def validate(data: dict):
    return  (1920 <= int(data['byr']) <= 2002) and \
            (2010 <= int(data['iyr']) <= 2020) and \
            (2020 <= int(data['eyr']) <= 2030) and \
            validhgt(data['hgt']) and \
            validhcl(data['hcl']) and \
            validecl(data['ecl']) and \
            validpid(data['pid'])


def both_part(data_):
    valid, valid_data = 0, 0
    d = ''

    for line in iter(data_.splitlines()):
        if line != '':
            d += line + ' '

        else:
            data = dict((k, v) for k, v in (elem.split(':') for elem in d.split()))
            keys = data.keys()
            l = len(keys)

            if valid_field(l, keys):

                if validate(data):
                    valid_data += 1

                valid += 1

            d = ''

    return valid, valid_data


def testcase():
    pass_data = open(os.path.join(os.path.dirname(__file__), "day-4-test.txt")).read()

    assert both_part(pass_data) == (2, 2)


if __name__ == "__main__":
    testcase()

    pass_data = open(os.path.join(os.path.dirname(__file__), "day-4-input.txt")).read()

    print('Part 1: {0}\nPart 2: {1}'.format(*both_part(pass_data)))