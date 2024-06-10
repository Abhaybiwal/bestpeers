row =int(input("enter number of rows: "))

for i in range(0,row):
    for k in range(0,row-i):
        print(" ",end="")
    for j in range(0,i+1):
        if j==0 or j==i or i==row//2:
            print("* ",end="")
        else:
            print("  ",end="")
    print(" ")

# enter number of rows: 6
#       *  
#      * *  
#     *   *  
#    * * * *  
#   *       *  
#  *         *  