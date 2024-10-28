x1 = int(input("Masukkan angka pertama : "))
x2 = int(input("Masukkan angkat kedua : "))
tentukanOperasi = input("Tentukan Operasi (Penjumlahan, Pengurangan, Perkalian, Pembagian)")

if tentukanOperasi.lower() == "penjumlahan" : 
    total = x1 + x2
    print(total)
elif tentukanOperasi.lower() == "pengurangan" :
    total = x1 - x2
    print(total)
elif tentukanOperasi.lower() == "perkalian" : 
    total = x1 * x2
    print(total)
elif tentukanOperasi.lower() == "pembagian" :
    total = x1 / x2
    print(total)