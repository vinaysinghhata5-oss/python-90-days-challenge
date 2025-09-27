'''
📝 Day 8 Practice Tasks

Create a file devops.txt and write 3 lines about why you are learning DevOps.

Read the file and print its content.

Count how many lines are in the file.

Append "Learning Python daily!" to the file.

Read again and show updated content.
'''

with open("devops.txt","w") as f:
    f.write("i learn python for devops for job")
    f.write("\nfor automation")
    f.write("\ni learn python AI")
with open("devops.txt","r") as f:
    for line in f:
        print(line.strip())
c=0
with open("devops.txt","r") as f:
    for line in f:
        c+=1
print(c)

with open("devops.txt","a") as f:
    f.write("\nLearning Python daily!")
    f.close()