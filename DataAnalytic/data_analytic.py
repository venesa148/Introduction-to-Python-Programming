# data_analytic.py
# Materi Data Analytic Dasar di Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Membuat DataFrame sederhana
data = {
    'Nama': ['Ayu', 'Budi', 'Citra', 'Dedi', 'Eka'],
    'Umur': [23, 25, 22, 24, 23],
    'Nilai': [85, 78, 92, 70, 88]
}

df = pd.DataFrame(data)

# 2. Menampilkan isi DataFrame
print("=== Data Mahasiswa ===")
print(df)

# 3. Statistik Deskriptif
print("\n=== Statistik Deskriptif ===")
print(df.describe())

# 4. Menambahkan Kolom Baru
df['Lulus'] = df['Nilai'] >= 75
print("\n=== Data dengan Status Lulus ===")
print(df)

# 5. Visualisasi: Plot Umur vs Nilai
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Umur', y='Nilai', hue='Lulus')
plt.title('Plot Umur vs Nilai Mahasiswa')
plt.xlabel('Umur')
plt.ylabel('Nilai')
plt.grid(True)
plt.tight_layout()
plt.show()
