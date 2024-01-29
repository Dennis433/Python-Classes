# Restaurant: Make a class called Restaurant. The init() method for Restaurant should
# store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant()
# that prints these two pieces of information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open.
class Resturant:
    '''A simple attempt to model a Resturant'''
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        ''''Describing the resturant type'''
        print(f'The name of this resturant is {self.resturant_name}, We have freshly baked {self.cuisine_type}')

    def open_resturant(self):
        ''''Indicates that the resturant is opened'''
        print(f'{self.resturant_name} is now opened')

    def set_number_served(self, total_served):
        self.number_served = total_served

    def increment_number_served(self, served):
        self.number_served = self.number_served +  served
class IceCreamStand(Resturant):
    def __init__(self,resturant_name, cuisine_type):
        super().__init__(resturant_name, cuisine_type)
        self.flavours = ['Chocolate_flavour', 'Icecream_flavour']
    def display_flavour(self):
        print(f'Then following flavours are available: ')
        for i in self.flavours:
            print(i)


icecream = IceCreamStand('Foodies Arena', 'Meatpie')
#print(icecream.flavours)
#print(icecream.display_flavour())
#Make an instance called restaurant from your class. Print the two attributes individually,
# and then call both methods.
resturant = Resturant('Foodies Arena', 'Meat pie')
#print(resturant.set_number_served(10))
resturant.set_number_served(888)#.increment_number_served(9))
resturant.increment_number_served(90)
#print(f'The number of people that have been served are {resturant.number_served} customers')
#print(resturant.describe_resturant())
#print(resturant.number_served)
#Three Restaurants: Start with your class from Exercise 9-1. Create three\
#different instances from the class, and call describe_restaurant() for each instance
resturant_1 = Resturant('Mr biggs', 'Cake')
resturant_2 = Resturant('Chicken republic', 'Fried chicken')
resturant_3 = Resturant('911', 'Bread')
#print(f'Welcome to {resturant_1.resturant_name}. we sell different types of {resturant_1.cuisine_type}')
#print(f'Welcome to {resturant_2.resturant_name}. we sell different types of {resturant_2.cuisine_type}')
#print(f'Welcome to {resturant_3.resturant_name}. we sell different types of {resturant_3.cuisine_type}')
