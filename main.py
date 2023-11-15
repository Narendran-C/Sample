from functions import subtraction as sub
from functions import add
from functions import multiply as mul


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
print(has_duplicate_letters(sentence1))
print(has_duplicate_letters(sentence2))
print(add(2, 3, 4, 5, 6))
print(sub(2, 3))
print(mul(10, 2, 2))
