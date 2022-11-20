# MyHomeApp v0.1
# MyHome is a home management app, specifically tailored for my home.
# ===================================================================
# This first version is a prototype to see what works well and what does not.
# At this point, I am still unsure about what I want to do with this project; I don't know if I want to make it public, if it has to be "other-users friendly", etc.
# I am still learning Python as I am developing this app so bugs and unoptimized code are expected. 
# I want to go with a Windows Aero-like design (Windows 7 wallpaper, WLM 2012-era, Windows Vista weather widget, glass, thin Segoe-like fonts, ...)
# ❤️

# -- Imports --
import logging
import pygame
import socket
import threading
import datetime
from subprocess import call

# -- Variables --
connected = False
width = 640
height = 480
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
t_livingroom = 0
t_room1 = 0
t_room2 = 0
h_livingroom = 0
h_room1 = 0
h_room2 = 0
time = "00:00 (notset)"

# -- Fonctions --
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
    mainwindow.blit(default_wallpaper, (0, 0))
    mainwindow.blit(livingroom_t_str, (16, 16))
    mainwindow.blit(temp_livingroom, (16, 20)) #
    mainwindow.blit(humidity_livingroom, (172, 20))
    mainwindow.blit(room1_t_str, (16, 144))
    mainwindow.blit(temp_room1, (16, 152)) #
    mainwindow.blit(humidity_room1, (172, 152))
    mainwindow.blit(room2_t_str, (16, 276))
    mainwindow.blit(temp_room2, (16, 284)) #
    mainwindow.blit(humidity_room2, (172, 284))
    mainwindow.blit(time_str, (360, 16))
    mainwindow.blit(date_str, (360, 80))

# -- Screen --
pygame.init()
mainwindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("MyHome App v0.2a")

# -- Assets --
default_font16 = pygame.font.Font(None, 16)
default_font32 = pygame.font.Font(None, 32)
default_font64 = pygame.font.Font(None, 64)
default_font128 = pygame.font.Font(None, 128)
haskoy_extralight32 = pygame.font.Font("assets/fonts/Haskoy-ExtraLight.otf", 32)
haskoy_medium64 = pygame.font.Font("assets/fonts/Haskoy-Medium.otf", 64)
haskoy_medium128 = pygame.font.Font("assets/fonts/Haskoy-Medium.otf", 128)
haskoy_bold128 = pygame.font.Font("assets/fonts/Haskoy-Bold.otf", 128)
placeholder64png = pygame.image.load("assets/img/placeholder64.png")
placeholder128png = pygame.image.load("assets/img/placeholder128.png")
default_wallpaper = pygame.image.load("assets/img/interface_default.png")
livingroom_t_str = haskoy_extralight32.render("Living room", True, black) # Don't forget to render these strings/values in a function in future versions
humidity_livingroom = haskoy_medium128.render(str(h_livingroom), True, black)
temp_livingroom = haskoy_bold128.render(str(t_livingroom), True, black)
room1_t_str = haskoy_extralight32.render("Children's room", True, black)
humidity_room1 = haskoy_medium128.render(str(h_room1), True, black)
temp_room1 = haskoy_bold128.render(str(t_room1), True, black)
room2_t_str = haskoy_extralight32.render("Parents' room", True, black)
humidity_room2 = haskoy_medium128.render(str(h_room2), True, black)
temp_room2 = haskoy_bold128.render(str(t_room2), True, black)

# -- Launch server --
serverThread = threading.Thread(target=server)
serverThread.start()


# -- Main loop --
while True:
    time_str = haskoy_medium64.render((get_time()), True, black)
    date_str = haskoy_extralight32.render((get_date()), True, black)
    interface()
    pygame.display.flip()
    for event in pygame.event.get():
        print(get_time())
        x, y = pygame.mouse.get_pos()
        print(x,y)
    if event.type == pygame.QUIT:
        break