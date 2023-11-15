person = {"name": ["Jessa", "Jack"], "country": ["USA", "UAE"], "telephone": [1178, 1234], "pet": ["Cat", "Dog"]}
person1 = {"name": "Josh", "country": "UK", "telephone": 8798, "pet": "Mice"}
# print('')
# print('Now accessing the element through [] and get() function')
# print(person['name'])
# print(person.get('telephone'))
# print('')
# print('Now accessing the key(), values() and items()')
# print(person.keys())
# print(person.values())
# print(person.items())
# print('')
# iterating
# print('key', ':', 'value')
# for key in person:
#     print(key, ':', person[key])
# for key in person:
#     print(key, ':', person1[key])
person.update({"height": [6, 7], "weight": 70})
print(person)
person.update({"height": [7, 6]})
print(person)
person.update({"hobby": "Baseball", "place": "NC"})
print(person)
person.update({"height": [5, 6], "weight": 60})
print(person)

