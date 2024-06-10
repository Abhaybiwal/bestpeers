row =int(input("Enter number of rows: "))

for i in range(row-1):
    for j in range(i+1):
        print("*",end="")
    for k in range(row-i):
        print("  ",end="")
    for l in range(i+1):
        print("*",end="")
    print()

for i in range(row-1,-1,-1):
    for j in range(i+1):
        print("*",end="")
    for k in range(row-i):
        print("  ",end="")
    for l in range(i+1):
        print("*",end="")
    print()

#Enter number of rows: 5
# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *          