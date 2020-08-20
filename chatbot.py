from datetime import datetime
from webbrowser import open

helloIntent = ["hi", "hello", "hola", "vanakkam", "hey there"]
greetIntent = ["I am fine", "I am good", "I am okay. What about you?"]
timeIntent = ["what's the time", "tell me time please", "time please"]

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
