list_a = [10, 20, 30, 40, 50]

print("Elemen ke 3:", list_a[2])
print("Elemen ke 2 sampai ke 4:", list_a[1:4])
print("Elemen terakhir:", list_a[-1])

list_a[3] = 45
list_a[3:] = [45, 55]
list_b = list_a[0:2]
list_b.append("Hello")
list_b.extend([1, 2, 3])
list_c = list_a + list_b

print("List A:", list_a)
print("List B:", list_b)
print("List C (gabungan A dan B):", list_c)
