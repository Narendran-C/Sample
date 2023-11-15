def vowels_count(value):
    print(value)
    count = 0
    for char in value:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    return count


sentence = "Hello World"
print('Number of Vowels :', vowels_count(sentence))
