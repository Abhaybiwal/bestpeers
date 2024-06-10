row =int(input("Enter number of rows: "))

for i in range(row-1,0,-1):
    for j in range(0,i+1):
        print("*",end="")
    print()

for i in range(row):
    for j in range(0,i+1):
        print("*",end="")
    print()

# Enter number of rows: 5
# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****