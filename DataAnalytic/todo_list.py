# To-Do List CLI App
import os

FILENAME = "todolist.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    print("\n📋 Daftar Tugas:")
    if not tasks:
        print(" (kosong)")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f" {idx}. {task}")
    print()

def add_task(tasks):
    task = input("Masukkan tugas baru: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Tugas ditambahkan.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            save_tasks(tasks)
            print(f"🗑️ Tugas '{removed}' dihapus.")
        else:
            print("❌ Nomor tidak valid.")
    except ValueError:
        print("❌ Input tidak valid.")

def main():
    tasks = load_tasks()

    while True:
        print("=== To-Do List ===")
        print("1. Lihat Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        choice = input("Pilih menu (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Keluar dari aplikasi.")
            break
        else:
            print("❌ Pilihan tidak tersedia.")
        print()

if __name__ == "__main__":
    main()
