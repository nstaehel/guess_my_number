#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:52:14 2020

@author: noestaeheli
"""

import random

MIN = 0
MAX = 1000

if __name__ == '__main__' :
    number_to_guess=random.randint(MIN, MAX)
    print('Hey ! Try to guess a number between %d and %d' %(MIN,MAX))
    
    while True:
        user_input=input('Your guess ?')
        try:
            user_attempt=int(user_input)
            if user_attempt == number_to_guess:
                print('Fantastic ! You could find the number I had in mind')
                break
            elif user_attempt < number_to_guess:
                print('Too low')
            else:
                print('Too high')
        except ValueError:
            print('You joker... That was not an integer!')
                
    