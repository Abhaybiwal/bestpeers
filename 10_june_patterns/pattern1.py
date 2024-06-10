row =int(input("enter number of rows"))

for i in range(row-1,-1,-1):
    for j in range(0,i+1):
        print("*",end="")
    for k in range(row-i):
        print("  ",end="")
    for l in range(0,i+1):
        print("*",end="")
    print()
# enter number of rows5
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *