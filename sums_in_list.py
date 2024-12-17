num = 1
sums=0
average=-1
lists=[]
while(num!=0):
    num=int(input("Enter NUmber"))
    sums=sums+num
    lists.append(num+num)
    average=average+1
print("sum of number",sums)
print('Average number',sums/average)
lists.pop()
print('Sums in  a list',lists)
