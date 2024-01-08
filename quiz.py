import json
import math

def new_quiz():
  corrects_answers = 0
  question_num = 0
  guess = ''
  for key in questions:
    print("-------------------------")
    print(key)
    for option in options[question_num]:
      print(option)
    guess = input("\nDigit the answer (A, B, C or D): ")
    corrects_answers += check_answer(questions.get(key), guess)
    
    question_num += 1
  finish_game(corrects_answers)
  

def check_answer(answer, guess):
  if answer == guess.upper():
    print("Correct!!")
    return 1
  else:
    print("Wrong!!")
    return 0
  
  
  
def finish_game(corrects_answers):
  print("-------------------------")
  print("Score Rate:", math.floor((corrects_answers/len(questions))*100), "% (", corrects_answers, "/", len(questions), ")")
  play_again = input("Would you like play again? (yes or no): ")
  if play_again.lower() == "yes" or play_again.lower() == 'y':
    new_quiz()


with open("questions.json") as questions:
  file_json = json.load(questions)
  questions = file_json["questions"]
  options = file_json["options"]


print("-----------Quiz Game-------------")
mode = input("What do you want? (P/Play or E/Edit) ")

new_quiz()
