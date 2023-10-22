import pyautogui
import keyboard
import string
import time


cor_ativa = False
letras = list(string.ascii_letters) + list(string.digits)

while True:
    try:
        if any(keyboard.is_pressed(letra) for letra in letras):
            cor_ativa = not cor_ativa

        if cor_ativa:
            pyautogui.press(['fn', 'scrolllock'])
            time.sleep(0.080)

        if cor_ativa:
            cor_ativa = False

    except KeyboardInterrupt:
        break








