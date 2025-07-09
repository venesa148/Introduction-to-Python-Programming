import socket

# Buat socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hubungkan ke server
client_socket.connect(("localhost", 12345))

# Kirim pesan ke server
client_socket.send("Halo server, ini client!".encode())

# Terima balasan dari server
balasan = client_socket.recv(1024).decode()
print(f"Balasan dari server: {balasan}")

# Tutup koneksi
client_socket.close()
