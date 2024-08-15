# tugas pertama
def faktorial_program(angka):

    number = None

    while angka > 0:
        if number == None:
            first_angka = angka
            number = angka
            angka = angka - 1
        else:
            number = number * angka
            angka = angka - 1

    print("faktorial dari " + str(first_angka) + " adalah " + str(number))

faktorial_program(5)
