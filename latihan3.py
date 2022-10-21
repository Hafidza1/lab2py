# input nilai variable
a=input("masukkan nilai a:")
b=input("masukkan nilai b:")

# cetak nilai variabel
print("Variabela=",a)
print("Variabelb=",b)

# cetal hasil operasi kedua variabel dengan String Format
print("Hasil penggabungan (1)&(0)=%s".format(a,b) %(a+b))

# konversi nilai variabel
a=int(a)
b=int(b)
print("Hasil penjumlahan (1)+(0)=%d".format(a,b) %(a+b))
print("Hasil pembagian (1)/(0)=%d".format(a,b) %(a/b))

