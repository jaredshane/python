showroom = set()

showroom.add('Tesla Model 3')
showroom.add('Chevy Impala')
showroom.add('VW Jetta')
showroom.add('Mitsubishi Eclipse')

# print(len(showroom))

showroom.add('VW Jetta')

# print(showroom)

new_showroom = { "Ford Mustang", "Big Truck"}

showroom.update(new_showroom)

# print(showroom)

showroom.discard("Big Truck")

# print(showroom)

junkyard = { "Ford Mustang", "Crappy Car", "Really crappy car"}

# print(showroom.intersection(junkyard))

showroom = showroom.union(junkyard)
print(showroom)

showroom.discard("Really crappy car")
print(showroom)