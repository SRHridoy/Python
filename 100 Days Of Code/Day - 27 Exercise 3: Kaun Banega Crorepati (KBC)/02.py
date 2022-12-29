questions = [
    ("What is the capital of India?", "New Delhi"),
    ("What is the currency of Japan?", "Yen"),
    ("Who is the founder of Facebook?", "Mark Zuckerberg"),
    ("What is the chemical symbol for gold?", "Au"),
    ("Who is the current President of the United States?", "Joe Biden"),
]

prize_money = [100, 200, 300, 500, 1000]

total_amount = 0

for i in range(len(questions)):
    question, correct_answer = questions[i]
    print(f"Question {i+1}: {question}")
    answer = input("Enter your answer: ")
    if answer == correct_answer:
        print("Correct answer! You win Rs.", prize_money[i])
        total_amount += prize_money[i]
    else:
        print("Incorrect answer! Better luck next time.")

print(f"Congratulations! You are taking home a total of Rs. {total_amount}.")
