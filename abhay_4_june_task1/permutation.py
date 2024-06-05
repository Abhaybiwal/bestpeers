# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.

def combibation(processed_list,input_list):
    if len(input_list)==0:
        listp=[]
        listp.append(processed_list)
        # print(processed_list)
        return listp
    
    ch=input_list[0]

    # local to this call
    ans=[]

    for i in range(0,len(processed_list)+1):
        f=processed_list[0:i]
        # print(f)
        s=processed_list[i:len(processed_list)]
        # print(s)
        ans.extend(combibation(f+ch+s,input_list[1:]))

    return ans


print(combibation("",["a","b","c"]))