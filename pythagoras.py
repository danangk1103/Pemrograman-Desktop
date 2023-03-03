# Input panjang sisi-sisi segitiga
a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))

# Hitung panjang sisi miring (c)
c = (a**2 + b**2)**0.5

# Hitung luas segitiga
luas = 0.5 * a * b

# Cetak hasil
print("Panjang sisi miring (c) = ", c)
print("Luas segitiga = ", luas)
