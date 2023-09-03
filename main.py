
import pyperclip
import pyautogui

while True:
    cod = input("Insira o código:")
    if len(cod) == 8:
            pyperclip.copy(cod)
            pyautogui.doubleClick(x=1275, y=715)
            pyautogui.doubleClick (x=1236, y=47)
            pyautogui.sleep(3)
            pyautogui.doubleClick(x=635, y=397)
            pyautogui.press ( 'd' )
            pyautogui.sleep(1)
            pyautogui.press ( 'enter' )
            pyautogui.sleep ( 5 )
            pyautogui.doubleClick ( x=635, y=397 )
            pyautogui.hotkey ( 'ctrl', 'v' )
            pyautogui.hotkey ( 'ctrl', 'p' )
            pyautogui.press ( 'enter' )