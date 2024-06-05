# Python program to find the Strongest Neighbour

def strongestadjacentneibour(input_list):
    list2=[]
    for i in range(1,len(input_list)):
        if input_list[i] > input_list[i-1]:
            list2.append(input_list[i])
        else:
            list2.append(input_list[i-1])

    return print(list2)


test_list=[1, 2, 2, 3, 4, 5]

strongestadjacentneibour(test_list)

test_list=[5, 5]

strongestadjacentneibour(test_list)


