import random

COLORS = ["R","G","B","Y","W","O"]
TRIES=10

# TRIES=int(input("How many times do you want to try?(id suggest choosing 15) ->"))

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
    color_counts = {
        
    }
    correct_pos=0
    incorrect_pos=0
    
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
        
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_code:
            correct_pos += 1
            color_counts[guess_color] -= 1
            
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] >0:
            incorrect_pos -= 1
            color_counts[guess_color] -= 1

        return correct_pos, incorrect_pos
    
    
    
    
def game():
    print(f"Welcome to the game of guessing the code. you have {TRIES} tries to guess the code.")
    print(f'the valid colors are:' ,*COLORS)
    
    code= generate_code()
    for attempt in range(1, TRIES+1):
        guess= guess_code()
        correct_pos, incorrect_pos= check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f'Congratulations! You guessed the correct code in {attempt} tries.')
            break
        
        print(f'Correct Position: {correct_pos} | Incorrect Position: {incorrect_pos}')
        
        
    else:
        print(f'Sorry, you ran out of tries. The correct code was:', *code)
        
        
        
if __name__ == '__main__':
    game()