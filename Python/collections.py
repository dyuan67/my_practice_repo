# lists
cart = ["apples", "bannanas", "cherries", "cherries"]
print(cart)

# Add elements to list --> This is a list so there are duplicates (not a set)
cart.append("donuts")
cart.append("eggs")
cart.append("flour")
print(cart)

cart.remove("cherries") # Removes the first iteration of cherries (only 1)
print(cart)

# Trying to remove something that is not on the list
# cart.remove("pineapple")
if "pineapple" in cart:
    cart.remove("pineapple")

# Remove is if you know the element you want to remove
# Pop is if you know the index you want to remove

cart.pop(3) #Removes the element at index 3
print(cart)

#Can treat list as a stack (first in, last out)
cart.pop() #Remove the last element added to your list
print(cart)

# Sort/reverse elements of a list
cart.reverse()
print(cart)
cart.sort() # If string alphabetical, numbers --> numerical, objects --> that thing)
print(cart)

cart.append("bannanas")
cart.append("grapes")
cart.append("oranges")
print(cart)

#Split the list
    # cart[start.index : end.index] --> the last index is not inclusive
fruit_basket = cart[4:] # if starting from the first index or going to the last index, can leave it blank
print(cart)
print(fruit_basket)

# Create an empty list
squares = [] # Declaring a list
for i in range(1, 10): # range(1, 10) --> starts from 1, goes up to 9 (10 is not inclusive)
    value = i**2 #or i*i
    squares.append(value)
print(squares)

# List Comprehension
squares2 = [i*i for i in range(1,10)]
print(squares2)

b_items = [item for item in cart if item.startswith("b")]
print(b_items)
# string.startswith("b")

'''
inventory = []
inventory[0] = 100, will result in an error because the list is empty,
    Nothing to call upon
'''

inventory = [0]*len(cart) #Give it a default value, and then multiple it
    # by how large you want it to be
print(inventory)
inventory[0] = 100

# Sets --> No duplicates
number_set = set()
number_set = {1, 1, 2, 3, 4, 0, 10, 5} # The double 1 will not cause error, just deleted
print(number_set) # Will print the list out "in order", sets have no order
number_set.add(-10)
print(number_set)

# How to rmeove duplicates from list
num_list = [1, 1, 4, 5, 5, 6, 6]
no_dups = set(num_list)
print(no_dups)
no_dups = list(no_dups) #convert set to a list
print(no_dups)

# Sort set function
ns = sorted(number_set)
print(ns)
'''
["apples", "grapes", "bannans"]
0, 1, 2 --> Key
    So, if you look up the key, it will return the value
        example: 1 = grapes
'''
# Dictionary (similar to a hash table in Java)
# ex. capitals = {"Maryland" : "Annaplis"}
    # {key : value}
fav_snacks = {} # empty
fav_snacks = {
    "kathleen" : "tortilla chips",
    "maggie" : "pretzels",
    "emily" : "buffalo chicken dip",
    "ava" : "chocolate"
}
print(fav_snacks)
fav_snacks["wade"] = "popcorn" # Similar to list, where key is the index place = value
print(fav_snacks)
print("Kathleen's favorite snack is " + fav_snacks["kathleen"])
    # The Key is basically an index value, so it uses[]
# print("Bob's favorite snack is " + fav_snacks["bob"])
    # Will reuslt in an error, so check if it is in list
if "bob" in fav_snacks:
    print("Bob's favorite snack is " + fav_snacks["bob"])

for key in fav_snacks:
    print(key + "'s favorite food is " + fav_snacks[key])
    print(f"{key}'s favorite food is {fav_snacks[key]}")
        # F string

for key, value in fav_snacks.items():
    print(key, value)

keys = fav_snacks.keys()
values = fav_snacks.values()
fav_snacks["alice"] = ["chips", "nuts"]
    # Value can be a list, multiple items
        # Key cannot be a list; single thing
            # No duplicate keys, but duplicate values
print(fav_snacks)

fav_snacks["alice"] = "bread"
print(fav_snacks)