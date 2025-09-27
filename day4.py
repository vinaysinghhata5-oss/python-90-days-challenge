'''
📝 Day 4 Practice Tasks

Create a list of 5 colors and print them one by one.

Take 5 numbers from the user, store them in a list, and print their sum and average.

Write a program to find the largest and smallest number in a list.

Reverse a list without using .reverse() (hint: use loop).
'''
colour=["red","green","yellow","blue","pink"]
for i in colour:
    print(i)



numbers = list(map(int, input("Enter 5 numbers separated by space: ").split()))
sum=numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]
avg=sum/5
print(f"sum is:{sum} and average is {avg}")   

num1=[10,5,80,1]
y=num1[0]
z=num1[0]
for a in num1:
    if a > y:
        y=a
        print(f"{a} is larger number")
    if a < z:
        z=a
        print(f"{a} is smallest")

t=[10,5,80,1]
num2=[]
for b in t:
    num2.insert(0,b)
print(num2)