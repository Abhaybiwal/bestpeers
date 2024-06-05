# show elements only once in a list
l=[1,2,34,52,1,2,34]
unique=[]
unicount=0;

for i in l:
    if i not in unique:
        unicount+=1
        unique.append(i)

print(unique,unicount)
