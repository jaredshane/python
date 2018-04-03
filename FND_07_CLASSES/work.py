class Zoo:
	'''Contains methods for maintaining a Zoo

    Methods:
    --------
    build_habitat
    sell_family_ticket
    purchase_animal
    '''
	def __init__(self, name):
		self.zoo_name = name
		self.animals = dict()
		self.habitats = set()
		self.visitors = list()

	def build_habitat(self, name, type): 
		'''Adds tuples to the habitats set in the format (name, type)

        Method arguments:
        -----------------
        name(string) -- The marketing name of the habitat
        type(string) -- The type of habitat (e.g. Saltwater, Savanna, Swamp, etc.)
        '''
		self.habitats.add((name, type))

	def sell_family_ticket(self, family):
		'''Adds an entire family to the list of vistors
			Method argument:
			----------------
			family(list) -- A list of people in the family of visitors
			'''
		self.visitors.extend(family)
	
	def purchase_animal(self, type, name):
		"""add an animal to the zoo
			Method arguments:
			------------------
			type(string) --- the type of animal to add
			name(string) --- the given name of the animal
			"""
		self.animals[name] = type

	def list_animals(self):
		"""Lists all the animals in the zoo
			 Method arguments:
        n/a
		"""
		[print(k + ' the ' + v) for k, v in self.animals.items()]

a_zoo = Zoo("Zoolandia")
a_zoo.purchase_animal("Tortoise", "Tommy")
a_zoo.list_animals()

a_zoo.list_animals.__doc__ # To view the docstring for the method

class Animal:
	def __init__(self, name = None, species = None):
		self.name = name
		self.species = species
		self.speed = 0
		self.legs = 0
	
	def get_name(self): 
		return self.name

	def walk(self):
		print("Parent class walk method")
		self.speed = self.speed + (0.1 * self.legs)

	def set_species(self, species):
		self.species = species

	def get_species(self):
		return self.species

	def __str__(self):
		return "%s is a %s" % (self.name, self.species)

class Dog(Animal):
	def __init__(self, name):
		Animal.__init__(name, "Dog")

	def walk(self):
		self.speed = self.speed + (0.2 * self.legs)