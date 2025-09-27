'''
Q1. Write a function to check if a number is even or odd.

Function should take 1 parameter (a number).

Return "Even" or "Odd"
'''

def even_odd(a):
    return a%2==0 
a=int(input("Enter any number:"))
even=even_odd(a)
if even_odd(a):
    print(f"{a} is even")
else:
    print(f"{a} is odd")



