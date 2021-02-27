import pyautogui as gui
import time

print("welcome to automatic typer 1.0.0 please input the type of typing this bot should do")
time.sleep(1)
print("please look inside the help document for more details.")
x = input("start type script number ")
y = input("repeat? ")

time.sleep(5)

f = open("script"+x, "r")

if ((y == 'y')or (y == 'Y')):
    while True:
        for word in f:
            time.sleep(0.3)
            gui.typewrite(word)
            gui.press("enter")

if ((y == 'n')or (y =='N')):
    for word in f:
        print("n passed")
        time.sleep(0.3)
        gui.typewrite(word)
        gui.press("enter")
