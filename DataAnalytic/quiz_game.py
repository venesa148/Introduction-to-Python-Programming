import random
import time

questions = [
    {
        "question": "Apa ibu kota Indonesia?",
        "options": ["A. Surabaya", "B. Jakarta", "C. Bandung", "D. Yogyakarta"],
        "answer": "B"
    },
    {
        "question": "Hasil dari 12 x 5 adalah...",
        "options": ["A. 50", "B. 55", "C. 60", "D. 65"],
        "answer": "C"
    },
    {
        "question": "Siapa penemu lampu pijar?",
        "options": ["A. Albert Einstein", "B. Galileo", "C. Isaac Newton", "D. Thomas Edison"],
        "answer": "D"
    },
    {
        "question": "Bahasa pemrograman yang digunakan untuk web development frontend adalah...",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "Gunung tertinggi di dunia adalah...",
        "options": ["A. Everest", "B. Kilimanjaro", "C. Merapi", "D. Elbrus"],
        "answer": "A"
    },
    {
        "question": "Siapa presiden pertama Indonesia?",
        "options": ["A. Habibie", "B. Soeharto", "C. Soekarno", "D. Gus Dur"],
        "answer": "C"
    },
    {
        "question": "Berapa hasil dari 2 ** 4 (pangkat)?",
        "options": ["A. 6", "B. 8", "C. 16", "D. 24"],
        "answer": "C"
    },
    {
        "question": "Apa nama planet ke-3 dari matahari?",
        "options": ["A. Venus", "B. Mars", "C. Bumi", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Satuan SI untuk arus listrik adalah...",
        "options": ["A. Ampere", "B. Volt", "C. Ohm", "D. Watt"],
        "answer": "A"
    },
    {
        "question": "Apa nama bahasa yang digunakan untuk membuat AI?",
        "options": ["A. Python", "B. PHP", "C. HTML", "D. Swift"],
        "answer": "A"
    }
]

def run_quiz():
    score = 0
    total = len(questions)
    random.shuffle(questions)
    
    print("🎓 Selamat datang di Quiz Pintar!\nJawab pertanyaan berikut dengan memilih A, B, C, atau D.\n")
    time.sleep(1)

    for i, q in enumerate(questions, 1):
        print(f"{i}. {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Jawaban kamu (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            print("✅ Benar!\n")
            score += 1
        else:
            print(f"❌ Salah. Jawaban yang benar: {q['answer']}\n")
        time.sleep(0.5)

    print("="*40)
    print(f"Skor akhir kamu: {score}/{total}")
    if score == total:
        print("🎉 Sempurna! Kamu luar biasa!")
    elif score >= total * 0.7:
        print("👍 Bagus! Kamu cukup pintar.")
    else:
        print("😅 Tetap semangat belajar ya!")
    print("="*40)

if __name__ == "__main__":
    run_quiz()
