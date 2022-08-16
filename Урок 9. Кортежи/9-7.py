a = [4,6,'ру','tell',78]
b = [44,'hello',56,'expert',3]
c = a + b
print(c)
c.insert(3,6)
for i in c:
    if type(i)==str:
        c.remove(i)
print(c)
c.sort()
print(c)
print('Длинна списка',len(c))
