from datetime import datetime
from webbrowser import open
import os
from subprocess import call
from random import choice

helloIntent = ["hi", "hello", "hola", "vanakkam", "hey there"]
greetIntent = ["I am fine", "I am good", "I am okay. What about you?"]
timeIntent = ["what's the time", "tell me time please", "time please"]
songsIntent = ["play a song", "play something for me", "play a random song"]

while True:
    userMessage = input("Enter your message: ")
    if userMessage in helloIntent:
        print("Hello, user.")
        print("How are you, today?")
    elif userMessage in greetIntent:
        print("I am also fine... Tell me something more")
    elif userMessage.startswith("open"):
        # open google
        # open github
        websiteName = userMessage.split()[1]
        open(f"https://www.{websiteName}.com")
    elif userMessage in songsIntent:
        os.chdir('/Users/anmolrajarora/Google Drive/Work/2020/Songs/')
        print(os.getcwd())
        # os.chdir("C:/Users/Ram/Documents/Songs/")
        # os.chdir("C:\\Users\\Ram\\Documents\\Songs\\")
        songs = os.listdir()
        print('''
            1. Play a random song
            2. Show all songs
        ''')
        userMessage = input("Please enter your choice: ")
        if userMessage == "1":
            current_song = choice(songs)
            # os.startfile(current_song)
            call(["open", current_song])
        elif userMessage == "2":
            for counter, song in enumerate(songs):
                print(f"{counter+1}. {song}")
            print("Press 0 to exit music player...")
            while True:
                userMessage = int(input("Which one do you want to play: "))
                if userMessage == 0:
                    break
                songIndex = userMessage - 1
                call(["open", songs[songIndex]])
        else:
            print("I don't understand")
    elif userMessage in timeIntent:
        print(datetime.now().strftime("%a %d %b %Y %H:%M:%S"))
        # print(datetime.now().strftime("%a"))
        # print(datetime.now().strftime("%A"))
        # print(datetime.now().strftime("%b"))
        # print(datetime.now().strftime("%B"))
        # print(datetime.now().strftime("%c"))
        # print(datetime.now().strftime("%d"))
        # print(datetime.now().strftime("%m"))
        # print(datetime.now().strftime("%M"))
        # print(datetime.now().strftime("%H"))
        # print(datetime.now().strftime("%S"))
        # print(datetime.now().strftime("%y"))
        # print(datetime.now().strftime("%Y"))
    elif userMessage == "bye":
        print("See you later.")
        break
    else:
        print("I don't understand")
