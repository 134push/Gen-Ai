for i in range(5):
    if i == 2:
        pass
    print(i)

subjects = ["Python","C","Java"]
for index, subject in enumerate(subjects):
    print(index, subject)   

import time
for i in range(100):
    print(".", end="",flush=True)
    time.sleep(0.05)

attempt = 1
while attempt <= 3:
    password = input("Password : ")
    if password == "python":
        print("Success")
        break
    attempt += 1
else:
    print("Failed 3 Times")
