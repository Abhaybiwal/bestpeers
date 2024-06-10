row =int(input("Enter number of rows: "))

num=1

for i in range(row):
    for j in range(i+1):
        if i==j:
            print(num,end="")
        else:
            print(str(num)+"*",end="")
        num+=1
    print()

num=num-row
for i in range(row,0,-1):
    for j in range(1,i+1):
        if i==j:
            print(num,end="")
        else:
            print(str(num)+"*",end="")
        num+=1
    num=(num+1)-2*i
    print()

#Enter number of rows: 4
# 1
# 2*3
# 4*5*6
# 7*8*9*10
# 7*8*9*10
# 4*5*6
# 2*3
# 1