import json
import os

# File untuk menyimpan data
DATA_FILE = 'books.json'

# Inisialisasi file jika belum ada
def init_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

# Menyimpan data buku ke file JSON
def save_books(books):
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=4)

# Membaca semua data buku dari file JSON
def load_books():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Menambahkan buku baru
def add_book(title, author):
    books = load_books()
    book_id = len(books) + 1
    books.append({
        'id': book_id,
        'title': title,
        'author': author
    })
    save_books(books)
    print(f"Buku '{title}' berhasil ditambahkan!")

# Menampilkan semua buku
def display_books():
    books = load_books()
    if not books:
        print("Belum ada buku.")
        return
    for book in books:
        print(f"[{book['id']}] {book['title']} - {book['author']}")

# Mencari buku berdasarkan judul
def search_book(keyword):
    books = load_books()
    found = [b for b in books if keyword.lower() in b['title'].lower()]
    if found:
        for book in found:
            print(f"[{book['id']}] {book['title']} - {book['author']}")
    else:
        print("Buku tidak ditemukan.")

# Menghapus buku berdasarkan ID
def delete_book(book_id):
    books = load_books()
    books = [b for b in books if b['id'] != book_id]
    save_books(books)
    print(f"Buku dengan ID {book_id} telah dihapus.")
