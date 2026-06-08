n = int(input("Enter a number = " ))
for i in range(n):
   for j in range(i+1):
       print("*",end=" ")
   print()



m = int(input("Enter a number = " ))
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()