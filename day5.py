'''
5. Practice Tasks – Day 5

Write a function square(num) that returns the square of a number.

Write a function is_even(num) that returns True if the number is even, else False.

Write a function largest_in_list(lst) that returns the largest number from a list.

Write a function greet_user(name, age) that prints:
👉 Hello Vinay, you are 28 years old.
'''

num=int(input("Enter any number:"))
def square(num):
    return num*num
result=square(num)

print(result)



def is_even(num):
    return num%2==0
if is_even(num):
    print(True)
else:
    print(False)
    
lst=[10,5,99,3]
def largest_in_list(lst):
    """
    Returns the largest number in the list.
    """
    if not lst:
        return None
    largest=lst[0]
    for i in lst:
        if i > largest:
            largest=i
    return largest
print(largest_in_list(lst))


def greet_user(name, age):
    print(f"Hello {name} you are {age} years old")

name=input("Enter the name:")
age=int(input("Enter the age:"))
greet_user(name, age)


def fact_num(a):
    result=1
    for x in range(1,a+1):
        result *= x

    return result
num=int(input("Enter nay num:"))
print(fact_num(num))
    
