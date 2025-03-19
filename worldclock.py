from tkinter import *
import pytz
from datetime import datetime
from PIL import Image, ImageTk

# Setting up the GUI main window and title
window = Tk()
window.geometry("800x400")
window.title("Rie's World Clock")

def update_time():
    for i, (zone, _, _) in enumerate(timezones):
        local_time = datetime.now(pytz.timezone(zone)).strftime("%H:%M:%S")
        time_labels[i].config(text=local_time)
    
    window.after(200, update_time)

# Timezones with city names and flag paths
timezones = [
    ("Asia/Istanbul", "KCHAN", "world clock/world-clock/Flag_of_Turkey.svg.png"),
    ("US/Pacific", "CHERISHIE", "world clock/world-clock/1600px-Flag_of_the_United_States.svg.png"),
    ("Europe/Dublin", "SHARON", "world clock/world-clock/1280px-Flag_of_Ireland.svg.png"),
    ("Australia/Sydney", "DAN", "world clock/world-clock/Flag_of_Australia.svg.png"),
    ("Asia/Tokyo", "ME!", "world clock/world-clock/japan-flag.png"),
    ("Asia/Bangkok", "DAY", "world clock/world-clock/1280px-Flag_of_Thailand.svg.png"),
]

time_labels = []

# Adjusting grid size
for row in range(2):
    window.rowconfigure(row, weight=1, minsize=150)
for col in range(3):
    window.columnconfigure(col, weight=1, minsize=150)

# Creating the frames for each time zone
for i, (zone, name, img_path) in enumerate(timezones):
    row, col = divmod(i, 3)

    frame = Frame(master=window, relief=RAISED, borderwidth=3, width=150, height=120)
    frame.grid(row=row, column=col, padx=5, pady=5)  # Less padding

    img = Image.open(img_path)
    img = img.resize((60, 40))  # Bigger image
    img = ImageTk.PhotoImage(img)

    img_label = Label(frame, image=img)
    img_label.image = img
    img_label.pack(side=TOP, pady=5)  # Less vertical space

    name_label = Label(frame, text=name, font=("times", 18, "bold"))
    name_label.pack(side=TOP, pady=2)

    time_label = Label(frame, text="--:--:--", font=("times", 20, "bold"))
    time_label.pack(side=TOP, pady=5)

    time_labels.append(time_label)

# Start updating time
update_time()

window.mainloop()
