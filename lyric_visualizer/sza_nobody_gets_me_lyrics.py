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
    playsound('lyric_visualizer/nobody_gets_me.mp3')

# Fungsi utama
def sing_song():
    # Lirik (ambil potongan pendek untuk contoh)
    lyrics = [
("\n[Musik]", 0.5, 0.08),
    ("\nTook a long vacation", 20, 0.08),
    ("No make-up, just Jay-Z", 22, 0.08),
    ("You were balls deep, now we beefin’", 24, 0.08),
    ("Had me butt naked at the MGM", 26, 0.08),
    ("So wasted, screamin’, 'f*** that'", 28, 0.08),
    ("Blurry now, but I meant it then", 30, 0.08),
    ("Hurry now, baby, stick it in", 32, 0.08),
    ("'Fore the memories get to kickin' in", 34, 0.08),
    ("It's too late, I don't want to lose", 36, 0.08),
    ("What's left of you", 38, 0.08),
    ("I’m not gonna hold you through it", 40, 0.08),
    ("Nobody gets me like you", 42, 0.1),

    ("\nHow am I 'posed to let you go?", 47, 0.08),
    ("Only like myself when I'm with you", 49, 0.08),
    ("Nobody gets me, you do", 51, 0.08),

    ("\nYou do", 53, 0.1),
    ("Nobody gets me, you do", 55, 0.08),
    ("Took me out to the ballet", 58, 0.08),
    ("You proposed, I went on the road", 60, 0.08),
    ("You was feelin' empty so you left me", 62, 0.08),
    ("Now I'm stuck dealin' with a deadbeat", 64, 0.08),
    ("If I'm real, I deserve less", 66, 0.08),
    ("If I was you, I wouldn't take me back", 68, 0.08),
    ("I pretend when I'm with a man, it's you", 70, 0.08),
    ("And I know that it's too late, I don't want to lose", 72, 0.08),
    ("What's left of you", 74, 0.08),
    ("How am I 'posed to tell you?", 76, 0.08),
    ("I don't wanna see you with anyone but me", 78, 0.08),
    ("Nobody gets me like you", 80, 0.1),

    ("\nHow am I 'posed to let you go?", 85, 0.08),
    ("Only like myself when I'm with you", 87, 0.08),
    ("Nobody gets me, you do", 89, 0.08),
    ("You do", 91, 0.1),
    ("Nobody gets me, you do", 93, 0.08),
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
