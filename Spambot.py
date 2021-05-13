import pyautogui
import time
import webbrowser as wb

a_string = "Subscribe to TBK \n"
f = open("spam",'w')
for line in range(2):
    result = a_string
    f.write(result)
    
time.sleep(2)
wb.open('web.whatsapp.com')
time.sleep(5)
f = open("spam", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")