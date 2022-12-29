# KBC game show simulation in Python

# list to store the questions and their correct answers
questions = [
    { "question": "Which of the following is the capital of India?", "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "correct_option": "New Delhi" },
    { "question": "Which of the following is the currency of Japan?", "options": ["Yen", "Dollar", "Euro", "Pound"], "correct_option": "Yen" },
    { "question": "Who is the current President of the United States?", "options": ["Joe Biden", "Donald Trump", "Barack Obama", "George W. Bush"], "correct_option": "Joe Biden" },
    { "question": "Which of the following is the highest mountain peak in the world?", "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "correct_option": "Mount Everest" }
]

# initial amount the person is taking home
amount = 0

# iterate over the questions and ask the user for their answer
for i, question in enumerate(questions):
    print(f"Question {i+1}: {question['question']}")
    for j, option in enumerate(question['options']):
        print(f"{j+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if user_answer == question['correct_option']:
        print("Correct answer! You win the prize money.")
        amount += 10000
    else:
        print("Incorrect answer. Better luck next time.")
        break

# display the final amount the person is taking home
print(f"You are taking home a total of Rs. {amount}.")
