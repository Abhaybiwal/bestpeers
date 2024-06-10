row =int(input("enter number of rows"))

for i in range(0,row):
    for k in range(0,row-i):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print(" ")

for i in range(row,-1,-1):
    for k in range(0,row-i):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print(" ")


