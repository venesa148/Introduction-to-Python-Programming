# bahasa pemprograman itu biasa nya di eksekusi satu satu sehingga , butuh perulangan untuk masalah yang dijalankan berulang

# while -> dieksekusi berkali kali ketika kondisi bernilai benar atau true

count = 1 
while (count<4):
    print("The count is:", count)
    count=count+1

    print ("okay!")

# for loop -> memiliki kemampuan untuk mengulagi item dari urutan apapun, seperti list atau string
# simpan nilai ke variabel x

nilai= [1,2,3,4,5]
for x in nilai:
    print(x)

buah =["nanas","apel","Mangga"]
for makanan in buah:
    print("saya suka makan buah:", makanan )

# nested loop -> memungkin pemprograman dalam satu lingkaran di dalam loop lain
# perulang dalam perulangan

a = 2
while a < 10:
    j = 2
    while j <= a / j:
        if a % j == 0:
            break
        j = j + 1
    if j > a / j:
        # Lanjut kessini jika tidak memenuhi whilw
        print(a, "is prima")
    a = a + 1