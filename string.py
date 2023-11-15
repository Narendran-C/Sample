x = "Emma is good developer. Emma is a writer"
y = x.split()
count = 0
#print(y)
for i in y:
    if (i == 'Emma') or (i == 'emma'):
        count += 1
print('The word EMMA appears', count, 'times in the sentence')
