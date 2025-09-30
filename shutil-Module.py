import shutil,os,sys
with open("sample.txt","w") as f:
    f.write("This is a sample file for shutil module demonstration.")   

dir="backup"
if os.path.exists(dir):
    print("Directory already exists")
    shutil.copy("sample.txt","backup/sample.txt")
else:
    os.mkdir(dir)
    print("Directory created")
    shutil.copy("sample.txt","backup/sample.txt")
    print("File copied successfully")



dir1="archive"
with open("backup/temp.txt","w") as log:
    log.write("This is a temporary log file.")
if os.path.exists(dir1):
    print("Directory already exists")
    shutil.move("backup/temp.txt","archive/temp.txt")
else:
    os.mkdir(dir1)
    print("Directory created")
    shutil.move("backup/temp.txt","archive/temp.txt")
    print("File moved successfully")

dir3="old_logs"
if os.path.exists(dir3):
    print("Directory already exists")
    shutil.rmtree("old_logs")
    print("Directory deleted successfully")
else:
    os.mkdir(dir3)
    print("Directory created")
    shutil.rmtree("old_logs")
    print("Directory deleted successfully")