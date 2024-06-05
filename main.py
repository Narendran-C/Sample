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


add_fun = add
sentence1 = "This is the third change"
sentence2 = "Hello change 4 "
print(has_duplicate_letters(sentence1))
print(has_duplicate_letters(sentence2))
print(add_fun(2, 5, 8, 5, 6))
print(sub(2, 3))
print(mul(10, 3, 1))
