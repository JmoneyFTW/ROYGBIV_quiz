print("Hello! Welcome to the ROYGIV quiz! Guess the correct answers for all of the questions to pass!")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
  quit()

print ("Okay! Let's start!")

score = 0

answer = input("Question 1: What does the R stand for in ROYGBIV?\n")
if answer.lower() == "red":
  print("Correct! Next question")
  score += 1
else:
  print("Incorrect!")

answer = input("Question 2: What does the V stand for in ROYGIV?\n")
if answer.lower() == "violet":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("Question 3: What does the O stand for in ROYGBIV?\n")
if answer.lower() == "orange":
  print("Corrrect!")
  score += 1
else:
  print("Incorrect!")

answer = input("Question 4: What does the I stand for in ROYGBIV?\n")
if answer.lower() == "indigo":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("Question 5: What does the B stand for in ROYGBIV?\n")
if answer.lower() == "blue":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("Question 6: What does the Y stand for in ROYGBIV?\n")
if answer.lower() == "yellow":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer= input("Question 7: What does the G stand for in ROYGBIV?\n")
if answer.lower() == "green":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("Awesome! you've succesfully completed the quiz! Thanks for playing!")
print("You've got " + str(score) + " questions correct!")
print("You've scored " + str((score / 7) * 100) + "%.")
