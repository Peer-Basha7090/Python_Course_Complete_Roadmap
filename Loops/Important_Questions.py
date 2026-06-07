"""#Prime Number
print("Prime Number")
n = int(input("Enter a Number = "))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1

if count == 2 :
    print("Prime Number")
else :
    print("Not a Prime Number")


#Print Prime Numbers From 1 to 100
for i in range(1,100+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1

    if count == 2 :
        print(i,end=" ")

#Fibonacci Series
num=int(input("Enter a Number.."))
x=0
y=1
print(f"{x} {y}",end =" ")
for i in range(2,num) :
    z=x+y
    print(z,end=" ")
    x=y
    y=z
print()

#Armstrong Number
num=int(input("Enter a Number = "))#153
temp = num
power=len(str(num)) #length = 3
arm = 0
while num > 0 :
     digit = num % 10
     arm += digit ** power
     num = num // 10
if temp == arm:
    print("Armstrong Number ..")
else:
    print("Not an Armstrong Number") """

#Palindrome
n=int(input("Enter a Number "))
temp=n
reverse=0
for i in range(len(str(n))):
    digits = n%10
    reverse= reverse * 10 + digits
    n = n // 10

if temp == reverse :
    print("Palindrome")
else:
    print("Not a Palindrome")


# Strong Number

num = int(input("Enter Number = "))

temp = num

strong = 0

while num > 0:

    digit = num % 10

    fact = 1

    for i in range(1, digit+1):

        fact *= i

    strong += fact

    num = num // 10

if temp == strong:

    print("Strong Number")

else:

    print("Not Strong Number")
