# MyHomeApp v0.1p (2022) - Ali
# MyHome is a home management app, specifically tailored for my home.
# ===================================================================
# This first version is a prototype to see what works well and what does not.
# At this point, I am still unsure about what I want to do with this project; I don't know if I want to make it public, if it has to be "other-users friendly", etc.
# I am still learning Python as I am developing this app so bugs and unoptimized code are expected. 
# I want to go with a Windows Aero-like design (Windows 7 wallpaper, WLM 2012-era, Windows Vista weather widget, glass, thin Segoe-like fonts, ...)
# === Features per version : ===
# v0.1p : design prototype
# v0.2a : networking, client/server architecture
# v0.3a : hardware integration
# v0.4a : wallpaper and weather(fixed picture, dynamic wallpaper according to the current weather)
# v0.5a : dark mode at sunset
# v0.6a : parameters charts (temperatures, humidity, ...)
# v0.7a : écowatt
# v0.8a : settings screen

# Libraries imports
import pygame
import sockets
import threading
import datetime
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
t_livingroom = 22
t_room1 = 23
t_room2 = 24
t_kitchen = 25
time = "notset"

# Fonctions
def server():
    call(["python3", "server.py"])

def get_time():
    time = datetime.datetime.now()
    time = time.strftime("%H:%M:%S")
    return time

def get_date():
    date = datetime.datetime.today()
    date = date.strftime("%B %d, %Y")
    return date

def interface():
    screen.blit(default_wallpaper, (0, 0))
    screen.blit(livingroom_str, (16, 16))
    screen.blit(temp_livingroom, (16, 40))
    screen.blit(room1_str, (16, 144))
    screen.blit(temp_room1, (16, 172))
    screen.blit(room2_str, (16, 276))
    screen.blit(temp_room2, (16, 304))
    screen.blit(time_str, (360, 16))
    screen.blit(date_str, (360, 64))
    screen.blit(placeholder64png, (128, 40)) # Temperature icon
    screen.blit(placeholder64png, (128, 172)) # Temperature icon
    screen.blit(placeholder64png, (128, 304)) # Temperature icon
    # screen.blit(placeholder64png, (16, 16))
    # screen.blit(placeholder128png, (480, 16))
    # pygame.draw.line(screen, black, (0, 240), (640, 240))

# Screen and loading assets
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MyHome App v0.1p")
placeholder64png = pygame.image.load("assets/placeholder64.png")
placeholder128png = pygame.image.load("assets/placeholder128.png")
default_wallpaper = pygame.image.load("assets/interface_default.png")
livingroom_str = font32.render("Living room", True, black) # Don't forget to render these strings/values in a function in future versions
temp_livingroom = font128.render(str(t_livingroom), True, black)
room1_str = font32.render("Children's room", True, black)
temp_room1 = font128.render(str(t_room1), True, black)
room2_str = font32.render("Parents' room", True, black)
temp_room2 = font128.render(str(t_room2), True, black)
# time_str = font64.render((time), True, black)
# kitchen_str = font32.render("Kitchen", True, black)
# temp_kitchen = font128.render(str(t_kitchen), True, black)

# Launch server
serverThread = threading.Thread(target=server)
serverThread.start()

# Main loop
while True:
    time_str = font64.render((get_time()), True, black)
    date_str = font32.render((get_date()), True, black)
    interface()
    pygame.display.flip()
    for event in pygame.event.get():
        print(get_time())
    if event.type == pygame.QUIT:
        break
