y = 2
z = 2
a = 2
for i in range(1, y + 1):
    print(f'first loop', i)
    for i in range(1, z + 1):
        print(f'second loop', i)
        for i in range(1, a + 1):
            print(f'third loop', i)
            break
        break
    break
