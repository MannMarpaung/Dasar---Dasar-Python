# function
def halaman_utama():
    print("Hello, World!")

halaman_utama()

print("-=-=-=-=-=-=--=-=-=-=-=-=-")

# argument in function
def calculator_tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(hasil)

calculator_tambah(10, 20)

print("-=-=-=-=-=-=--=-=-=-=-=-=-")

def tambah_satu(angka = 0):
    hasil = angka + 1
    print(hasil)

tambah_satu()
tambah_satu(9)

print("-=-=-=-=-=-=--=-=-=-=-=-=-")

# return value in function
def calculator_tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

nomor = calculator_tambah(20, 30)
print(nomor)
