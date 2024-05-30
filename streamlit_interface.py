import streamlit as st
from database import insert_user_data

# Function to display questions and get answers
def questions():
    score = 0
    
    # Question 1
    st.write("What is the correct syntax to output 'Hello, World' in Python?")
    answer_1 = st.radio("Choose your answer:", options=["a) echo 'Hello, World'", "b) print('Hello, World')", "c) printf('Hello, World')", "d) console.log('Hello, World')"])
    
    # Question 2
    st.write("What is the value of π (pi) up to two decimal places?")
    answer_2 = st.radio("Choose your answer:", options=["a) 3.12", "b) 3.14", "c) 3.16", "d) 3.18"])
    
    # Question 3
    st.write("Who was the first President of the United States?")
    answer_3 = st.radio("Choose your answer:", options=["a) Abraham Lincoln", "b) Thomas Jefferson", "c) George Washington", "d) John Adams"])
    
    # Question 4
    st.write("Which is the largest ocean on Earth?")
    answer_4 = st.radio("Choose your answer:", options=["a) Atlantic Ocean", "b) Indian Ocean", "c) Arctic Ocean", "d) Pacific Ocean"])
    
    # Question 5
    st.write('Who wrote "Romeo and Juliet"?')
    answer_5 = st.radio("Choose your answer:", options=["a) Charles Dickens", "b) Jane Austen", "c) William Shakespeare", "d) Mark Twain"])
    
    return answer_1, answer_2, answer_3, answer_4, answer_5

# Main Streamlit app
def main():
    st.title("Quiz App")
    name = st.text_input("Please Enter your name")
    age = st.text_input("How old are you?")
    email = st.text_input("Please enter your email address")

    start_test = st.button("Start the Test")
    
    if start_test:
        st.write("Answer the following questions:")
        answer_1, answer_2, answer_3, answer_4, answer_5 = questions()
        
        submit = st.button("Submit Answers")
        if submit:
            score = 0
            if answer_1 == "b) print('Hello, World')":
                score += 1
            if answer_2 == "b) 3.14":
                score += 1
            if answer_3 == "c) George Washington":
                score += 1
            if answer_4 == "d) Pacific Ocean":
                score += 1
            if answer_5 == "c) William Shakespeare":
                score += 1
            
            st.write("Your score is:", score, "/ 5")
            insert_user_data(name, age, email, score)
            st.success("Data submitted successfully!")

if __name__ == "__main__":
    main()
