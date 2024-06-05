# Test if List contains elements in Range

def eleInrange(list_ele,element,Start,End):
    if element in list_ele[start:end+1]:
        print(f"{element} is present in a range {Start} to {End}")
    else:
        print(f"{element} is not present in a range {Start} to {End}")

list_input= [4, 5, 6, 7, 3, 9]
start=1
end=2
element=7
eleInrange(list_input,element,start,end)