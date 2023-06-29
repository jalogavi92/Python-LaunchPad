import random

def generate_random_list(length, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(length)]

def find_max_min_avg(numbers):
    if not numbers:
        return None, None, None
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    return maximum, minimum, average

length = 10
min_val = 1
max_val = 100

random_list = generate_random_list(length, min_val, max_val)
print("Random List:", random_list)

maximum, minimum, average = find_max_min_avg(random_list)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)
