from time import sleep 
import pyautogui as pya

while True:
    x, y = pya.position()
    print(f"Posição X: {x}\nPosição Y: {y}")

    sleep(2)
