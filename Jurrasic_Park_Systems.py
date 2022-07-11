
import time


print("Jurassic Park, System Security Interface")
print("Version 4.0.5, Alpha E")
print("Ready...")

a = input()

if "access" in a:
    print("access: PERMISSION DENIED")

b = input()

if "access" in b:
    print("access: PERMISSION DENIED")

c = input()

if "access" in c:
    print("access: PERMISSION DENIED....and....")

time.sleep(.2)

i = 1

while i < 10:
    print("YOU DIDN'T SAY THE MAGIC WORD!!!")
    time.sleep(.1)
    i = i + 1


time.sleep(20)
