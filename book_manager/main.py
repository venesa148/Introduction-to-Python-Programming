import book_manager

def main():
    book_manager.init_file()
    
    while True:
        print("\n=== Manajemen Buku ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Cari Buku")
        print("4. Hapus Buku")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            judul = input("Judul buku: ")
            penulis = input("Nama penulis: ")
            book_manager.add_book(judul, penulis)

        elif pilihan == '2':
            book_manager.display_books()

        elif pilihan == '3':
            kata_kunci = input("Masukkan judul yang dicari: ")
            book_manager.search_book(kata_kunci)

        elif pilihan == '4':
            try:
                id_buku = int(input("Masukkan ID buku yang ingin dihapus: "))
                book_manager.delete_book(id_buku)
            except ValueError:
                print("ID harus berupa angka!")

        elif pilihan == '5':
            print("Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == '__main__':
    main()
