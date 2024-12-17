my_list = [10,10,20,65,60,30,30,40,40,30]

index = 0
while index < len(my_list):
    if my_list[index] in my_list[:index] :
        my_list.remove(my_list[index])
    else:
        index += 1

print(my_list)
