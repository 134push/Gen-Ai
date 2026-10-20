import time

spinner = ["|", "/", "-", "\\"]

print("Downloading File...")

for i in range(101):
    filled = "█" * (i // 2)
    empty = "░" * (50 - (i // 2))

    spin = spinner[i % len(spinner)]

    print(f"\r{spin} [{filled}{empty}] {i}%", end="", flush=True)
    time.sleep(0.05)

print("\n\n✅ Download Completed Successfully!")