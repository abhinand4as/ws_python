fruits = ["mango","apple","banana","grape", "apple"]
print(fruits)
# print(type(fruits))
# print(fruits[-2])
fruits[0] = "orange"
print(fruits)
fruits.append("mango")
print(fruits)
fruits.insert(1, "guava")
print(fruits)
fruits.pop()
print(fruits)
del fruits[3]
print(fruits)
fruits.remove("apple")
print(fruits)