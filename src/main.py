from core_24game import calc

if __name__ == '__main__':

    print('\n~~~~~~~~~~~ Started ~~~~~~~~~~~\n')

    operands_orig = [1, 5, 7, 9]

    print('Input is {0}\n'.format(operands_orig))

    ret = calc(operands_orig)

    if ret:
        for item in ret:
            print('Solution found as: ', item, '= 24')
    else:
        print('Solution not found!')

    print('\n~~~~~~~~~~~ Finished ~~~~~~~~~~~\n')
