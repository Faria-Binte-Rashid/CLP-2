import random
random_numbers = [random.randint(0, 100) for _ in range(100)]
min_num = min(random_numbers)
max_num = max(random_numbers)
normalized_list = [(num - min_num) / (max_num - min_num) for num in random_numbers]
print(normalized_list)
