from database import insert_user_data
from database import retrieve_user_data_by_email


#Questions 
def questions():
    print('What is the correct syntax to output "Hello, World" in Python? \n a) echo "Hello, World" \n b) print("Hello, World") \n c) printf("Hello, World") \n d) console.log("Hello, World")')
    answer_1 = input()
    score = 0
    if answer_1 == "b":
        score = score + 1
    else:
        score 
    print('What is the value of π (pi) up to two decimal places? \n a) 3.12 \n b) 3.14 \n c) 3.16 \n d) 3.18')
    answer_2 = input()
    if answer_2 == "b":
        score = score + 1
    else:
        score
    print('Who was the first President of the United States? \n a) Abraham Lincoln \n b) Thomas Jefferson \n c) George Washington \n d) John Adams')
    answer_3 = input()
    if answer_3 == "c":
        score += 1
    else:
        score
    print('Which is the largest ocean on Earth? \n a) Atlantic Ocean \n b) Indian Ocean \n c) Arctic Ocean \n d) Pacific Ocean')
    answer_4 = input()
    if answer_4 == "d":
        score += 1
    else:
        score
    print('Who wrote "Romeo and Juliet"? \n a) Charles Dickens \n b) Jane Austen \n c) William Shakespeare \n d) Mark Twain')
    answer_5 = input()
    if answer_5 == "c":
        score += 1
    else:
        score
    print("your score is ", score , "/ 5")
    return score


#Main

while True:
    start = input('Welcome to the test. Press 1 to start or 2 to get your result: ')
    if start == "1":
        name = input('Please Enter your full name* ').strip()
        if not name:
            print("Name is required, please try again ")
            continue
        age = input('How old are your?* ')
        email = input('Please enter your email address: ')
        # Call the function to insert data into the database
        score = questions()
        break  # Exit the loop if user entered "1"
    elif start == "2":
        email_to_search = input("Enter the email address to retrieve user data: ")
        user_data = retrieve_user_data_by_email(email_to_search)

        if user_data:
            print("User found:")
            print("Name:", user_data[0])
            print("Age:", user_data[1])
            print("Score:", user_data[3])
            # Continue with other data retrieval as needed
        else:
            print("User with this email address not found.")

    else:
        exit()
    


insert_user_data(name, age, email, score)

