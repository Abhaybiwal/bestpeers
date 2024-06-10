row =int(input("enter number of rows"))

for i in range(0,row):
    for j in range(0,row):
        if j==0 or i==row-1:
            print("* ",end="")
        else:
            print(" ",end="")
    print("")

# enter number of rows5
# *     
# *     
# *     
# *     
# * * * * * 

