from core_24game_new import calc_01, calc_02

if __name__ == '__main__':

    print('\n~~~~~~~~~~~ Started ~~~~~~~~~~~\n')

    operands_orig = [1, 5, 7, 9]

    print('Input is {0}\n'.format(operands_orig))

    ret = calc_01(operands_orig)

    if ret:
        for item in ret:
            print('Solution found as: ', item, '= 24')
    else:
        print('Solution not found!')

    print('\n~~~~~~~~~~~ Finished ~~~~~~~~~~~\n')

    print('\n~~~~~~~~~~~ Started ~~~~~~~~~~~\n')

    operands_orig = [1, 5, 7, 9]

    print('Input is {0}\n'.format(operands_orig))

    ret = calc_02(operands_orig)

    if ret:
        for item in ret:
            print('Solution found as: ', item, '= 24')
    else:
        print('Solution not found!')

    print('\n~~~~~~~~~~~ Finished ~~~~~~~~~~~\n')