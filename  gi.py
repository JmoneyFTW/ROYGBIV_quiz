print("Hello! Welcome to the ROYGIV quiz! Guess the correct answers for all of the questions to pass!")

playing = input("Do you want to play?\n")

if playing != "yes":
    quit()

print("Okay! Let's start!")

answer = input("Question 1: What does the R stand for in ROYGBIV?\n")
if answer == "red":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 2: What does the V stand for in ROYGIV?\n")
if answer == "violet":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 3: What does the O stand for in ROYGBIV?\n")
if answer == "orange":
    print("Corrrect!")
else:
    print("Incorrect!")

answer = input("Question 4: What does the I stand for in ROYGBIV?\n")
if answer == "indigo":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 5: What does the B stand for in ROYGBIV?\n")
if answer == "blue":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 6: What does the Y stand for in ROYGBIV?\n")
if answer == "yellow":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Question 7: What does the G stand for in ROYGBIV?\n")
if answer == "green":
    print("Correct!")
else:
    print("Incorrect!")

print("Awesome! you've succesfully completed the quiz! Thanks for playing!")
