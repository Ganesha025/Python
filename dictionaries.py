# Creating a dictionary
person = {
    'name': 'John',
    'age': 30,
    'job': 'Engineer'
}

#check
age='age' in person
print(age)

#Duplicate
dup=person.copy()
print(dup)
#Accessing
print(person["name"])#it doesn' return anything
print(person.get("age"))# it return when value not found

#Updating Value
person["name"]="Savage"
print(person['name'])
person["Gender"]='Male'
print(person)

#Remove 
person.pop('job')#usinh pop()
print(person)
test=person.popitem()#using popitem,it popup last key with value
print(test)
empty=person.clear()#clear all
print(empty)
print("hello")