import pandas as pd
import matplotlib.pyplot as plt

# Data penjualan (langsung di kode)
data = {
    'Tanggal': ['2025-07-01','2025-07-01','2025-07-02','2025-07-02','2025-07-03','2025-07-03'],
    'Produk': ['Kaos','Sepatu','Kaos','Celana','Sepatu','Celana'],
    'Jumlah_Terjual': [10, 5, 8, 7, 6, 9],
    'Harga_Satuan': [100000, 300000, 100000, 150000, 300000, 150000]
}

df = pd.DataFrame(data)
df['Pendapatan'] = df['Jumlah_Terjual'] * df['Harga_Satuan']

# Total pendapatan per produk
total_produk = df.groupby('Produk')['Pendapatan'].sum()
print("=== Pendapatan per Produk ===")
print(total_produk)

# Produk terlaris
produk_terlaris = df.groupby('Produk')['Jumlah_Terjual'].sum().idxmax()
print("\nProduk terlaris:", produk_terlaris)

# Visualisasi pendapatan per produk
total_produk.plot(kind='bar', color='coral', title='Pendapatan per Produk')
plt.ylabel('Pendapatan (Rp)')
plt.tight_layout()
plt.show()
