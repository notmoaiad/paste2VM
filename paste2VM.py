import pyperclip
from pyautogui import typewrite
from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()

s = pyperclip.paste()
keyboard.press(".")
keyboard.release(".")
keyboard.press(Key.backspace)
keyboard.release(Key.backspace)
req_shift = "_#$@:!%^&*()+`'\"><?|{}"
for l in s:
	if l in req_shift or l.isupper():
		keyboard.press(Key.shift)
	keyboard.press(l)
	keyboard.release(l)
	keyboard.release(Key.shift)
	#sleep(.1)
