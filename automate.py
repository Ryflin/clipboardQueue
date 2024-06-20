import pynput
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

# hardcoded queue
# queue = ["Daniel Schley", "schleyflies@gmail.com", "4199890281", "Cessna 172N", "N733KB", "C1759305", "4771093", "JonathanJones", "4199893853", "jonjones1333@gmail.com" ]
# ids = ["00000000-0000-0000-0000-000000000001-input", "00000000-0000-0000-0000-000000000002-input", "label-for-id-155", "34d8da14-b8ee-45df-a235-ce9134d42a17-input", "ce09ebbe-1af4-470f-be59-a43fb4458849-input", "baeb1be3-e788-4f49-9360-fb66bd085266-input", "1e22e7f3-c905-4e4b-a62a-8f0411f5bacb-input", "cbc0f3d4-4633-4bde-8d50-c8199e118e45-input", "b5388cbb-386d-4633-8ab2-ac4537c0feb6-input", "ef6f90c1-e9a4-4434-be49-cf2ac968441f-input"]

queue = []
try:
  with open("automate.json", "r") as f:
    queue = json.load(f)
except:
  print("It looks like there is nothing in the input queue\n")

  qu = {"value": input("Enter an item, press q then ENTER to exit: "), "id": input("Enter the id of the item: ")}
  while qu["value"] != "q" and qu["id"] != "q":
    queue.append(qu)
    qu = {"value": input("Enter an item, press q then ENTER to exit: "), "id": input("Enter the id of the item: ")}
  json.dump(queue, open("automate.json", "w"))

print(queue)
def fill_form2():
  global queue, ids
  web = webdriver.Firefox()
  site = web.get("https://www.ohiopilotexaminer.com/booking-calendar/cfi-amel-asel-added-class?referral=service_list_widget")
  while "booking-form" not in web.current_url:
    time.sleep(.1)
  time.sleep(.5)

  try:
    elements = web.find_elements(By.CLASS_NAME, "sk7DQ7V")
    if len(elements) > 2:
      elements[2].send_keys("+1")
  except Exception as e:
    print(e, '\n')
    pass
  for i in range(0, len(queue)):
    web.find_element(By.ID, queue[i]["id"]).send_keys(queue[i]["value"])
  # try the two checkboxes
  try:
    checkbox = web.find_element(By.ID, "checkbox-160")
    checkbox.send_keys(" ")
  except Exception as e:
    print(e, '\n')
    pass
  try:
    web.find_element(By.ID, "checkbox-177").send_keys(" ")
  except Exception as e:
    print(e, '\n')
    pass
  
fill_form2()  

user_input = input("Press s to start listener for p, q to quit: ")
while user_input != "q":
  # listener.start()
  fill_form2()
  user_input = input("Press s to start listener for p, q to quit: ")