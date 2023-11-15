f = open('test.txt', 'a+')
f.write("\nFile Terminated....Thanks....Good Luck!!!")
f.seek(0)
print(f.read())
f.close()




