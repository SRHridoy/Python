questions = [
    {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "answer": "Delhi"},
    {"question": "Who is the current Prime Minister of India?", "options": ["Narendra Modi", "Rahul Gandhi", "Sonia Gandhi", "Manmohan Singh"], "answer": "Narendra Modi"},
    {"question": "Which of the following is not a programming language?", "options": ["Java", "C++", "Python", "Microsoft Word"], "answer": "Microsoft Word"},
    {"question": "Which is the largest planet in the Solar System?", "options": ["Earth", "Jupiter", "Saturn", "Mars"], "answer": "Jupiter"},
]

score = 0
for question in questions:
    print(question["question"])
    print("Options:")
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")
    answer = input("Enter your answer: ")
    if answer.lower() == question["answer"].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")

print(f"You scored {score} out of {len(questions)}.")
