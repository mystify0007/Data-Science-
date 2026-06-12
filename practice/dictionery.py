cars = {
    "model " : " modern",
    "price" : "$300,000",
    "name" : "ferrari"
}
for x in cars :
    if x == "price":
        continue
    print(x)
print(cars)
print(cars["model "])
print(len(cars))

x1 =["anup","beni","kushal"]
y1 = ["karki","pahadi","shrestha"]
for x in x1 :
    for y in y1:
        print(x,y)

# for x in range(3,30,3):
    # print(x)