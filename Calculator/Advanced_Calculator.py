import math
from mathcalc import *

numbers = []
# Send operation for calcule
def Initiate():
  print(f"{' Advanced Calculation ':=^60}\n")
  problem_input = input("Write the operation (Ex: 10+10, 20/20...): ")
  print("")
  Interpretation(problem_input)
  print(f"{'Result':>10}: {problem_input} → {ProblemSolving()}\n")
  
# Calculation of expression
def Interpretation(problem_input):
  new_char = ""
  new_op = ""
  for char in problem_input+' ':
    try:
      int(char)
      new_char += char
      if new_op != '':
        numbers.append(new_op)
        new_op = ''
    except:
      try:
        numbers.append(int(new_char))
        new_char = ''
      except:
        pass
      new_op += char

def ProblemSolving():
  OperationsList = ['+','-','*','/','**','v', 'log', '(', ')']
  OperationsList.reverse()
  
  for i in OperationsList:
    try:
        while numbers.count(i) > 0:
          PosNumber = numbers.index(i)
          numbers[PosNumber-1] = WhichOperation(numbers[PosNumber], numbers[PosNumber-1], numbers[PosNumber+1])
          if len(numbers) > 2:
            del numbers[PosNumber]
          if len(numbers) > 1:
            del numbers[PosNumber]
    except ZeroDivisionError: 
      return 'ZeroDivisionError'
    except Exception as E:
      return E
  if len(numbers) == 1:
    return numbers[0]
  else:
    return 'Operation Error'

# Function WhichOperation for calcule result
def WhichOperation(operator, number1, number2):
  match operator:
    case '+':
      return number1 + number2
    case '-':
      return number1 - number2
    case '*':
      return number1 * number2
    case '/':
      return number1 / number2
    case '**':
      return number1 ** number2
    case 'v':
      return number2**(1/number1)
    case 'log':
      return math.log10(number2)

# Send result
Initiate()
  
  
