# database_functions.py
import mysql.connector
from database_settings import *

def insert_score(name, score):
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Insert the score into the database
    cursor.execute('''
    INSERT INTO scores (name, score)
    VALUES (%s, %s)
    ''', (name, score))

    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()

    print("Score saved successfully!")
