row =int(input("Enter number of rows: "))

for i in range(1,1+row):
    for l in range(0,row-i):
        print(" ",end="")
    for j in range(i,1,-1):
        print(j,end="")
    for k in range(1,i+1):
        print(k,end="")
    print()

for i in range(row-1,0,-1):
    for l in range(0,row-i):
        print(" ",end="")
    for j in range(i,1,-1):
        print(j,end="")
    for k in range(1,i+1):
        print(k,end="")
    print()

# Enter number of rows: 4
#    1
#   212
#  32123
# 4321234
#  32123
#   212
#    1
