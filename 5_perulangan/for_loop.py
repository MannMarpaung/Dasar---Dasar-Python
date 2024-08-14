for i in range(0, 10):
    print("angka yang ke-" + str(i))

print("-=-=-=-=-=-=--=-=-=-=-=-=-")

array = ['mobil', 'motor', 'kereta']
for i in array:
    print(i)

print("-=-=-=-=-=-=--=-=-=-=-=-=-")

for x in range(5):
    if int(x) == 2:
        continue
    print(x)

print("-=-=-=-=-=-=--=-=-=-=-=-=-")

# break
makanan = ['apel', 'pisang', 'semangka', 'jeruk']
for x in makanan:
    print(x)
    if x == 'semangka':
        break