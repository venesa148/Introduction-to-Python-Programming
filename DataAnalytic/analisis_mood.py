import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data mood selama seminggu
data = {
    'Hari': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'Mood': ['Sedih', 'Biasa', 'Senang', 'Biasa', 'Senang', 'Senang', 'Biasa'],
    'Skor_Mood': [3, 5, 8, 5, 9, 10, 6]  # Skala mood: 1 (buruk) sampai 10 (sangat baik)
}

df = pd.DataFrame(data)

# Statistik sederhana
print("=== Rata-rata Mood ===")
print("Rata-rata skor mood mingguan:", df['Skor_Mood'].mean())
print("Hari dengan mood terbaik:", df.loc[df['Skor_Mood'].idxmax(), 'Hari'])

# Visualisasi: Mood line chart
plt.figure(figsize=(8, 4))
sns.lineplot(x='Hari', y='Skor_Mood', data=df, marker='o', color='orange')
plt.title('Grafik Mood Harian')
plt.ylabel('Skor Mood (1-10)')
plt.ylim(0, 10)
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualisasi: Jumlah tiap kategori mood
plt.figure(figsize=(5, 4))
sns.countplot(x='Mood', data=df, palette='Set2')
plt.title('Frekuensi Mood Mingguan')
plt.tight_layout()
plt.show()
