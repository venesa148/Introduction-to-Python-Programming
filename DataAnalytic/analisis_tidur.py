import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Hari': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'Jam_Tidur': [6, 7, 5.5, 6.5, 5, 8, 9]
}

df = pd.DataFrame(data)

# Statistik
print("=== Statistik Tidur ===")
print("Rata-rata jam tidur:", df['Jam_Tidur'].mean())
print("Hari paling sedikit tidur:", df.loc[df['Jam_Tidur'].idxmin(), 'Hari'])

# Visualisasi
plt.plot(df['Hari'], df['Jam_Tidur'], marker='o', color='purple')
plt.title('Kebiasaan Tidur Mingguan')
plt.ylabel('Jam Tidur')
plt.xlabel('Hari')
plt.grid(True)
plt.tight_layout()
plt.show()
