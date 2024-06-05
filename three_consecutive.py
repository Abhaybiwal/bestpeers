# program to check if the list contains three consecutive common numbers in

def three_consecutive(list_input):
    for i in range(0,len(list_input)):
        if (i<=(len(list_input)-3)) and (list_input[i]==list_input[i+1] and list_input[i]==list_input[i+2]):
            print(list_input[i])


input_list1=[4, 5, 5, 5, 3, 8]

three_consecutive(input_list1)

input_list2=[1, 1, 1, 64, 23, 64, 22, 22, 22]

three_consecutive(input_list2)