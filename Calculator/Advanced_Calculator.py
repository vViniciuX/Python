
print("--------- Advanced Calculation ---------\n")
operation = input("----- Write the operation (Ex: 10+10, 20/20...): -----\n")
print("")
    
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
    print('Is Number')
  except:
    numbers.append(int(current_var))
    operator = var
    base = 0
    current_var = 0
    print('Is NaN')
  print('- var: {0}, base: {1}'.format(current_var, base))
  
numbers.append(int(current_var))
print(numbers)

try:
  result = WhichOperator(numbers[0], operator, numbers[1])
except: 
  print ("---- Error: {0}\n".format(numbers))
else:
  print("---- Conclusion: {0} = {1}\n".format(operation, result))
finally:
  print ("----- End -----")
  
  
