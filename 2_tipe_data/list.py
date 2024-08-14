list_example = ['a', 2, 3.5, 4j, 'Enak', 63, 70.4, 88j]
print(list_example)
print(type(list_example))

print("-=-=-=-=-=-=--=-=-=-=-=-=-")



# sesuai index a dari awal
print("list_example[2] : " + str(list_example[2]))

# sesuai index a dari akhir
print("list_example[-2] : " + str(list_example[-2]))

# range dari index a sampai index b
print("list_example[1:4] : " + str(list_example[1:4]))

# range dari index 0 sampai b
print("list_example[:4] : " + str(list_example[:4]))

# range dari index a dari akhir sampai akhir
print("list_example[-2:] : " + str(list_example[-2:]))

# range dari index a sampai index b setiap jaka c
print("list_example[1:6:2] : " + str(list_example[1:6:2]))

print("-=-=-=-=-=-=--=-=-=-=-=-=-")



# Menambahkan elemen
hewan = ['ayam', 'burung', 'cacing']
print(hewan)

hewan.append('delman')
print(hewan)

warna = ['ehijau', 'funing']
hewan.append(warna)
print(hewan)

hewan = ['ayam', 'burung', 'cacing', 'delman']
warna = ['ehijau', 'funing']
hewan.extend(warna)
print(hewan)

hewan.insert(0, 'zebra')
print(hewan)

hewan[0] = 'zeus'
print(hewan)

print("-=-=-=-=-=-=--=-=-=-=-=-=-")



# Menghapus elemen
del hewan[0]
print(hewan)

hewan.remove('funing')
print(hewan)

out_hewan = hewan.pop(4)
print(out_hewan)
print(hewan)

print("-=-=-=-=-=-=--=-=-=-=-=-=-")



# Panjang Elemen
print("panjang list hewan ada " + str(len(hewan)))

# Mengetahui index dari sebuah elemen
print("cacing ada di index ke-" + str(hewan.index('cacing')))

# Mengetahui berapa banyak elemen (a)
angka = [0, 2, 3, 5, 2, 4, 3, 2]
print(angka)
print("elemen '2' ada di list sebanyak " + str(angka.count(2)) + " elemen")

# Mengurutkan elemen pada list dari a
warna = ["fkuning", "ahijau", "biru", "chitam", "dungu", "emerah"]
print(warna)
warna.sort()
print(warna)

# Mengurutkan elemen pada list dari z
warna.sort(reverse=True)
print(warna)

# Menggabungkan list
print(hewan + warna)

# Mereplikasikanlist
print(angka*2)