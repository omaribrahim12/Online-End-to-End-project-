# main_script.py
from database_functions import insert_score
from questions_functions import questions

# Get user's name
name = input('Please enter your name: ')

# Call the function to ask questions and calculate the score
score = questions()

# Insert the score into the database
insert_score(name, score)
