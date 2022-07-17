import random
from secrets import choice

"""

"""

def guessing_game():
    answer = random.randint(0, 100)
    print(answer)
    attempts = 0
    while True:
        if attempts == 3:
            print('You have used up all 3 attempts')
            break
        user_guess = int(input('What is your guess? '))
        attempts += 1

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')

        

if __name__ == "__main__":
    guessing_game()