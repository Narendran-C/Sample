def dectobinary(n):
    binarynum = [0] * n
    i = 0
    while n > 0:
        binarynum[i] = n % 2
        n = int(n / 2)
        i += 1
    for j in range(i, 0, -1):
        print(binarynum[j], end="")


n = 10
dectobinary(n)
