import random
import os

choices = {
    '1': 10,
    '2': 5,
    '3': 3
}

random_number = 0

def generate_number():
    return random.randint(1, 100)

def Congrats(cont_attemps):
    return f"Congratulations! You guessed the correct number in {cont_attemps} attempts."

def Incorrect(random_number, number):
    if random_number > number:
        return f"Incorrect! The number is greater than {number}."
    else:
        return f"Incorrect! The number is less than {number}."

while(True):
    print(
    """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
    """)

    #Invalid option of main menu
    option = input("Enter your choice: ")
    if choices.get(option) == None:
        print('Invalid option')
        exit(0)
    else:
        pass
    
    tries = 1
    random_number = generate_number()
    print("""Great! You have selected the Medium difficulty level.
    Let's start the game!""")

    while(tries <= choices[option]):
        try:
            number = int( input('Enter your guess: ') )
        except ValueError:
            number = int( input('It´s not a number. Input the number please: ') )

        if random_number == number:
            print(Congrats(tries))
            break
        else:
            print(Incorrect(random_number, number))

        tries += 1
    print('You\'ve lost :(') if tries == choices[option] else None

    another_round = input('Do you want to play another round?')
    if another_round.lower() != 'yes':
        print('Goodbye, see you soon!')
        break
    
    #Clean the console
    os.system("cls")