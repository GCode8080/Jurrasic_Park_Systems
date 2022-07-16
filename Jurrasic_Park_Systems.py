import time

print("Jurassic Park, System Security Interface")
print("Version 4.0.5, Alpha E")
print("Ready...")

count = 0

a = input()

if "please" in a:
    print("perhaps ;)")
elif "access" in a:
    print("access: PERMISSION DENIED")
    count = count + 1
else:
    print("no")

b = input()

if "please" in b:
    print("perhaps ;)")
elif "access" in b:
    print("access: PERMISSION DENIED")
    count = count + 1
else:
    print("no")

c = input()

if "please" in c:
    print("perhaps ;)")
elif "access" in c:
    print("access: PERMISSION DENIED....and....")
    time.sleep(.2)
    repeatTimes = 10
    i = 1

    while i < repeatTimes:
        print("YOU DIDN'T SAY THE MAGIC WORD!!!")
        time.sleep(.1)
        i = i + 1
else:
    print("no")

time.sleep(20)
