"""
import random

my_list =range(1,7)
pattern = []
for i in range (50):
    num_elements = random.randint(1,3)
    random_elements = random.sample(my_list, num_elements)

    pattern.append(random_elements)

print(pattern)
"""

pattern = [[6, 3], [4], [6, 3, 1], [4], [6, 5, 1], [5, 4], [2, 5], [1], [4, 6, 5], [3, 5, 6], [1, 5], [1, 3],
           [3, 1], [4], [5, 4, 1], [5, 6], [3, 4], [2, 6, 1], [6, 1, 2], [4], [1], [1], [2], [3], [5, 3, 2], [4],
           [2], [3, 6, 1], [3, 4], [1, 5, 6], [2], [2], [6, 3], [1, 2], [5, 2, 3], [1], [1], [3, 4, 2], [1, 5], [5],
           [1, 2, 3], [6, 1, 3], [6, 3], [1, 3], [5, 2, 4], [2, 1, 4], [4, 2], [4, 5, 2], [6], [2, 4, 1]]
my_dict = {}
my_list = []

for i in pattern:
    if not i in my_list:
        my_list.append(i)
        my_dict[str(i)] = 1
    else:
        value = my_dict[str(i)]
        value+=1
        my_dict[str(i)] = value
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse= True))


print(sorted_dict)

