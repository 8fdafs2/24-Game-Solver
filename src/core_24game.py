'''
Created on Sep 11, 2015

@author: ray.wang
'''
import itertools


class oper_lv2():
    def __init__(self, operand_1, operand_2):

        self._operand_1_ = operand_1
        self._operand_2_ = operand_2

        if (isinstance(operand_1, oper_lv2)):
            self.operand_1 = operand_1.dat
        else:
            self.operand_1 = operand_1
        if (isinstance(operand_2, oper_lv2)):
            self.operand_2 = operand_2.dat
        else:
            self.operand_2 = operand_2

    def __str__(self):
        return self.fmt.format(self._operand_1_, self._operand_2_)

    def __eq__(self, other):
        return not self.dat < other and not other < self.dat


class oper_lv2_add(oper_lv2):
    def __init__(self, operand_1, operand_2):
        super().__init__(operand_1, operand_2)
        self.dat = self.operand_1 + self.operand_2
        self.fmt = '( {0} + {1} )'


class oper_lv2_sub(oper_lv2):
    def __init__(self, operand_1, operand_2):
        super().__init__(operand_1, operand_2)
        self.dat = self.operand_1 - self.operand_2
        self.fmt = '( {0} - {1} )'


class oper_lv2_mul(oper_lv2):
    def __init__(self, operand_1, operand_2):
        super().__init__(operand_1, operand_2)
        self.dat = self.operand_1 * self.operand_2
        self.fmt = '( {0} * {1} )'


class oper_lv2_div(oper_lv2):
    def __init__(self, operand_1, operand_2):

        super().__init__(operand_1, operand_2)
        if self.operand_2 == 0:
            self.dat = 1000
        else:
            self.dat = self.operand_1 / self.operand_2
        self.fmt = '( {0} / {1} )'


def oper_lv3_a(operand_1, operand_2, operand_3,
               oper_1, oper_2):
    return oper_1(operand_1, oper_2(operand_2, operand_3))


def oper_lv3_b(operand_1, operand_2, operand_3,
               oper_1, oper_2):
    return oper_1(oper_2(operand_1, operand_2), operand_3)


def oper_lv4_a(operand_1, operand_2, operand_3, operand_4,
               oper_1, oper_2, oper_3):
    return oper_1(
        oper_lv3_a(operand_1, operand_2, operand_3, oper_2, oper_3), operand_4)


def oper_lv4_b(operand_1, operand_2, operand_3, operand_4,
               oper_1, oper_2, oper_3):
    return oper_1(
        oper_lv3_b(operand_1, operand_2, operand_3, oper_2, oper_3), operand_4)


def oper_lv4_c(operand_1, operand_2, operand_3, operand_4,
               oper_1, oper_2, oper_3):
    return oper_1(
        operand_1, oper_lv3_a(operand_2, operand_3, operand_4, oper_2, oper_3))


def oper_lv4_d(operand_1, operand_2, operand_3, operand_4,
               oper_1, oper_2, oper_3):
    return oper_1(
        operand_1, oper_lv3_b(operand_2, operand_3, operand_4, oper_2, oper_3))


def oper_lv4_e(operand_1, operand_2, operand_3, operand_4,
               oper_1, oper_2, oper_3):
    return oper_1(
        oper_2(operand_1, operand_2), oper_3(operand_3, operand_4))


opers_lv2_orig = [oper_lv2_add, oper_lv2_sub, oper_lv2_mul, oper_lv2_div]

opers_lv4_orig = [oper_lv4_a, oper_lv4_b, oper_lv4_c, oper_lv4_d, oper_lv4_e]


# F(a,b,c) = f(a, f(b, c)) | f(f(a, b), c)
# G(a,b,c,d) =
#     f( f(a, f(b, c)),       d )
#     f( a,       f(b, f(c, d)) )
#     f( f(a, b),       f(c, d) )


def calc(operands_orig):
    '''
    >>> operands_orig = [4, 5, 10, 10]
    >>> ret_preset = {'( ( 5 + ( 10 / 10 ) ) * 4 )',
    ...              '( ( ( 10 / 5 ) * 10 ) + 4 )',
    ...              '( ( 10 / ( 5 / 10 ) ) + 4 )',
    ...              '( ( 10 * ( 10 / 5 ) ) + 4 )',
    ...              '( ( 10 * ( 10 / 5 ) ) + 4 )',
    ...              '( ( ( 10 * 10 ) / 5 ) + 4 )',
    ...              '( ( ( 10 / 10 ) + 5 ) * 4 )',
    ...              '( 4 * ( 5 + ( 10 / 10 ) ) )',
    ...              '( 4 + ( ( 10 / 5 ) * 10 ) )',
    ...              '( 4 + ( 10 / ( 5 / 10 ) ) )',
    ...              '( 4 + ( 10 * ( 10 / 5 ) ) )',
    ...              '( 4 + ( ( 10 * 10 ) / 5 ) )',
    ...              '( 4 * ( ( 10 / 10 ) + 5 ) )',
    ...              }
    >>> assert(set(calc(operands_orig)) == ret_preset)
    '''
    ret = []
    operands_iter = set(itertools.permutations(operands_orig))
    opers_lv2_iter = list(itertools.product(opers_lv2_orig, repeat=3))
    for operands in operands_iter:
        for opers_lv2 in opers_lv2_iter:
            for oper_lv4 in opers_lv4_orig:
                tmp = oper_lv4(*(operands + opers_lv2))
                if tmp == 24:
                    ret.append(str(tmp))
    return ret


if __name__ == '__main__':
    import doctest

    doctest.testmod()
