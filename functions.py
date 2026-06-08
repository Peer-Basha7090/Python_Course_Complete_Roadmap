

#Write a function square(n) that returns the square of a number.
def sqare(a):
    return a * a
result=sqare(5)
print(result)

#Q2) Write a function is_even(n) that returns True if a number is even, otherwiseFalse.
def isEven(n):
    if n % 2 == 0 :
        return True
    else:
        return False
Even=isEven(8)
print(Even)

#Q3) Write a function maximum(a, b) that returns the larger of two numbers.

def maximum(a,b):
    if a > b :
        return a
    else :
        return b
max=maximum(10,25)
print(max)

#Q4) Write a function sum_n(n) that returns the sum of numbers from 1 to n.

def sum_n(n):
    sum=0
    for i in range(1,5+1):
        sum +=i
    return sum
result=sum_n(5)
print(result)

#Q5) Write a function factorial(n) using a loop.
def factorial(n):
    fact = 1
    for i in range (1,n+1):
        fact = fact * i
    return fact
result=factorial(5)
print(result)

#Q6) Write a function count_vowels(text) that counts vowels in a string.

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou" :
            count += 1
    return count
print(count_vowels("Hello"))
print(count_vowels("python"))
print(count_vowels("goodmorning"))
print(count_vowels("WELLCOME"))

#q7) Write a function reverse_string(text).
def reverse_string(text):
    reverse=""
    for ch in text:
        reverse = ch + reverse
    return reverse
print(reverse_string("Hello"))

def reverse_strings(text):
    return text[::-1]
print(reverse_strings("Bye"))

#Q8) Write a function is_palindrome(text).

def palindrome(text):
    text=text.lower()
    palindrome=text
    reverse=""
    for ch in text:
        reverse = ch + reverse

    if reverse == palindrome :
        return "palindrome"
    else:
        return "Not Palindrome"

print(palindrome("madam"))


#Q9) Write a function count_words(sentence).
def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("I love Python"))


#Q10)Write a function that prints all key-value pairs received through **kwargs.
''' Collect all extra keyword arguments into a dictionary.
    Why use **kwargs?
    Suppose you don't know how many arguments the user will pass.'''

def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display(name="John")
display(name="John", age=25)
display(name="John", age=25, city="Bangalore")
display(name="John", age=25, city="Bangalore", salary=50000)


# Q11) *args  it Collects extra positional arguments into a tuple.
def show(*args):
    print(args)

show(1, 2, 3, 4)

#Q12) use both *args and **kwargs
def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(10, 20, name="John", age=25)
