cars = ("bmw", "audi", "lambo")
engine = list(cars)

engine[1] = "modern"
cars = tuple(engine)
print(cars)


cars2 = ("ferrari",)
cars += cars2
print(cars)