x=["403","500","502"]

def error_count(file_name):
    try:
        with open(file_name,"r") as f:
            for line in f:
                if x in line:
                #if any(code in line for code in ["403","500","502"]):
                    print(line)


    except FileNotFoundError:
        print()
    except Exception as e:
        print()
error_count("nginx.log")