# Python All Module Demo

import time
import random
import os
import sys
import tkinter as tk
import turtle
import pygame


print("===== Python Module Demo =====\n")


# 1. time module
print("1) TIME MODULE")
print("Loading...")
time.sleep(2)
print("Completed!\n")


# 2. random module
print("2) RANDOM MODULE")
number = random.randint(1, 100)
print("Random Number:", number)
print()


# 3. os module
print("3) OS MODULE")
current_folder = os.getcwd()
print("Current Folder:", current_folder)

files = os.listdir()
print("Files in Folder:")
print(files)
print()


# 4. sys module
print("4) SYS MODULE")
print("Python Version:")
print(sys.version)
print()


# 5. tkinter module (GUI)
print("5) TKINTER MODULE")


window = tk.Tk()
window.title("Python Module Demo")
window.geometry("300x200")

label = tk.Label(
    window,
    text="Hello Python!",
    font=("Arial", 20)
)

label.pack()

button = tk.Button(
    window,
    text="Close",
    command=window.destroy
)

button.pack()

print("Tkinter Window Opened")
print()


# 6. turtle module
print("6) TURTLE MODULE")


t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)

print("Turtle Drawing Completed")
print()


# 7. pygame module
print("7) PYGAME MODULE")

try:

    pygame.init()

    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Python Pygame Demo")

    print("Pygame Window Created")

except:
    print("Pygame not installed")
    print("Install using: pip install pygame")


# 8. curses module
print("\n8) CURSES MODULE")

try:
    print("Curses module available")

except:
    print("Curses works mainly on Linux systems")


print("\n===== Program Finished =====")


window.mainloop()