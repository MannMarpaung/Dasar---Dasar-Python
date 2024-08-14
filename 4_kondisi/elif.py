nilai = 90
print("nilai = " + str(nilai))

if nilai >= 60 and nilai < 70:
    print('Grade C')
elif nilai >= 70 and nilai < 80:
    print('Grade B')
elif nilai >= 80 and nilai < 100:
    print('Grade A')
else:
    print('Tidak Lulus')