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

print(showroom)