def get_integers(mixed_list):
    return [x for x in mixed_list if isinstance(x, (int, float)) and x >= 0]


mixed_list = [10, 'apple', 5, 0.2, 'orange', 7, 'banana', 3]
result = get_integers(mixed_list)

print("Original List:", mixed_list)
print("Integers Only:", result)
