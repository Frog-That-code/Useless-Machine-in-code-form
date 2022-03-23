import os, platform
def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

print("Type on")

while True:
    Status = input("Off ")
    clear()
    if Status == "q":
        break
