import pynput
from selenium import webdriver
from selenium.webdriver.common.by import By

# hardcoded queue
queue = ["Daniel Schley", "schleyflies@gmail.com", "4199890281", "Cessna 172N", "N733KB", "C1759305", "4771093", "JonathanJones", "4199893853", "jonjones1333@gmail.com" ]
ids = ["00000000-0000-0000-0000-000000000001-input", "00000000-0000-0000-0000-000000000002-input", "label-for-id-155", "34d8da14-b8ee-45df-a235-ce9134d42a17-input", "ce09ebbe-1af4-470f-be59-a43fb4458849-input", "baeb1be3-e788-4f49-9360-fb66bd085266-input", "1e22e7f3-c905-4e4b-a62a-8f0411f5bacb-input", "cbc0f3d4-4633-4bde-8d50-c8199e118e45-input", "b5388cbb-386d-4633-8ab2-ac4537c0feb6-input", "ef6f90c1-e9a4-4434-be49-cf2ac968441f-input"]


def fill_form2():
  global queue, ids
  web = webdriver.Firefox()
  site = web.get("http://127.0.0.1:5500/formSite/Booking%20Form%20_%20Ohio%20Pilot%20Examiner2_files/Booking%20Form%20_%20Ohio%20Pilot%20Examiner2%20copy.html")
  # web.find_element(By.ID, "checkbox-180").click()
  # web.find_element(By.ID, "checkbox-177")
  for i in range(0, len(queue)):
    web.find_element(By.ID, ids[i]).send_keys(queue[i])
  
fill_form2()  

def fill_form():
  global queue
  controller = pynput.keyboard.Controller()
  for i in range(0, 10):
    controller.press(pynput.keyboard.Key.tab)
    controller.release(pynput.keyboard.Key.tab)
  for i in queue:
    controller.type(i)
    controller.press(pynput.keyboard.Key.tab)
    controller.release(pynput.keyboard.Key.tab)
  controller.type("\n")

def on_presss(key: pynput.keyboard.Key):
  try:
    if key.char == "p":
      fill_form()
    if key.char == "q":
      return False
  except AttributeError:
    pass

listener = pynput.keyboard.Listener(on_press=on_presss)
user_input = input("Press s to start listener for p, q to quit: ")
while user_input != "q":
  listener.start()
  user_input = input("Press s to start listener for p, q to quit: ")