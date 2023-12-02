# 🏠 MyHome

**MyHome is a home management app, specifically tailored for my home.**

This first version is a prototype to see what works well and what does not. At this point, I am still unsure about what I want to do with this project; I don't know if I want to make it public, if it has to be "other-users friendly", etc.

## ❓ What is MyHome?
MyHome is a home management app designed for a **station** that is itself connected to multiple **probers** in different rooms of your household. The probers will collect information about the air quality, current temperature and humidity. The station then gathers the data provided by the probers and displays them in real-time. 

## 🧐 What does PyHome currently do?
The temperatures displayed are hard-coded (and thus, fake): they aren't referring to real temperatures. The only real-time value here is the time and date. I am unsure about the layout though.

## 🤔 What will happen next?
The next version will feature data communication in real-time. It will be able to send data, such as the current temperature, from clients (located in different rooms, one per room) to the server (the "station"). 

## How to run the app?
Python 3 must be installed on your system (previous versions of Python may work but I haven't tested it) alongside with these libraries:

```
- pygame
- sockets
- threading
- datetime
- subprocess
```

⚠️ If you're missing one of these libraries, you can install them using either `pip install` or `pip3 install` commands (depends on your installation). For instance, if you need to install the pygame library:
`pip install pygame`

### macOS & Unix-based systems

1. Open the Terminal
2. Navigate to the unzipped folder using `cd`
3. Type `python3 app.py` and press Enter

### Windows
🛠
