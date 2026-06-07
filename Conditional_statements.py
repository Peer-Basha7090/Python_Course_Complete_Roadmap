#Positive or negative
print("Print Positive or negative numer")

#a=int(input("Enter a Number = "))
a=10
if a > 0:
    print(f"Value is {a} so it is Positive ")
else:
    print(f"Value is {a} so it is Negative ")


# Even  or odd
print(" Find Even or Odd Numer ")

a=int(input("Enter a Number = "))
if a  % 2 == 0:
    print("Even Number")
else:
    print("Odd number")

#Largest of 2 Numbers
print("Largest of 2 numbers")

x=int(input("Enter x   value= "))
y=int(input("Enter y value = "))
print(f"x value = {x} and y value = {y}")
if x > y :
   print("X is greater")
else:
    print("Y is greater")


#Largest of 3 Numbers
print("Largest of 3 numbers")

x=int(input("Enter x value = "))
y=int(input("Enter y value = "))
z=int(input("Enter z value = "))

print(f"x value = {x} and y value = {y}")
if x > y  and x > z:
   print("X is greater")
elif y > x  and y > z:
    print("Y is greater")
else:
    print("Z is greater")

# Leap Year
year = int(input("Enter a year "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    print("Leap year")
else :
    print("Not Leap year") 


#Find Grades

print("print grades")
marks=int(input("Enter marks = "))
if marks >= 90 :
    print("A grade")
elif marks >= 75 and marks <= 89 :
    print("B grade")
elif marks >= 60 and marks <= 74 :
    print("c grade")
else :
    print("Fail") 


#Voting Eligiblity

print("Voting Eligiblity")
age =int(input("Enter age = "))
if age >= 18 :
    print("Eligible")
else :
    print("Not Eligible") 

#Calculator

print("Calculator using sign")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Division by zero!")

else:
    print("Invalid operator!")


