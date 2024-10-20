import pygame
import sys
import keyboard
import os
import tempfile
import shutil
import pystray

mp3_filename = 'pedik.mp3'

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.mixer.init()

mp3_path = resource_path(mp3_filename)
try:
    pygame.mixer.music.load(mp3_path)
except Exception as e:
    print(f"Ошибка загрузки файла: {e}")
    sys.exit()

def on_exit(icon, item):
    icon.stop()
    pygame.mixer.music.stop()
    sys.exit()

def main():

    while True:
        if keyboard.is_pressed('esc'):
            break

        if keyboard.read_event().event_type == keyboard.KEY_DOWN:
            pygame.mixer.music.play()

def setup(icon):
    icon.visible = True

if __name__ == "__main__":
    main()
