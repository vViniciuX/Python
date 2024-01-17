# Send operation for calcule
print("--------- Advanced Calculation ---------\n")
operation = input("----- Write the operation (Ex: 10+10, 20/20...): -----\n")
print("")

# Function WhichOperation for calcule result
def WhichOperator(number1, operator, number2):
  match operator:
    case '+':
      return number1 + number2
    case '-':
      return number1 - number2
    case '*':
      return number1 * number2
    case '/':
      return number1 / number2
    case '^':
      return Exponentiation(number1, number2)
    case 'v':
      return Root_Extraction(number1, number2)

# Calculation Functions
def Exponentiation(number, exponent):
  x = 1
  for _ in range(exponent):
    x = x * number
  return x

def Root_Extraction(index, rooting):
  Base = 1
  isRoot = 1
  resultRoot = 1
  
  for _ in range(rooting*24):
    for _ in range(index):
      isRoot *= resultRoot
      
    if isRoot > rooting:
      resultRoot -= Base
      Base *= 0.1
    elif index == 0:
      return 'Undefined'
    elif isRoot < rooting:
      resultRoot += Base
    elif isRoot == rooting:
      return resultRoot
    isRoot = 1
  return resultRoot

# Calculation of expression
current_var = 0
base = 0
numbers = []
operator = ''

for var in operation:
  try:
    if int(var) < 10 and int(var) > -1:
      base += 1
      if base > 1:
        current_var = current_var * 10
      current_var += int(var)
  except:
    numbers.append(int(current_var))
    operator = var
    base = 0
    current_var = 0
numbers.append(int(current_var))

# Send result
try:
  result = WhichOperator(numbers[0], operator, numbers[1])
except: 
  print ("---- Error: {0}\n".format(numbers))
else:
  print("---- Conclusion: {0} = {1}\n".format(operation, result))
finally:
  print ("----- End -----")
  
  
