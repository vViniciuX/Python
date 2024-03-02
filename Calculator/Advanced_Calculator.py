import math
from mathcalc import *

numbers = []

# Send operation for calcule
print("------- Advanced Calculation -------\n")
problem_input = input("Write the operation (Ex: 10+10, 20/20...): ")
print("")

# Calculation of expression
def Interpretation():
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
Interpretation()


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
      Error = 'Zero Division Error'
    except Exception as E:
      Error = E
  if len(numbers) == 1:
    return numbers[0]
  else:
    return Error

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
      return RootExtraction(number2, number1)
    case 'log':
      return math.log10(number2)

# Calculation Functions
def RootExtraction(rooting, index=2):
  decimal = 1
  resultRoot = rooting
  
  if index <= 0:
      return 'Undefined'
  
  while resultRoot ** index > rooting:
    resultRoot /= 1.002

  for _ in range(len(str(math.floor(resultRoot)))*70):
    if resultRoot ** index > rooting:
      resultRoot -= decimal
      decimal *= 0.1
    if resultRoot ** index < rooting:
      resultRoot += decimal
    if resultRoot ** index == rooting:
      return resultRoot
  print("Done")
  return resultRoot

# Send result
try:
  print(f"-- Result: {problem_input} → {ProblemSolving()}\n")
except:
  pass
  
  
