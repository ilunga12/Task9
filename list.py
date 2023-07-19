

n = int(input("enter the elements:"))
list=[]
for i in range(0,n):
    element=int(input())
    list.append(element)
print("the list is:",list)
unique=[]
duplicate=[]
for element in list:
    if element not in unique:
        unique.append(element)
    elif element not  in duplicate:
        duplicate.append(element)
print("the unique list is:",unique)
print("the duplicate list is",duplicate)