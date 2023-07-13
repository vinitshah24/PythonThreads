import random

# Original array
array = [
    "category1/1", "category1/2", "category1/3", "category1/4", "category1/5", "category1/6",
    "category2/1", "category2/2", "category2/3", "category2/4",
    "category3/1", "category3/2"
]

# Separate elements by category
category1 = []
category2 = []
category3 = []

for element in array:
    if element.startswith("category1"):
        category1.append(element)
    elif element.startswith("category2"):
        category2.append(element)
    elif element.startswith("category3"):
        category3.append(element)

# Calculate the length of each category
category1_length = len(category1)
category2_length = len(category2)
category3_length = len(category3)

# Determine the maximum length among the categories
max_length = max(category1_length, category2_length, category3_length)

# Randomize the elements while maintaining a good balance
random.shuffle(category1)
random.shuffle(category2)
random.shuffle(category3)

# Create a new randomized array
randomized_array = []

for i in range(max_length):
    if i < category1_length:
        randomized_array.append(category1[i])
    if i < category2_length:
        randomized_array.append(category2[i])
    if i < category3_length:
        randomized_array.append(category3[i])

print(randomized_array)
