import random
import os
print("Select a random element from a list:")
elements = [1, 2, 3, 4, 5]
print(random.choice(elements))

elements = set([1, 2, 3, 4, 5])
# convert to tuple because sets are invalid inputs
print(random.choice(tuple(elements)))