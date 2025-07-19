import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Nama': ['Ani', 'Budi', 'Citra', 'Dani', 'Eka', 'Fajar', 'Gita', 'Hana'],
    'Genre_Favorit': ['Drama', 'Aksi', 'Drama', 'Komedi', 'Aksi', 'Aksi', 'Komedi', 'Drama']
}

df = pd.DataFrame(data)

# Hitung jumlah penyuka tiap genre
genre_count = df['Genre_Favorit'].value_counts()

print("=== Genre Paling Disukai ===")
print(genre_count)

# Genre paling favorit
favorit = genre_count.idxmax()
print("\nGenre paling favorit:", favorit)

# Visualisasi
genre_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Genre Favorit')
plt.ylabel('')
plt.tight_layout()
plt.show()
