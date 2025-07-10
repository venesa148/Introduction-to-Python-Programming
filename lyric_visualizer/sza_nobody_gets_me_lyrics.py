import time
import sys
from threading import Thread
from playsound import playsound

# Fungsi untuk menampilkan teks dengan animasi karakter per karakter
def animate_text(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Fungsi untuk menyanyi per baris (dipanggil oleh thread)
def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

# Fungsi untuk memutar lagu di thread terpisah
def play_music():
    playsound("nobody_gets_me.mp3")

# Fungsi utama
def sing_song():
    # Lirik (ambil potongan pendek untuk contoh)
    lyrics = [
        ("\nTook a long vacation", 0.5, 0.08),
        ("No make-up, just Jay-Z", 3, 0.08),
        ("You were balls deep, now we beefin’", 6, 0.08),
        ("Had me butt naked at the MGM", 9, 0.08),
        ("So wasted, screamin’, 'f*** that'", 12, 0.08),
        ("Blurry now but I meant it then", 15, 0.08),
        ("Hurry now baby, stick it in", 18, 0.08),
        ("’Fore the memories get to kickin’ in", 21, 0.08),
        ("It's too late, I don't want to lose", 24, 0.08),
        ("What’s left of you", 27, 0.08),
        ("I’m not gonna hold you through it", 30, 0.08),
        ("Nobody gets me like you", 33, 0.1),
    ]

    # Thread untuk musik
    music_thread = Thread(target=play_music)
    music_thread.start()

    # Thread untuk teks
    lyric_threads = [Thread(target=sing_lyric, args=lyric) for lyric in lyrics]

    for thread in lyric_threads:
        thread.start()

    for thread in lyric_threads:
        thread.join()

    music_thread.join()

if __name__ == "__main__":
    sing_song()
