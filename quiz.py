
def new_game():
  question_num = 0
  guesses = []
  guess = ''
  for key in questions:
    print("-------------------------")
    print(key)
    for option in options[question_num]:
      print(option)
    guess = input("\nDigit the answer (A, B, C or D): ")
    guesses[question_num] = guess
    
    question_num += 1
  print(guesses)

def check_guess(guess):
  print("Test")
    

questions = {
  "When was Python launched? ": "A",
  "How much is 2+2": "D"
}

options = [
  ["A. 1991", "B. 1992", "C. 1990", "D. 1985"],
  ["A. 1", "B. 3", "C. 2", "D. 4"]
]

new_game()
