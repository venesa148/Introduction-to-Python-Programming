import pandas as pd
import matplotlib.pyplot as plt

# 1. Data nilai siswa
data = {
    'Nama': ['Ayu', 'Budi', 'Citra', 'Dedi', 'Eka'],
    'Matematika': [85, 70, 90, 60, 75],
    'Bahasa Inggris': [80, 75, 88, 65, 85]
}

# 2. Membuat DataFrame
df = pd.DataFrame(data)

# 3. Menampilkan data
print("=== Nilai Siswa ===")
print(df)

# 4. Menghitung nilai rata-rata tiap siswa
df['Rata-rata'] = df[['Matematika', 'Bahasa Inggris']].mean(axis=1)
print("\n=== Dengan Rata-rata ===")
print(df)

# 5. Visualisasi - Bar chart rata-rata nilai
plt.figure(figsize=(8, 5))
plt.bar(df['Nama'], df['Rata-rata'], color='skyblue')
plt.title('Rata-rata Nilai Siswa')
plt.xlabel('Nama')
plt.ylabel('Rata-rata Nilai')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
