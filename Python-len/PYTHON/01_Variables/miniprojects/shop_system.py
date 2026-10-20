import time

print("===================================")
time.sleep(0.3)
print("      SHOP MANAGEMENT SYSTEM")
time.sleep(0.3)
print("===================================")
time.sleep(0.3)

print("System is loading...")
time.sleep(0.5)
print("Loading complete!")

# Security System State Variables
camera = "open"
sos_system = "active"
alarm_system = "active"
time.sleep(0.3)
print(f"camera = {camera} \nsos_system = {sos_system} \nalarm_system = {alarm_system}")
time.sleep(0.2)
print(".")
time.sleep(0.2)
print(".")
time.sleep(0.2)
print("System is ready to use!")

time.sleep(0.5)
shop_time = "23:45"
person_visible = 3
person_known_unknown = "unknown"
at_camera_person_visible = 2
time.sleep(0.5)

print("\n------- Alert Found --------")
time.sleep(0.2)

print("\n")
print(f"Time: {shop_time}")
print(f"At camera no {at_camera_person_visible}, visible persons: {person_visible}.")
print(f"The person status is: {person_known_unknown}.\n")

print("========================================")
time.sleep(0.3)
print("      Alert message sending.....")
time.sleep(0.3)
print("========================================")
time.sleep(0.3)

alarm = "on"
message_sending = True

print(f"The alarm system is {alarm}. \nMessage sending to the owner: {message_sending}")
