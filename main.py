"""

Karim Rivera-Apolinar

12/12/2022

Capitals of Different Countries

Purpose: To quiz the user on the names of capitals of 10 different countries.

Description:
Provides user with a different password each time, where user has to type it in
to access program. Afterwards it asks the user for their name and their guess
of how many correct out of 10 they will get. User then takes quiz and is told
how many are correct. Their name and score is then recorded in a txt file,
which is used to create leaderboard at the end, this leaderboard is not sorted
it justs states a name and score, user can make comparisons by themselves.

"""


import string
import random
import os
os.system('cls')


# Define a function that generates a password

password_length = random.randint(8, 16)


def generate_password(password_length):
    """
    Will generate a random password with specific restrictions, it can only use
    letters and numbers its length is somewhat random, at the end it tells the
    user what the password is
    """

    # Create a list of possible characters for the password
    # This includes uppercase and lowercase letters, digits, and punctuation
    possible_characters = string.ascii_letters + string.digits

    # Generate the password by choosing random characters from the list of possible characters
    password = "".join(random.choices(possible_characters, k=password_length))

    # Return the generated password
    return password


# Generate a password and print it to the screen
# Define the password

password = generate_password(password_length)
print(f"Your password is: {password}")


# Use a while loop to ask the user for their password
# Keep looping until the user enters the correct password
while True:
    user_password = input(
        "Enter your password: ")

    # Check if the user's password is correct
    if user_password == password:
        # If the password is correct, break out of the loop
        print("Correct password")
        break
    else:
        # If the password is incorrect, continue looping
        print("Incorrect password, please try again.")

os.system('cls')
# Asks the user what their name is in a specific format
user_name = input('What is your name (First, Last)? ')
title_name = user_name.title()
guessNumberCorrect = input(
    '\nOut of 10 how many do you think you will get correct?')

try:

    number = int(guessNumberCorrect)
    print(f'You entered the number {number}.')
except ValueError:
    # This code will only be executed if the code in the try block raises a ValueError
    # (which will happen if the user enters a non-numeric value)
    print('You did not enter a valid number. Please try again.')
    while ValueError:
        print(guessNumberCorrect)


"""



Place Holder



"""


# Define a list of quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    {
        "question": "What is the capital of Canada?",
        "answer": "Ottawa"
    },
    {
        "question": "What is the capital of India?",
        "answer": "New Delhi"
    },
    {
        "question": "What is the capital of Ecuador?",
        "answer": "Quito"
    },
    {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"

    },
    {
        "question": "What is the capital of the United Kingdom?",
        "answer": "London"
    },
    {
        "question": "What is the capital of Venezuela?",
        "answer": "Caracas"
    },
    {
        "question": "What is the capital of China?",
        "answer": "Beijing"
    }
]

# Define a function that takes in a list of questions and asks each question to the user
# The function returns the number of correct answers


def take_quiz(questions):
    """
    Enables user to take a quiz using a for loop where it searches for a questiona and its answer.
    number of answers correct are kept and at the end your score is returned
    """
    # Keep track of the number of correct answers
    correct_answers = 0

# Ask each question to the user
    for question in questions:
        # Print the question
        print(question["question"])

        # Ask the user for their answer
        user_answer = input("Your answer: ")

        # Check if the user's answer is correct
        if user_answer.lower() == question["answer"].lower():
            # If the answer is correct, increment the number of correct answers
            correct_answers += 1

    # Return the number of correct answers
    return correct_answers


# Test the quiz function
num_correct = take_quiz(questions)
print(f"You got {num_correct} out of {len(questions)} questions correct.")
if int(guessNumberCorrect) == 10 and num_correct == 10:
    print("You were right, maybe confidence really is key!")

"""Creates a variable named leaderboard that will be used to create
a leaderboard at the end of this program """

leaderboard = []
f = open('Leaderboard.txt', 'r', encoding="utf8")
leaderboard = [line.replace('\n', '') for line in f.readlines()]
print(leaderboard)
"""





"""
# opens a text file named "Leaderbaord", file contains names and scores of users
saveFile = open('Leaderboard.txt', 'a', encoding="utf8")


stats = title_name + ' ' + str(num_correct)
saveFile.write(stats)
saveFile.write('\n')


countries = ['Netherlands', 'China', 'Wales', 'Africa', 'Canada', 'Bolivia']
rankings = ['1', '2', '3', '4', '5', '6']
countries.append('Japan')
countries.remove('Africa')
countries.insert(0, 'Brazil')
