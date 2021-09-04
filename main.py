# -*- coding: utf-8 -*-
import sys
import time
def main():
    n = 0
    n2 = 0
    n = input('Please enter an integer.')
    try:
        int(n)
        integer = True
    except ValueError:
        print('Do not enter anything other than an integer.')
        print('\n')
        integer = False
    if integer == True:
        while n != 1:
            if int(n) % 3 == 0:
                n = int(n) // 3
                print('Now number is ' + str(n) + '.')
                n2 = int(n2) + 1
            else:
                n = int(n) + 1
                print('Now number is ' + str(n) + '.')
                n2 = int(n2) + 1
        print('Executed ' + str(n2) + ' times.')
        choice()

    else:
        main()

def choice():
    print('\n')
    print('Would you like to do it again?')
    print('Enter c to continue and e to finish.')
    print('\n')
    ch = input('Which one?')
    if ch == 'c':
        print("OK! Let's do it again!")
        print('\n')
        main()
    elif ch == 'e':
        sys.exit()
    else:
        print('\n')
        print('Enter c or e.')
        choice()

if __name__ == '__main__':
    main()