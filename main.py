#Create Function for Addition
def add(num1, num2):
  return num1 + num2

#Create Function for Substraction
def substract(num1, num2):
  return num1 - num2

#Create function for Multiplication
def multiply(num1, num2):
  return num1 * num2

#Create function for dividing
def divide(num1, num2):
  return num1 - num2

#Ask user to input 2 numbers the calculate

print("Welcome to simple calculator")
print()
print("Select A Type of Calculation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Divide")

print()
while True:
  #Accept input from user
  choice = input("Make your choice (1/2/3/4): ")

  #Check if choice of four options
  if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter Your First Number: "))
    num2 = float(input("Enter Your Second Number: "))

    if choice == '1':
      print(num1, " + ", num2, " = ", add(num1, num2))
    
    elif choice == '2':
      print(num1, " - ", num2, " = ", substract(num1, num2))
    
    elif choice == '3':
      print(num1, " * ", num2, " = ", multiply(num1, num2))
    
    elif choice == '4':
      print(num1, " : ", num2, " = ", divide(num1, num2))
    
    # Check Again if user wants to another calculation
    # Break the WHILE LOOP if the answer No 

    next_calculation = input("Let's do next calculation? (Yes/No): ")
    if next_calculation == "No":
      break

  else:
    print("It is wrong input")



