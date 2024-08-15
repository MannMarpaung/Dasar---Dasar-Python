# tugas kedua
def faktor_bilangan_program(angka):
    faktor_faktor = []
    bilangan = 1

    while bilangan <= angka:
        if angka % bilangan == 0:
            faktor_faktor.append(bilangan)
        bilangan = bilangan + 1

    print("faktor bilangan dari " + str(angka) + " adalah " + str(faktor_faktor))
faktor_bilangan_program(100)