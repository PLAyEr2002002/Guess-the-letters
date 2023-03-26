import random

COLORS = ["R","G","B","Y","W","O"]
TRIES=10
CODE_LENGTH=4


def generate_code():
    code=[]

    for _ in range(CODE_LENGTH):
        color=random.choice(COLORS)
        code.append(color)
        
    return code


def guess_code():
    while True:
        guess=input("Guess: ").upper().split(" ")
        
        if len(guess)!= CODE_LENGTH: 
            print(f'You must enter {CODE_LENGTH} letters.')
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f'"{color}" is not a valid color. try again.')
                break
            
            else:
                break
    return guess


def check_code(guess, real_code):
    