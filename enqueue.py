import pyperclip
import json
from pynput import keyboard
from pynput.keyboard import Controller

keyControl = Controller()
queue = []
try:
  with open("queue.json", "r") as f:
    queue = json.load(f)
except:
  print("It looks like there is nothing in the input queue\n")
  qu = input("Enter an item, press q then ENTER to exit: ")
  while qu != "q":
    queue.append(qu)
    qu = input("Enter an item, press q then ENTER to exit: ")
  json.dump(queue, open("queue.json", "w"))
i = 0
print(queue)
def on_release(key: keyboard.KeyCode):
  if key == keyboard.Key.esc:
    return False

def on_press(key: keyboard.KeyCode):
  global i
  try:
    if key == keyboard.Key.ctrl_l:
      if i == len(queue):
        i = 0
      pyperclip.copy(queue[i])
      keyControl.press('v')
      keyControl.release('v')
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