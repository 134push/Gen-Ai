import time
spinner = ["|", "/", "-", "\\"]

for i in range(100):
    print("\r " + spinner[i % len(spinner)], end="")
    print(f"downloading ... {i}%", end="")
    time.sleep(0.05)
    