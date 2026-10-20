# 3. EV Battery System

battery = float(input("Enter Battery Percentage (%): "))

if battery > 80:
    print("Status: Excellent")
elif battery >= 50:
    print("Status: Good")
elif battery >= 20:
    print("Status: Low")
else:
    print("Status: Charge Immediately")
