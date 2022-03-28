import os

print("Welcome to the Y11 Factorisng Quadratics Quiz 2022!\n")
print("Program written and quiz composed by Ron Geilik")
print("---------------------------------------------\n")

#Remember to remind users to put no  symbols between brackets in answer, and code try-except to check whether input is valid and provide feedback

questions = ["x^2 + 3x + 2", "x^2 + 8x +15", "x^2 - 8x - 20", "x^2 + 7x - 18", "2x^2 + 8x + 6", "4x^2 + 10x + 6", "9x^2 + 12x + 4", "5x^2 - 13x - 6", "5x^2 - 34x + 24", "25x^2 - 60x + 36"]
answers_1 = ['Answer1', 'Answer2', 'Answer3', 'Answer4', 'Answer5', 'Answer6', 'Answer7', 'Answer8', 'Answer9', 'Answer10']
answers_2 = ['Answer1Alt', 'Answer1Alt', 'Answer3Alt', 'Answer4Alt', 'Answer5Alt', 'Answer6Alt', 'Answer7Alt', 'Answer8Alt', 'Answer9Alt', 'Answer10Alt']

score = 0
def main():
  for question in questions:
    
    print("Simplify {}".format(question))
    answer = input("Answer>> ")
    index = int(questions.index(question))
    

    if (answer == os.environ[answers_1[index]] or os.environ[answers_2[index]]): #<----- Remember to add alt answer as well.

      print ("Correct!")

    else:
      print("Sorry, you didn't get that one. The correct answer was {}".format(os.environ[answers_1[index]]))

    
  
main()

  
  
  
  
        