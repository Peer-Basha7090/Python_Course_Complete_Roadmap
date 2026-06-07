
name = "Basha"
age= 25
city="banglore"
print(f"Hello {name} , your age is {age} and your city is {city}")


a=10
b=20
sum= a+b
print(sum)

a =7.9
print(type(a))

x,y,z=5,6,7
print(f"x = {x} , y = {y} , z = {z}")


m=10
n=20
print(f"m = {m} , n = {n} ")
t=m
m=n
n=t
print(f"m = {m} , n = {n} ")

print(" Type Convertions ")
print(" Integer to float")

p =10
q=float(p)
print(q,type(q))

print(" float to Integer")

p =10.10
q=int(p)
print(q,type(q))


print(" Integer to string")

p =10
q=str(p)
print(q,type(q))



print("  string to Integer")

p ="500"
q=int(p)
print(q,type(q))



print("  Boolean to Integer")

p=False
q=int(p)
print(q,type(q))



print("Real problems ")

print("Create a local variable inside a function and try accessing it outside. ")

def var():
    s=10
    print(f"Local Variable {s}")

var()



print("Create a global variable outside  function and accessing . ")
global_name="Basha"
def var():
    print(f"global Variable = {global_name}")

var()

print("Create a global variable outside  function and modify that and print . ")
global_name="Basha"
def var():
    global_name="Peer"
    print(f"global Variable = {global_name}")

var()



print("Create three nested functions,Observe how Python searches for variables.")

x = "Global"

def outer():
    x = "Outer"

    def middle():
        x = "Middle" # reassign the value 

        def inner():
            print(x)  # Searches for x

        inner()

    middle()

outer()


print("Use id() to compare two variable")

s=10
t=s
print("s = ",s,id(s))
print("t= ",t,id(t))
