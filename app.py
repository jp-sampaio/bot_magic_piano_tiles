'''
    Automatizar o jogo Magic Piano Tiles, utilizando as libs pyautogui, webbrowser, pywin32, sleep.
'''

import pyautogui
import webbrowser
import keyboard
import win32api
import win32con
from time import sleep


# Passo 1 - Entrar na página do jogo e inicia-lo
webbrowser.open('https://gameforge.com/en-US/littlegames/magic-piano-tiles/')
sleep(3.5)
pyautogui.click(x=559, y=406, duration=1.3) 
sleep(0.6)
pyautogui.click(x=392, y=478, duration=1.5)
sleep(4.0)
image_x = pyautogui.locateCenterOnScreen('./assets/x.png')
pyautogui.click(x=image_x[0], y=image_x[1], duration=1.5)
sleep(1)
start = pyautogui.locateCenterOnScreen('./assets/start.png')
pyautogui.click(x=start[0], y=start[1], duration=1)

def clicar(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Passo 2 - Lógica do jogo, clicar com o mouse quando tiver a cor preta na coordenada
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(458, 338, (0, 0, 0)):
        clicar(458, 338)
    if pyautogui.pixelMatchesColor(524, 338, (0, 0, 0)):
        clicar(524, 338)
    if pyautogui.pixelMatchesColor(588, 338, (0, 0, 0)):
        clicar(588, 338)
    if pyautogui.pixelMatchesColor(650, 338, (0, 0, 0)):
        clicar(650, 338)