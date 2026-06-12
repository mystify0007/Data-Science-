list_a = [1,2,3,"tesla",0]
print(list_a)

list_b = ["ps5","ps4","$500"]
list_a.extend(list_b)

print(list_a)
list_a.extend('MacBook')

list_a.extend(range(3,8))
print(list_a)

# for i in range(11,1000,11):
#     print(i)


list_c=["mango","apple","banana"]
list_c.insert(1,"kiwi") # value index anusar halna milxa
print(list_c)

index = list_c.index("apple") # first find the index then remove 
print(index)

list_c.pop(2)
print(list_c)

#dublicates
e_list = [1,2,3,4,6,7,8,9,5,3,4,5,7,8,9]
no_dublicates = list (set(e_list)) #type casting 
print(no_dublicates)


# list_c.pop() # always from last same as append 
# print(list_c) 
 
#remove 
#list_a[1,3,4,5,6,7,7,4]
#.remove(4) this removes all the 4 not the index 

list_d=[1,2,3,4,6,7,8,9,5,3]
# complete this
# if(list_d.vlaue != '10'):
#     print("error ")
# else:
#     list_d.remove(4)
#     print(list_d)
# list_d.remove(10) this throws error 

list_d.sort()
print(list_d)

print(list_d[0])
print(list_d[-1])
print(list_d[3:4])
print(list_d[::2]) # list_d[start: end : step]
print(list_d[::]) # all

nested_list=[[1,2,3],[4,5,],[6,7,8]]
nested_list[1]
print(nested_list)

for items in nested_list:
    print(items)
    for item in items:
        print(item)

# list_d=[1,2,3,4,6,7,8,9,5,3] 


d = [1,2,3,4,6,7,8,9,5,3] 

#even 
# c =[]
# for item in d :
#     if item%2 == 0:
#         d.append(item)
#     print(c)

b = [item for item in d if item%2 == 0 ] # (any expressioin for in )
print(b)

a = [1,3,5,4,6]
# traditional way f = [item*item*item for item in a]
f = [item**2 for item in a if item%2 == 0] 
print(f)

