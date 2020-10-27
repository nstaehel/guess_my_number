#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:00:27 2020

@author: noestaeheli
"""

import random

from guess_my_number import MIN, MAX,  GuessMachine

if __name__ == '__main__':
    Min = MIN
    Max = MAX
    guess_machine=GuessMachine()
    while True:
        attempt=random.randint(Min,Max)
        result=guess_machine.guess(attempt)
        print('tried %d: %s' %(attempt,result))
        if result == 'found':
            print('Finished in %d attempts.' %guess_machine.number_of_attempt)
            break
        elif result=='too low':
            Min = attempt + 1
        else:
            Max = attempt - 1