import pyperclip
import json
import types
from pynput import keyboard
from pynput.keyboard import Controller

keyControl = Controller()
queue = []

with open("queue.json", "r") as f:
  queue = json.load(f)
i = 0
print(queue)
def on_release(key: keyboard.KeyCode):
  if key == keyboard.Key.esc:
    return False

def on_press(key: keyboard.KeyCode):
  global i
  try:
    if key == keyboard.Key.ctrl_r:
      if i == len(queue):
        i = 0
      pyperclip.copy(queue[i])
      keyControl.press(keyboard.Key.ctrl)
      keyControl.press('v')
      keyControl.release('v')
      keyControl.release(keyboard.Key.ctrl)
      i += 1
    if key ==  keyboard.Key.esc:
      return False
  except AttributeError:
    pass

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
terminate = ""
while terminate != "q":
  terminate = input("Input q to terminate program:  ")