import sqlite3

# 1. Koneksi ke database (jika belum ada, maka akan dibuat)
conn = sqlite3.connect('data_mahasiswa.db')

# 2. Membuat objek cursor
cursor = conn.cursor()

# 3. Membuat tabel jika belum ada
cursor.execute('''
CREATE TABLE IF NOT EXISTS mahasiswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    nim TEXT NOT NULL UNIQUE,
    jurusan TEXT NOT NULL
)
''')

# 4. Menambahkan data (CREATE)
def tambah_mahasiswa(nama, nim, jurusan):
    cursor.execute('''
    INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (?, ?, ?)
    ''', (nama, nim, jurusan))
    conn.commit()
    print("Data berhasil ditambahkan.")

# 5. Menampilkan data (READ)
def tampilkan_semua_mahasiswa():
    cursor.execute('SELECT * FROM mahasiswa')
    hasil = cursor.fetchall()
    print("Data Mahasiswa:")
    for mhs in hasil:
        print(mhs)

# 6. Mengubah data (UPDATE)
def ubah_mahasiswa(id_mahasiswa, nama_baru):
    cursor.execute('''
    UPDATE mahasiswa SET nama = ? WHERE id = ?
    ''', (nama_baru, id_mahasiswa))
    conn.commit()
    print("Data berhasil diubah.")

# 7. Menghapus data (DELETE)
def hapus_mahasiswa(id_mahasiswa):
    cursor.execute('''
    DELETE FROM mahasiswa WHERE id = ?
    ''', (id_mahasiswa,))
    conn.commit()
    print("Data berhasil dihapus.")

# ---- Penerapan ----
tambah_mahasiswa("Venesa Hutajulu", "11423059", "RPL")
tambah_mahasiswa("Samuel Sitorus", "11423016", "RPL")
tampilkan_semua_mahasiswa()

ubah_mahasiswa(1, "Venesa H. Hutajulu")
hapus_mahasiswa(2)

tampilkan_semua_mahasiswa()

# 8. Menutup koneksi
conn.close()
