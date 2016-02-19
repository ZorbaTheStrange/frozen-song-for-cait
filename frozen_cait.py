#! /usr/bin/python3
'''
frozenCait.py - This is a script for my neice that opens a youtube video for a frozen song. 

by zorba
'''

import webbrowser, sys


def frozen_song():
    ''' User gets two choices. let it go (we can add in regualr song if that becomes a thing), or the option to search for a new song. if user picks new song then we ask what kind of frozen song would they like to hear.

        changing the options so it is easier for cait(a three year old) to run.
    '''

    choice = input("\nIf you would like to watch 'Let It Go' Please type 'L.' If you would like to search for a new frozen song Please type 'N'\n\nWhat would you like to watch?: ")

    if choice.lower() == 'l':
        return webbrowser.open('https://www.youtube.com/embed/L0MK7qz13bU')

    elif choice.lower() == 'n':
        new_song = input('\nWhat frozen song would you like to search for? Pleaes ask Uncle Davis to type in the song you would like to search for. \n\nType Here: ')
        return webbrowser.open('https://www.youtube.com/results?search_query=' + 'Frozen' + new_song)
    else:
        print('\nWhoops! It looks like you typed something that I do not understand! Please try again!')
        return frozen_song()


def opening_remarks():
    ''' Prints out the opening print to start of the code.
    '''

    hello =  '==================================== !Hello CaitCait! ===================================='
    welcome = 'Welcome to Frozen CaitCait!'

    print('\n' + hello.center(150, ' ') + '\n')
    print(welcome.center(150, ' ') + '\n')


def main():
    '''
    main
    '''
    opening_remarks()
    frozen_song()


if __name__ == '__main__':
    sys.exit(main())

