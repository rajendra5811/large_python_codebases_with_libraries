#(<10 lines) that uses some features of the Standard Library to randomly pick a cat name and print out a short message for that cat
import random, os

catString = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--, --Henry--, --Mr.Paws--"
def RANDOM_CAT(string_list):
    cat_list = catString.split(', ')# split the cats
    cat_list = [cat.strip('--') for cat in cat_list]
    return random.choice(cat_list)

print(  f'{RANDOM_CAT(catString)} is a good kitty'  )
# exception
"""story =  "Once upon a time there was a very long string that was 
          over 100 characters long and could not all fit on the 
          screen at once."
print(story)  SyntaxError: EOL while scanning string literal """ 

story =  "Once upon a time there was a very long string that was " + \
         "over 100 characters long and could not all fit on the " + \
         "screen at once."
print(story)
