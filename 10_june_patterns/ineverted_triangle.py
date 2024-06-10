row = int(input("Enter number of row "))

for i in range(row-1,-1,-1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

# Enter number of row 5
#  *********
#   *******
#    *****
#     ***
#      *
