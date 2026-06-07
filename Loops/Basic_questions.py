#Print 1 to 10 numbers
print("1 to 10 numbers")
for i in range(1,11):
    print(i,end=" ")

print()

#print Even Numbers from 1 to 100
print("Even Numbers from 1 to 100")
for i in range(1,101):
    if i % 2 == 0:
        print(i,end=" ")

print()

#print First N natural Numbers
print("First N natural Numbers")
n=int(input("Enter a Number "))
sum =0
for i in range(1,n+1):
    sum += i
print(sum)

print()

# Multiplication Table 
m = int(input("ENter n number"))
n = int(input("ENter m number"))
for s in range (m,n+1):
    for i in range(1,11):
        print(f"{s} * {i} = {s*i}")

    print()

#Factorial Number
print("Factorial Number")
n =int(input("Enter one Number"))
fact=1
for i in range(1,n+1):
    fact *= i
print(fact)


#Reverse a Number
print("Reverse a Number")
n=int(input("Enter a Number "))
reverse=0
for i in range(len(str(n))):
    digits = n%10
    reverse= reverse * 10 + digits
    n = n // 10

print(reverse)


# Count digits
n=int(input("ENter a numbers"))
count = 0
for i in range(len(str(n))):
    count += 1
print(count)


# while Loop

#Print number from 1 to 10
i=1
while(i<=10):
    print(i,end=" ")
    i+=1

print()

#print 10 to 1
i=10
while i >=0 :
     print(i,end=" ")
     i -=1

print()
#Print EVen Numbers
print(" Even Numbers")
i=1
while i <=100 :
    if i % 2 == 0:
        print(i,end = " ")
    i += 1
    
print()
#Print Odd Numbers
print(" odd Numbers")
i=1
while i <=100 :
    if i % 2 != 0:
        print(i,end = " ")
    i += 1


#SUM NUMBERS UNTILL USER ENTERS 0
sum = 0
while True :
    n = int(input("Enter a Number"))

    if n == 0 :
        break

    sum += n

print("\nsum = ",sum)


#GUESS THE NUMBER
import random

Number=random.randint(1,10)

while True :
    guess=int(input("Guess a Number = "))

    if guess==Number :
        print("Congracts You Guessed Right Number..Thank You Have a Nice Day..")
        break
    print("Sry!!!!, Wrong Number , Try one more Time")



