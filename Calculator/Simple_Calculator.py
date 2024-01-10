def Calculate(number1, operator, number2):
  print(number1 +operator +number2+'=')
  match operator:
    case '+':
      print(int(number1)+int(number2))
    case '-':
      print(int(number1)+int(number2))
    case '*':
      print(int(number1)+int(number2))
    case '/':
      print(int(number1)+int(number2))

number1 = input("Number 1: ")
operator = input("Operator: ")
number2 = input("Number 2: ")

Calculate(number1, operator, number2)
    
  