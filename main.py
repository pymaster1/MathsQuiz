import os
from random import randint, shuffle
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
    index = int(questions.index(question))
    possible_answers = ["(x+{})(x+{})".format(str(randint(1, 10)), str(randint(1, 10))), "(x+{})(x+{})".format(str(randint(1, 10)), str(randint(1, 10))), "(x+{})(x+{})".format(str(randint(1, 10)), str(randint(1, 10))), os.environ[answers_1[index]]]
    shuffle(possible_answers)
    option_1 = "a) {}".format(possible_answers[0])
    option_2 = "b) {}".format(possible_answers[1])
    option_3 = "c) {}".format(possible_answers[2])
    option_4 = "d) {}".format(possible_answers[3])
    print("Options:\n {}\n {}\n {}\n {}\n".format(option_1, option_2, option_3, option_4))
    
    answer = input("Answer>> ")
    
    correct_answer_1 = str(os.environ[answers_1[index]])
    correct_answer_2 = str(os.environ[answers_2[index]])
    print(correct_answer_1)
    print(type(correct_answer_1))
    

    if (answer == correct_answer_1 or answer == correct_answer_2): 

      print ("Correct!")

    else:
      print("Sorry, you didn't get that one. The correct answer was {} and {}".format(os.environ[answers_1[index]], os.environ[answers_2]))

    
  
main()

  
  
  
  
        