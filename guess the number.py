import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    
    lower_range = int(input("Enter the lower range for the number: "))
    upper_range = int(input("Enter the upper range for the number: "))
    
    secret_number = random.randint(lower_range, upper_range)
    attempts = 0
    
    while True:
        guess = int(input("Guess a number: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()