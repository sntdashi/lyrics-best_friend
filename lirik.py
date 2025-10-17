import sys
import time

def jalanin_lirik():
    lirik = [
        ("I say that I'm happy", 0.125),
        ("I say that I'm happy", 0.125),
        ("But no, no, no, no", 0.135),
        ("No, no, noooooo", 0.145),
        ("Oh, I still wanna be your favorite boyyyyyyyyyyyyy", 0.093),
        ("I wanna be the one that makes your day", 0.089),
        ("The one you think about as you lie awakeeee", 0.080),
        ("And I can't wait to be your number,", 0.091),
        ("your number oneeeeee", 0.095),
        ("I'll be your biggest fan and you'll be mine", 0.088),
        ("But I still wanna break your heart and make you cry", 0.088)
    ]

    # jeda antar baris, disinkronin sama phrasing aslinya
    delay = [
        1.35, 0.6, 0.7, 1.2, 
        1.06, 0.46, 0.28, 
        0.22,  # ← dikasih jeda dikit di “number,” sebelum lanjut ke baris berikutnya
        0.36, 
        0.33,
        0.45  
    ]

    print("\n== Favorite Boy - Rex Orange County ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='', flush=True)
            time.sleep(delay_karakter)
        print('')
        if i < len(delay):
            time.sleep(delay[i])
    print("\n// Code by rawrzn <3")

jalanin_lirik()