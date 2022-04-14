import os
import sys
from random import randint, shuffle
import time

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

print("Welcome to the Y11 Factorisng Quadratics Quiz 2022!\n")
print("Program written and quiz composed by Ron Geilik")
print("---------------------------------------------\n")

print("Automatically starting the quiz in: ")
countdown(10)



     
    
#Remember to remind users to put no  symbols between brackets in answer, and code try-except to check whether input is valid and provide feedback
  
questions = ["x^2 + 3x + 2", "x^2 + 8x +15", "x^2 - 8x - 20", "x^2 + 7x - 18", "2x^2 + 8x + 6", "4x^2 + 10x + 6", "9x^2 + 12x + 4", "5x^2 - 13x - 6", "5x^2 - 34x + 24", "25x^2 - 60x + 36"]
answers_1 = ['Answer1', 'Answer2', 'Answer3', 'Answer4', 'Answer5', 'Answer6', 'Answer7', 'Answer8', 'Answer9', 'Answer10']
answers_2 = ['Answer1Alt', 'Answer1Alt', 'Answer3Alt', 'Answer4Alt', 'Answer5Alt', 'Answer6Alt', 'Answer7Alt', 'Answer8Alt', 'Answer9Alt', 'Answer10Alt']
answers_char = ["a"]


#Program function to start the actual program

  
  #Main variables
running = 10
score = 0

  #The main part of the program() function
def main():
  for question in questions:
    index = int(questions.index(question))
    possible_answers = ["(x+{})(x+{})".format(str(randint(1, 10)), str(randint(1, 10))), "(x+{})(x+{})".format(str(randint(1, 10)), str(randint(1, 10))), "(x+{})(x+{})".format(str(randint(1, 10)), str(randint(1, 10))), os.environ[answers_1[index]]]
    shuffle(possible_answers)
    option_1 = "a) {}".format(possible_answers[0])
    option_2 = "b) {}".format(possible_answers[1])
    option_3 = "c) {}".format(possible_answers[2])
    option_4 = "d) {}".format(possible_answers[3])
    print("Question: {}\n".format(str(question)))
    print("Options: (Please input the answer exactly as it is on the options\n e.g instead of 'a', input (x+__)(x+__))\n {}\n {}\n {}\n {}\n".format(option_1, option_2, option_3, option_4))
    
    try:
      answer = input("Answer>> ")
      #Checks if the answer is one of the options. If not, displays that you have not entered a valid option
      if answer in (possible_answers):
        correct_answer_1 = str(os.environ[answers_1[index]])
        correct_answer_2 = str(os.environ[answers_2[index]])
      
      
      #Answer-checking part
        if (answer.casefold() == correct_answer_1 or answer.casefold() == correct_answer_2): 
  
          print ("Correct!\n")
          global score
          score += 1
          global running
          running -= 1
  
        else:
          print("Sorry, you didn't get that one. The correct answer was {} and       {}".format(os.environ[answers_1[index]], os.environ[answers_2]))
      else:
        print("Incorrect Input")
    #Checks for any errrors
    except TypeError:
      print("\nSorry, you didn't get that one. The correct answer was {}\n".format(os.environ[answers_1[index]]))
      
      
      if running == 0:
        print("Thank you for completing the quiz. Your score was {}/10".format(str(score)))
      else:
        
        running -= 1
        pass
  

#While loop to keep the program running while there are questions left.
while running > 1:
  main()
  #Exit message
if (running == 0):
  print("Thank you for completing this quiz. Your score was {}/10".format(str(score)))

  #Checks if the user has inputed "Start" and starts the program

  