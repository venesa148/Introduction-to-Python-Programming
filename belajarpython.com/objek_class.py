# inheritance adalah pengalihan karakteristik kelas ke kelas lain yang berasal darinya, keturunan
# instance objek individu kelas tertentu
#  instantiantio  => penciptaan sebuah instance dari sebuah kelas
# method => jenis fungsi jhusu yang didefinisikan dalam definisi kelas

# class itu blue print
# Objek hasil class

# 1. Menbuat kelas di pyhton

class Pekerja:
    # Konstruksi (_init_) untuk mengukur atribut awal
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

    # Method untuk menampilkan informasi pekerja
    def tampilkan_info(self):
        print(f"Nama    : {self.nama}")
        print(f"Jabatan : {self.jabatan}")
        print(f"Gaji    : Rp{self.gaji:,}")

    # Method untuk menaikkan gaji
    def naikkan_gaji(self, persen):
        kenaikan = self.gaji * persen / 100
        self.gaji += kenaikan
        print (f"Gaji{self.nama} naik sebesar {persen}% menjadi Rp{self.gaji:,}")

    # Membuat penggunaan objek
pekerja1 = Pekerja("Venesa", "Programmer", 500000)
pekerja2 = Pekerja("Samuel", "Data Analyst", 600000)

# Menampilkan info pekerja
pekerja1.tampilkan_info()
print()
pekerja2.tampilkan_info()

print("\nStelah Kenaikan gaji:\n")

# Naikkan gaji pekerja
pekerja1.naikkan_gaji(10)
pekerja2.naikkan_gaji(15)

              
