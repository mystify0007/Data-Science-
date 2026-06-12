mylist = ["Apple", "banana", "grape", "watermelon", "kiwi", "dragon fruit"]
print(mylist[-1] ,mylist[-2])
print(mylist[2:4])
print(mylist[:4])
print(mylist[2:])
print(mylist[-4:-1])
mylist[1:3] = ["chiya seed", " pumpkin seed"]
print(mylist)
mylist.insert(2,"angur")
print(mylist)
mylist.append("kera")
print(mylist)
secondlist = ["coke", "fanta", "sprite"]
mylist.extend(secondlist)
print(mylist)
mylist.remove("kiwi")
print(mylist)
mylist.pop(2)
print(mylist)
del mylist[3]
print(mylist)
print(len(mylist))
mylist.clear()
print(mylist)
# this throws error as the list has been deleted
# del mylist
# print(mylist)

# tuples

mytuple = ("one", "two", "three", "four", "one")
print(mytuple)

mytuple= ("hello","this is hello ")
print(mytuple)

print(type(tuple))
tuple2 =("hello")
print(type(tuple2))

x = ("hello twiace",)
tuple += x
print(tuple)