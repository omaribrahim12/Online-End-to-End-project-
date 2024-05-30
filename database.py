import mysql.connector

def insert_user_data(name, age, email , score):

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='companydatabase'
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Insert the data into the table
    cursor.execute('''
    INSERT INTO users (name, age, email , score)
    VALUES (%s, %s, %s , %s)
    ''', (name, age, email, score))

    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()

    print('Data saved successfully!')


def retrieve_user_data_by_email(email):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='companydatabase'
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute SQL query to retrieve data based on email
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user_data = cursor.fetchone()  # Assuming only one user per email, fetch one row

        return user_data

    except mysql.connector.Error as error:
        print("Error retrieving data:", error)

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()