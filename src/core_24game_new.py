import itertools


# F(a,b,c) = f(a, f(b, c)) | f(f(a, b), c)
# G(a,b,c,d) =
#     f( f(a, f(b, c)),       d )
#     f( a,       f(b, f(c, d)) )
#     f( f(a, b),       f(c, d) )


def calc_01(operands):
    ret = []
    opers = {'+': int.__add__,
             '-': int.__sub__,
             '*': int.__mul__,
             '/': lambda x, y: None if y == 0 or x % y != 0 else x // y,
             }

    operands_permutations = list(itertools.permutations(operands))

    for operands in operands_permutations:

        for key_0 in opers:
            operands_0 = opers[key_0](operands[0], operands[1])
            if operands_0 is None:
                continue
            rep_0 = '{} {} {}'.format(operands[0], operands[1], key_0)

            for key_1 in opers:
                operands_1 = opers[key_1](operands_0, operands[2])
                if operands_1 is None:
                    continue
                rep_1 = '{} {} {}'.format(rep_0, operands[2], key_1)

                for key_2 in opers:
                    operands_2 = opers[key_2](operands_1, operands[3])
                    if operands_2 is None:
                        continue
                    rep_2 = '{} {} {}'.format(rep_1, operands[3], key_2)
                    if operands_2 == 24:
                        ret.append(rep_2)

                operands_1 = opers[key_1](operands[2], operands[3])
                if operands_1 is None:
                    continue
                rep_1 = '{} {} {}'.format(operands[2], operands[3], key_1)

                for key_2 in opers:
                    operands_2 = opers[key_2](operands_0, operands_1)
                    if operands_2 is None:
                        continue
                    rep_2 = '{} {} {}'.format(rep_0, rep_1, key_2)
                    if operands_2 == 24:
                        ret.append(rep_2)

    return set(ret)


def calc_02(operands):
    ret = []
    operands_permutations = set(itertools.permutations(operands))

    opers = {'+': int.__add__,
             '-': int.__sub__,
             '*': int.__mul__,
             '/': lambda x, y: None if y == 0 or x % y != 0 else x // y,
             }

    def recur(operands, rep=[]):
        # print(operands)

        n_operands = len(operands)

        if n_operands == 2:
            for key in opers:
                operands___ = opers[key](operands[0], operands[1])
                if operands___ is None:
                    continue
                if operands___ == 24:
                    ret.append('{} {} {}'.format(rep[0], rep[1], key))

        elif n_operands == 3:
            for key in opers:
                operands___ = opers[key](operands[0], operands[1])
                if operands___ is None:
                    continue
                recur([operands___, operands[2]],
                      ['{} {} {}'.format(rep[0], rep[1], key), rep[2]])
                recur([operands[2], operands___],
                      [rep[2], '{} {} {}'.format(rep[0], rep[1], key)])

        else:
            for key in opers:
                operands___ = opers[key](operands[0], operands[1])
                if operands___ is None:
                    continue
                recur([operands___, operands[2], operands[3]],
                      ['{} {} {}'.format(operands[0], operands[1], key), operands[2], operands[3]])

    for operands in operands_permutations:
        # print(operands)
        recur(operands)

    return set(ret)


if __name__ == '__main__':
    operands_orig = [4, 5, 10, 10]
    print(calc_01(operands_orig))
    print(calc_02(operands_orig))
