# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:41:14 2020
Last Edit on Tue Sep 22
@author: Mary PC
Objective: Trivia Quiz
"""
from random import choice

quest_ans = {'woody':'What is the name of the toy cowboy in Toy Story? ',
       'september':'What month are we in? ',
       'earth':'What is the 3rd planet from the sun? ',
       'd':'What is the 4th letter of the alphabet? ',
       'kitten':'What do you call a baby cat? ',
       'luzon':'What is the largest island in the Philippines? ',
       'bat':'What animal is batman inspired from? ',
       'butterfly':'What does a caterpillar turn into? ',
       'paris':'In which capital city, would you find the Eiffel Tower? ',
       'hydrogen':'What does H in the periodic table stands for? ',
       }

exclaim = {'right':['Wow! You got it correct!',
                      'You are awesome! Your answer is correct.',
                      'Amazing! You\'re correct!',
                      'You are doing great! Keep it up!',
                      'You\'re correct! You\'re doing a good job!'],
           'wrong':['Sad. You are wrong.',
                    'You are wrong but that is okay!',
                    'Aww. It is wrong!',
                    'Your answer is not correct.',
                    'This is wrong but it\'s fine!'],
           }

def check(ask):
    ans = input(ask).title()
    while ans not in ['Yes','No']:
        print('Hmm. Something is wrong. Check your spelling!')
        print('Here, try again.') 
        ans = input(ask).title()
    return ans

def game(Quest_Ans=quest_ans, Exclaim=exclaim, score = 0): 
    print('\nWelcome to the Ultimate Trivia Game!')
    print('Can you answer all 10 of these super easy trivia questions?')  
    
    ready = check('Are you ready (\'Yes\' or \'No\')? ')
    if ready == 'No': return print('Okay! See you later~')
    print('Let us begin!')
    
    for correct in Quest_Ans:
        answer = input(Quest_Ans[correct]).lower()
        if answer == correct: 
            print(choice(Exclaim['right'])); score += 1
        else: print(choice(Exclaim['wrong']))    
    
    total = len(Quest_Ans)
    print('\nYou answered %d out of %d questions correct.'%(score,total))
    if score <= (total/2): print('You failed but that\'s okay.')
    elif score == total: print('Wow! You got a perfect score!')
    else: print('Nice. You did a good job!')    
    
    again = check('Do you want to try again (\'Yes\' or \'No\')? ')
    if again == 'Yes': return game()
    print('Okay! Thank you for answering~')   
    
    
    
    