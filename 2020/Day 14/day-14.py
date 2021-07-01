import os
from pprint import pprint


def both_part(data):
    total = 0
    memory1 = dict()
    memory2 = dict()
    mask = ''

    for inst in data:
        left, right = inst.split(' = ')

        if left == 'mask':
            mask = right
        else:
            addr, value = left[4:-1], list(f'{int(right):0>36b}')

            for bit in range(36):
                if mask[bit] != 'X':
                    value[bit] = mask[bit]

            value = int(''.join(value), 2)
            memory1[addr] = value

            addr = list(f'{int(addr):0>36b}')
            flt = mask.count('X')

            for bit in range(36):
                if mask[bit] != '0':
                    addr[bit] = mask[bit]

            for num in range(2 ** flt):
                temp = addr[:]
                bits = f'{num:0>{flt}b}'

                for bit in bits:
                    temp[temp.index('X')] = bit

                memory2[int(''.join(temp), 2)] = int(right)

    return sum(memory1.values()), sum(memory2.values())



def testcase():
    program = open(os.path.join(os.path.dirname(__file__), "day-14-test.txt")).read()
    program = program.split('\n')

    assert both_part(program) == (51, 208)


if __name__ == "__main__":
    testcase()

    program = open(os.path.join(os.path.dirname(__file__), "day-14-input.txt")).read()
    program = program.split('\n')


    print('Part 1: {0}\nPart 2: {1}'.format(*both_part(program)))