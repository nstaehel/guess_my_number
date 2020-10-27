#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:52:14 2020

@author: noestaeheli
"""

import random

MIN = 0
MAX = 1000

class GuessMachine():
    '''
    I have a number in mind,
    you have to guess it !
    
    + self._number_to_guess is generated during creation of the object
    + Use 'guess(num)' method to make a guess
    + I'll count the number of attempt in self.number_of_attempt
    '''
    def __init__(self):
        self._number_to_guess = random.randint(MIN,MAX)
        self.number_of_attempt = 0
    
    def guess(self,num):
        '''
        Attempt to find the right number
        it returns 'too high', 'too low', 'found'

        '''
        self.number_of_attempt+=1
        if num < self._number_to_guess:
            return 'too low'
        elif num > self._number_to_guess:
            return 'too high'
        else:
            return 'found'
    


if __name__ == '__main__' :
    guess_machine = GuessMachine()
    print('Hey! Try to guess a number between %d and %d' %(MIN,MAX))
    
    while True:
        user_input = input('Your guess ?')
        try:
            user_attempt=int(user_input)
            result = guess_machine.guess(user_attempt)
            if result == 'find':
                print(
                    'Fantastic !You could find '
                    'the number I had in mind'
                    'in %d attempt' %guess_machine.number_of_attempt)
                break
            else:
                print(result)
        except ValueError:
            print('You joker... That was not an integer!')
                
    