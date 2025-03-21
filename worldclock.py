from tkinter import *
import pytz
from datetime import datetime
from PIL import Image, ImageTk

# Setting up the GUI main window and title
window = Tk()
window.geometry("800x400")
window.title("Rie's World Clock")

def update_time():
    timezones = [
        ("Asia/Istanbul", "KCHAN", "world clock/world-clock/Flag_of_Turkey.svg.png"),
        ("US/Pacific", "CHERISHIE", "world clock/world-clock/1600px-Flag_of_the_United_States.svg.png"),
        ("Europe/Dublin", "SHARON", "world clock/world-clock/1280px-Flag_of_Ireland.svg.png"),
        ("Australia/Sydney", "DAN", "world clock/world-clock/Flag_of_Australia.svg.png"),
        ("Asia/Tokyo", "ME!", "world clock/world-clock/japan-flag.png"),
        ("Asia/Bangkok", "DAY", "world clock/world-clock/1280px-Flag_of_Thailand.svg.png"),
    ]

    for i, (zone, name, img_path) in enumerate(timezones):
        local_time = datetime.now(pytz.timezone(zone)).strftime("%H:%M:%S")
        time_labels[i].config(text=local_time)

    window.after(200, update_time)

# List to hold time labels
time_labels = []

# Creating a grid layout
for row in range(2):
    window.rowconfigure(row, weight=1, minsize=100)
for col in range(3):
    window.columnconfigure(col, weight=1, minsize=100)

# Adding time zones to the GUI
for i, (zone, name, img_path) in enumerate([
    ("Asia/Istanbul", "KCHAN", "world clock/world-clock/Flag_of_Turkey.svg.png"),
    ("US/Pacific", "CHERISHIE", "world clock/world-clock/1600px-Flag_of_the_United_States.svg.png"),
    ("Europe/Dublin", "SHARON", "world clock/world-clock/1280px-Flag_of_Ireland.svg.png"),
    ("Australia/Sydney", "DAN", "world clock/world-clock/Flag_of_Australia.svg.png"),
    ("Asia/Tokyo", "ME!", "world clock/world-clock/japan-flag.png"),
    ("Asia/Bangkok", "DAY", "world clock/world-clock/1280px-Flag_of_Thailand.svg.png"),
]):
    row, col = divmod(i, 3)

    frame = Frame(master=window, relief=RAISED, borderwidth=2, padx=10, pady=10)
    frame.grid(row=row, column=col, padx=10, pady=10)

    img = Image.open(img_path)
    img = img.resize((50, 30))
    img = ImageTk.PhotoImage(img)

    img_label = Label(frame, image=img)
    img_label.image = img
    img_label.pack(side=TOP)

    name_label = Label(frame, text=name, font=("times", 20))
    name_label.pack(side=TOP)

    time_label = Label(frame, text="--:--:--", font=("times", 25))
    time_label.pack(side=TOP)

    time_labels.append(time_label)

# Start updating time
update_time()

window.mainloop()
