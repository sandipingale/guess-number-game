import random
import math

def verify_guess(user_number, server_number, range_start, range_end):
    if user_number == server_number:
        return 0
    
    if user_number > server_number:
        return 1
    
    if user_number < server_number:
        return -1
    pass

def do_guess_work(range_start, range_end):
    allow_guess = int(round(math.log2(range_end-range_start+1),0))
    print(f"You are allowed to have {allow_guess} guesses")
    server_number = random.choice(range(range_start, range_end+1))
    guessed = False
    guess_iter = 0
    while(guess_iter <= allow_guess):
        user_number = int(input("Enter your guess number : "))
        guess_status = verify_guess(user_number, server_number, range_start, range_end)
        if guess_status == 0:
            print(f"Congratulation, you guessed {user_number} in {guess_iter+1} guesses")
            guessed = True
            break
        if guess_status < 0:
            print(f"Try Again! You guessed too small")

        if guess_status > 0:
            print(f"Try Again! You guessed too high")

        guess_iter = guess_iter + 1

    if not guessed:
        print("Better Luck Next Time!")

if __name__ == '__main__':
    range_start = int(input("Enter Start of the Range : "))
    range_end = int(input("Enter end of the Range : "))
    do_guess_work(range_start, range_end)
