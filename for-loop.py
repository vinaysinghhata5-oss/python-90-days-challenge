'''
🔹 Basic for loop questions

Print numbers from 1 to 20 using a for loop.

Print only even numbers between 1 and 50.

Print the square of numbers from 1 to 10.

Calculate the sum of numbers from 1 to 100.

Find the factorial of a number (e.g., 5! = 1×2×3×4×5).
'''
'''
for i in range(1,21):
    print(i)

for i in range(1,50):
    if i %2==0:
       print(i)
y=0
for a in range(1,11):
    y=a*a
    print(y)
    '''

for i in range(1,5):
       for j in range(1,i+1):
         print(j, end=" ")
       print()


'''
Print the multiplication table of 7.
'''
 
     
numbers = [10, 25, 7, 92, 56]
low=numbers[0]
for a in numbers:
     if a < low:
          low=a
print(low)
     