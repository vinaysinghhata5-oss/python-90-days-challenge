'''
📝 Your Day 7 Task

Create a dictionary of 5 students with their marks. Print who scored highest.

Create a set of numbers from a list with duplicates and show only unique values.

Parse a log file into dictionary format like:

'''


student={"vinay": "99",
         
         "rohit": "50",
          "ajay": "80",
          "pankaj": "81",
          "amar": "100"
         
         
         }
topper=max(student,key=student.get)
print(f"the higest marks is {topper} is {student[topper]}")   


a={1,3,4,5,5}
print(a)


logs={"level": "ERROR",
      
  "date": "2025-09-25",
  "message": "Connection failed",
  "server": "server01"
}
for key,value in logs.items():
    print(key,":",value)


'''
Q1. Merge Two Dictionaries

'''

dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}
dict2.update(dict1)


print(dict2)

'''
Q2. Common Elements in Sets

'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print(set1.intersection(set2))


'''
Q3. Word Frequency Counter

Given a string:
'''
text = "devops with python python with automation"

# Step 1: Split the string into words
words = text.split()

# Step 2: Create an empty dictionary
frequency = {}

# Step 3: Count each word
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Step 4: Print the result
print(frequency)


'''
Q5. Remove Duplicates from List Using Set
'''
nums = [1,2,3,2,4,5,1,6,3]
c=list(set(nums))
print(c)