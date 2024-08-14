jumlah_kaki = 4
suara = 'meong'
kategori = "mamalia"

if jumlah_kaki == 4:
    print("-=-=-=-=-=- Kemungkinan Pertama : jumlah_kaki = " + str(jumlah_kaki) + " -=-=-=-=-=-")
    print("kemungkinan kucing   = 25%")
    print("kemungkinan buaya    = 25%")
    print("kemungkinan anjing   = 25%")
    print("kemungkinan cicak    = 25%")
    if kategori == 'mamalia':
        print("-=-=-=-=-=- Kemungkinan Kedua : kategori = " + str(kategori) + " -=-=-=-=-=-")
        print("kemungkinan kucing   = 50%")
        print("kemungkinan anjing   = 50%")
        if suara == 'meong':
            print("-=-=-=-=-=- Kemungkinan Ketiga : suara = " + str(suara) + " -=-=-=-=-=-")
            print("kemungkinan kucing   = 100%")
