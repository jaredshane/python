flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip']
# large_flowers = ['a large ' + f for f in flowers]

# print(large_flowers)

large_flowers = list()
for f in flowers:
	large_flowers.append('a large ' + f)

# print(large_flowers)

family = { 'mother': 'Margaret', 'father': 'Reginald', 'sister': 'Jenny'}
my_family = {'my ' + k + ' is ' + v for (k,v) in family.items()}
# print(my_family)

possible_ratings = set(range(100))
funky_ratings = {r/2 for r in possible_ratings}
# print(funky_ratings)