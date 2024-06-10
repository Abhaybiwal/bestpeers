row=int(input("Enter number of row"))
asci=65
for i in range(0,row):
    for j in range(0,i+1):
        print(chr(j+asci),end="")
    print()

    # Output
# Enter number of row5
# A
# AB
# ABC
# ABCD
# ABCDE