def Calculate(number1: int, operator: str, number2: int):
  match operator:
    case '+':
      return number1+number2
    case '-':
      return number1-number2
    case '*':
      return number1*number2
    case '/':
      return number1/number2

try:
  number1 = int(input("Number 1: "))
  operator = input("Operator: ")[0]
  number2 = int(input("Number 2: "))
  
  print(number1, operator, number2, '=')
  print(f'Result: {Calculate(number1, operator, number2)}')
except:
  print("Error")


    
  