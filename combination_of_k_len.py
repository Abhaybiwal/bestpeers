# program to find all the Combinations in the list with the given condition

def combination(k,processed_list,input_list):
    if len(processed_list)==k:
        listp=[]
        listp.append(processed_list)
        return listp
    
    ch=input_list[0]

    ans=[]

    for i in range(0,len(processed_list)+1):
        f=processed_list[0:i]
        s=processed_list[i:len(processed_list)]
        ans.extend(combination(k,f+ch+s,input_list[1:]))

    return ans

print(combination(3 ,"",["a","b","c"]))



