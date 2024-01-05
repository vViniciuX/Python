
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
  final((corrects_answers/len(questions))*100)
  

def check_answer(answer, guess):
  if answer == guess.upper():
    print("Correct!!")
    return 1
  else:
    print("Wrong!!")
    return 0
  
  
def final(corrects_answers):
  print("-------------------------")
  print("Score Rate:", corrects_answers, "%")
  play_again = input("Would you like play again? (yes or no): ")
  if play_again.lower() == "yes" or play_again.lower() == 'y':
    new_quiz()
    
questions = {
  "When was Python launched? ": "A",
  "Who created Python?": "B",
  "How much is 2+2": "D"
}

options = [
  ["A. 1991", "B. 1992", "C. 1990", "D. 1985"],
  ["A. Anders Hejlsberg", "B. Guido van Rossum", "C. Dennis Ritchie", "D. James Gosling"],
  ["A. 1", "B. 3", "C. 2", "D. 4"]
]

new_quiz()
