import json
import os
from datetime import datetime

DATA_FILE = "finance_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def tambah_transaksi(data):
    print("\n=== Tambah Transaksi Baru ===")
    jenis = input("Jenis (masuk/keluar): ").strip().lower()
    if jenis not in ['masuk', 'keluar']:
        print("Jenis tidak valid. Gunakan 'masuk' atau 'keluar'.")
        return

    try:
        jumlah = float(input("Jumlah: "))
    except ValueError:
        print("Jumlah harus angka.")
        return

    keterangan = input("Keterangan: ")
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transaksi = {
        "jenis": jenis,
        "jumlah": jumlah,
        "keterangan": keterangan,
        "tanggal": tanggal
    }

    data.append(transaksi)
    save_data(data)
    print("Transaksi berhasil ditambahkan!\n")

def tampilkan_ringkasan(data):
    print("\n=== Ringkasan Keuangan ===")
    total_masuk = sum(t['jumlah'] for t in data if t['jenis'] == 'masuk')
    total_keluar = sum(t['jumlah'] for t in data if t['jenis'] == 'keluar')
    saldo = total_masuk - total_keluar

    print(f"Total Masuk  : Rp {total_masuk:,.2f}")
    print(f"Total Keluar : Rp {total_keluar:,.2f}")
    print(f"Saldo Akhir  : Rp {saldo:,.2f}\n")

    tampilkan_grafik(total_masuk, total_keluar)

def tampilkan_grafik(masuk, keluar):
    print("=== Grafik Sederhana ===")
    def buat_batang(nilai, simbol):
        return simbol * int(nilai // 10000)  # 1 simbol = 10.000

    print(f"Masuk  : {buat_batang(masuk, '#')}")
    print(f"Keluar : {buat_batang(keluar, '-')}\n")

def tampilkan_transaksi(data):
    print("\n=== Riwayat Transaksi ===")
    if not data:
        print("Belum ada data transaksi.\n")
        return

    for i, t in enumerate(data, 1):
        print(f"{i}. [{t['tanggal']}] {t['jenis'].upper()} Rp {t['jumlah']:,.2f} - {t['keterangan']}")
    print()

def menu():
    data = load_data()
    while True:
        print("========== Aplikasi Keuangan ==========")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Ringkasan")
        print("3. Tampilkan Semua Transaksi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == '1':
            tambah_transaksi(data)
        elif pilihan == '2':
            tampilkan_ringkasan(data)
        elif pilihan == '3':
            tampilkan_transaksi(data)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    menu()
