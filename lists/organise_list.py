#Organising a list

car = ["benz", "bmw", "audi", "nano", "tiago"]
print(car)

# sort
car.sort()
print("Sort: ", car)

#reverse sort
car.sort(reverse=True)
print("Reverse Sort: ",car)

#printable sort
print("Temp Sort: ", sorted(car))

#reverse
car.reverse()
print("Reverse: ",car)

#length of list
print(len(car))

print(car[4])