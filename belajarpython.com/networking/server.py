import socket

# Buat socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tentukan alamat IP dan port
server_socket.bind(("localhost", 12345))

# Dengarkan koneksi masuk
server_socket.listen()

print("Server siap menerima koneksi...")

# Terima koneksi dari client
client_socket, client_address = server_socket.accept()
print(f"Terkoneksi dengan {client_address}")

# Terima pesan dari client
pesan = client_socket.recv(1024).decode()
print(f"Pesan dari client: {pesan}")

# Kirim balasan ke client
client_socket.send("Halo juga dari server!".encode())

# Tutup koneksi
client_socket.close()
server_socket.close()
