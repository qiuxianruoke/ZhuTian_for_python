a = [1, 2, 3, 4, 5]
#print(a[0])
l = len(a)
for i in range(len(a)):
    a.remove(a[i])
    print(a[i],'\n')