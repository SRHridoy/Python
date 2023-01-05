questions = [ ["Which language was used to create Facebook?", "Python", "English", "Go", "PHP", "None" , 4],
["What is the capital of Bangladesh?", "Delhi", "Barishal", "Dhaka", "Rajshahi", "Dinajpur", 2],
["When Facebook was invented?", "2003", "1990", "2005", "1972", "2004", 4] ]

levels = [1000, 2000,3000, 5000, 10000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"a. {questions[i][1]}       b. {questions[i][2]}")
    print(f"c. {questions[i][3]}       d. {questions[i][4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit >>>>> "))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
    else:
        print("Wrong answer! ")
    break

print(f"Your take home money is {money}")