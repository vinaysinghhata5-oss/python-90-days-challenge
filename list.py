'''
Create a list of 10 numbers and print only the even numbers.
'''

num=[10,7,8,4,3,77,33,23,89]
for i in num:
    if i%2==0:
        print(f"{i} is even number")



'''
Reverse a list without using the reverse() function.
'''
a=[10,7,8,4,3,77,33,23,89]
b=[]
for x in a:
    b.insert(0,x)
print(b)



'''
Count how many times a number appears in a list.
'''
a=[10,7,8,4,3,33,33,23,10]
q=0
for c in a:
    q=a.count(c)
    print(f"{c} is appear {q}")


'''
Merge two lists into a single list.
'''
m=[10,7,8,4,3,33,33,23,10]
n=[1,4,0,0,100]
for t in m:
    n.append(t)
print(n)

s=[]
for j in m:
  if j not in s:
      s.append(j)
print(s)


'''
Sort a list in ascending order without using sort() (hint: use loops).
'''
m=[10,7,8,4,3,33,33,23,10]
for u in range(len(m)):
    for k in range(0,len(m)-u-1):
       if m[k] < m[k+1]:
          m[k],m[k+1] = m[k+1],m[k]
print(m)
'''

Take a list of strings and print the longest string.
'''

str=["vinay","ksusksu","jskskdiuaaa","aaa"]
l=str[0]
for w in str:
    if len(w) > len(l):
       l=w
print(l)

