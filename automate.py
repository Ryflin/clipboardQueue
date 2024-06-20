import pynput
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

queue = []
try:
  with open("automate.json", "r") as f:
    queue = json.load(f)
except:
  print("It looks like there is nothing in the input queue\n")
  qu =  input("Enter the next item: ")
  while qu != "q":
    queue.append(qu)
    qu = input("Enter an item, press q then ENTER to exit: ")
  json.dump(queue, open("automate.json", "w"))

print(queue)
def fill_form2():
  global queue, ids
  web = webdriver.Firefox()
  site = web.get("http://127.0.0.1:5500/formSite/index.html")
  while "booking-form" not in web.current_url:
    time.sleep(.1)
  time.sleep(.5)
  elements = web.find_elements(By.TAG_NAME, "input")
  for i in range(0, len(elements)):
    try:
      elements[i].send_keys(queue[i])
    except Exception as e:
      print(e, '\n')
      pass
fill_form2()  
user_input = input("Press s to start listener for p, q to quit: ")
while user_input != "q":
  # listener.start()
  fill_form2()
  user_input = input("Press s to start listener for p, q to quit: ")