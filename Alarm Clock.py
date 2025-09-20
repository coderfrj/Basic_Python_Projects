import time, datetime
import pygame

def set_clock():
    now = time.strftime('%H:%M:%S')
    clocktime = input('Enter your time(HH:MM:SS): ')

    while now != clocktime:
        now = time.strftime('%H:%M:%S')
        print(now)
        time.sleep(1)

    pygame.mixer.init()
    pygame.mixer.music.load('alarm.mp3')
    print("TIME'S UP!")

    pygame.mixer.music.play(5)

set_clock()

answer = input(f'Do you want to set the clock again or quit? (a / q): ').lower()
if answer == 'a':
    pygame.mixer.music.stop()
    set_clock()


while answer not in ['a', 'q']:
    if answer == 'a':
        set_clock()
    pygame.mixer.music.play()
    answer = input(f'Do you want to set the clock again or quit? (a / q)').lower()

