i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('готово')

i = 0
for i in range(3):
    print(i)
    if i == 1:                #элсе не выполняеьть ся если отановили принудительно.
        break
else:
    print('готово')