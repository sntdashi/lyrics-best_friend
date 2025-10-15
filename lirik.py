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
        ("The one you think about as you lie awake", 0.088),
        ("And I can't wait to be your number, your number one", 0.093),
        ("your number one", 0.092),
        ("I'll be your biggest fan and you'll be mine", 0.087),
        ("But I still wanna break your heart and make you cry", 0.080)
    ]

    # jeda antar kau dan baris anjg
    delay = [
        1.35, 0.8, 0.9, 1.2, 
        1.45, 0.45, 0.25, 
        0.35,  
        0.18, 
        0.35,
        0.4  
    ]

    print("\n== Favorite Boy - Rex Orange County ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='', flush=True)
            time.sleep(delay_karakter)
        print('')
        if i < len(delay):
            time.sleep(delay[i])
    print("\n// Code by rawzn <3")

jalanin_lirik()