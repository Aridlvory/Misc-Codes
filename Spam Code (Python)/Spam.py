import pyautogui, time

i = 0
times = int(input("Number of times to spam: "))
msg = input("Enter the message to spam: ")

print("Spamming in...")
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

for i in range(times):
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
    print("Spam Count =",i)
