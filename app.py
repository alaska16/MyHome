# MyHomeApp v0.1p (2022) - Ali
# MyHome is a home management app, specifically tailored for my home.
# ===================================================================
# This first version is a prototype to see what works well and what does not.
# At this point, I am still unsure about what I want to do with this project; I don't know if I want to make it public or not, if it has to be "other-users friendly".
# I am still learning this language as I am developing this app so bugs and unoptimized code are expected. 
# I want to go with a Windows Aero-like design (Windows 7 wallpaper, WLM 2012-era, Windows Vista weather widget, glass, thin Segoe-like fonts, ...)
# === Features per version : ===
# v0.1p : design prototype
# v0.2a : networking, client/server architecture
# v0.3a : hardware integration
# v0.4a : wallpaper and weather(fixed picture, dynamic wallpaper according to the current weather)
# v0.5a : dark mode at sunset
# v0.6a : parameters charts (temperatures, humidity, ...)
# v0.7a : écowatt

# Libraries imports
from concurrent.futures import thread
import pygame
import sockets
import threading
from subprocess import call
pygame.init()
print("Libraries are imported and initialized.") # Soon to be replaced with (import logging)

# Variables
width = 640
height = 480
white = (255, 255, 255)
black = (0, 0, 0)
font16 = pygame.font.Font(None, 16)
font32 = pygame.font.Font(None, 32)
font64 = pygame.font.Font(None, 64)
font128 = pygame.font.Font(None, 128)
t_livingroom = 0
t_room1 = 0
t_room2 = 0
t_kitchen = 0

# Fonctions
def server():
    call(["python3", "server.py"])

def interface():
    screen.blit(placeholder64png, (16, 16))
    screen.blit(placeholder64png, (480, 16))

# Screen and loading assets
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MyHome App v0.1p")
placeholder64png = pygame.image.load("assets/placeholder64.png")

# Launch server
serverThread = threading.Thread(target=server)
serverThread.start()

# Main loop
while True:
    for event in pygame.event.get():
        interface()
        pygame.display.flip()
    if event.type == pygame.QUIT:
        break
