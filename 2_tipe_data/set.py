set_var = {'a', 2, 3.5, 4j, 'enak', 61, 78.6, 86j}
print(set_var)
print(type(set_var))

print("-=-=-=-=-=-=--=-=-=-=-=-=-")



# tidak dapat slicing
# print(set_var[3])

# menghapus elemen
set_var.remove('enak')
print(set_var)

# menambahkan elemen
set_var.add('enak kembali')
print(set_var)

# operasi himpunan
var_set1 = {4, 1, 2, 3, 4, 4, 5, 6}
var_set2 = {6, 8, 8, 9, 2, 7}
print(var_set1.intersection(var_set2))
print(var_set1.difference(var_set2))
print(var_set1.union(var_set2))

print("-=-=-=-=-=-=--=-=-=-=-=-=-")