import json
import math

def new_quiz():
  corrects_answers = 0
  question_num = 0
  for key in questions:
    print("----------- Quiz Game / Game -------------")
    print(key)
    for option in options[question_num]:
      print(option)
    guess = input("\nDigit the answer (A, B, C or D): ")
    corrects_answers += check_answer(questions.get(key), guess)
    
    question_num += 1
  print("----------- Quiz Game / Results -------------")
  print("Score Rate:", math.floor((corrects_answers/len(questions))*100), "% (", corrects_answers, "/", len(questions), ")")
  play_again = input("Would you like play again? (yes or no): ")
  if play_again.lower() == "yes" or play_again.lower() == 'y':
    new_quiz()
  
def check_answer(answer, guess):
  if answer == guess.upper():
    print("Correct!!")
    return 1
  else:
    print("Wrong!!")
    return 0


def edit_mode():
  print("----------- Quiz Game / Edit -------------")
  question = input("Add question (+) / Remove question (-): ")
  if question == '+':
    print("Teste")
  elif question == '-':
    print("Teste")

with open("questions.json") as questions:
  file_json = json.load(questions)
  questions = file_json["questions"]
  options = file_json["options"]


# Quiz game - Home
print("----------- Quiz Game / Home -------------")
mode = input("What do you want? (P/Play or E/Edit): ")
if mode.lower() == 'e' or mode.lower() == 'edit':
  edit_mode()
elif mode.lower() == 'p' or mode.lower() == 'play':
  new_quiz()
