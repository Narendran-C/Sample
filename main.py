def has_duplicate_letters(sentence):
    words = sentence.split()

    for word in words:
        seen = set()

        for char in word:
            if char in seen:
                return True
            seen.add(char)
    return False


sentence1 = "This is the third change"
sentence2 = "Hello change 3 "
#print(has_duplicate_letters(sentence1))  # True (because "This" has duplicate letters)
#print(has_duplicate_letters(sentence2))  # False (no word has duplicate letters)
