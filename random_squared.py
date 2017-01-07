import random

random_numbers = random.sample(range(49), 20)
print(random_numbers)
squared_nums = [num**2 for num in random_numbers]
print(squared_nums)