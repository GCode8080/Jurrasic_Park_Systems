
import time

i = 1000

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

while i > 1:
    print("YOU DIDN'T SAY THE MAGIC WORD!!!")
    time.sleep(.1)
    i+1


time.sleep(20)
