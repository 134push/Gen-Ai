## Countdown Time
import time
counting_number = int(input("enter a number : "))

while counting_number > 0:
    print(counting_number)
    counting_number -= 1
    time.sleep(0.8)

print("Blast Off!")