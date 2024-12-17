array_sample =[20,20,25,2,4,3]#creating an array
print(array_sample)
print(array_sample[1])#access
array_sample[1]=45#modify
print(array_sample)
array_sample.append(5)#add element
print("added",array_sample)
array_sample.remove(5)#remove by element name
print(array_sample)
del array_sample[1]#delete by index number
print(array_sample)
print(len(array_sample))#length of array
print(array_sample[0:3])#slice using index from x to x
reversed_list = array_sample[0:3:1]#reverse
print(reversed_list)
array_sample.sort()
print(array_sample)