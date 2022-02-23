from tkinter import *
import pytz
import time
from datetime import datetime 
import time
from PIL import Image, ImageTk

#setting up the GUI main window and title
window = Tk()
window.geometry("600x300")
window.title("Rie's World Clock")

def times():
    home=pytz.timezone("Asia/Istanbul")
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    clock.config(text=current_time)

    home=pytz.timezone("US/Pacific")
    local_time2=datetime.now(home)
    current_time2=local_time2.strftime("%H:%M:%S")
    clock2.config(text=current_time2)
    
    home3=pytz.timezone("Europe/Dublin")
    local_time3=datetime.now(home3)
    current_time3=local_time3.strftime("%H:%M:%S")
    clock3.config(text=current_time3)
    
    home4=pytz.timezone("Australia/Sydney")
    local_time4=datetime.now(home4)
    current_time4=local_time4.strftime("%H:%M:%S")
    clock4.config(text=current_time4)
    
    home5=pytz.timezone("Asia/Tokyo")
    local_time5=datetime.now(home5)
    current_time5=local_time5.strftime("%H:%M:%S")
    clock5.config(text=current_time5)
    
    home6=pytz.timezone("Asia/Bangkok")
    local_time6=datetime.now(home6)
    current_time6=local_time6.strftime("%H:%M:%S")
    clock6.config(text=current_time6)
    
    clock.after(200,times)


#time zone grid of 3 by 4
for rows in range(0,4):
    window.rowconfigure(rows, weight=1, minsize=20)
    window.columnconfigure(rows, weight=2, minsize=20)
    

    for columns in range(0,3):
        frame = Frame(
            master=window,
            relief=RAISED,
            borderwidth=1,
        )
        frame.grid(row=rows, column=columns, padx=50, pady=50)

#time zone 1: Kchan
clock = Label(master=window,font=("times", 30))
clock.grid(row=0, column=0)
    
img_1=Image.open("world clock/world-clock/Flag_of_Turkey.svg.png")
img_1=img_1.resize((60,40))
size = 40,40
img_1.thumbnail(size)
img_1 = ImageTk.PhotoImage(img_1)
    
label1 = Label(font=("times", 25),text=" KCHAN", image=img_1, compound=LEFT)
label1.grid(row=1, column=0)
label1.image=img_1

#time zone 2: Cherishie
clock2 = Label(font=("times", 30), fg="white", compound=TOP)
clock2.grid(row=0, column=1)

img_2=Image.open("world clock/world-clock/1600px-Flag_of_the_United_States.svg.png")
img_2=img_2.resize((60,40))
img_2.thumbnail(size)
img_2 = ImageTk.PhotoImage(img_2)

label2 = Label(font=("times", 25),text=" CHERISHIE", image=img_2, compound=LEFT)
label2.grid(row= 1, column=1)
label2.image=img_2

#time zone 3: Sharon

clock3 = Label(font=("times", 30), fg="white", compound=TOP)
clock3.grid(row=0, column=2)

img_3=Image.open("world clock/world-clock/1280px-Flag_of_Ireland.svg.png")
img_3=img_3.resize((60,40))
img_3.thumbnail(size)
img_3 = ImageTk.PhotoImage(img_3)

label3 = Label(font=("times", 25),text= " SHARON", image=img_3, compound=LEFT)
label3.grid(row=1, column=2)
label3.image=img_3

#time zone 4: Dan
clock4 = Label(font=("times", 30), fg="white", compound=TOP)
clock4.grid(row=2, column=0)

img_4=Image.open("world clock/world-clock/Flag_of_Australia.svg.png")
img_4=img_4.resize((60,40))
img_4.thumbnail(size)
img_4 = ImageTk.PhotoImage(img_4)

label4 = Label(font=("times", 25),text=" DAN", image=img_4, compound=LEFT)
label4.grid(row=3, column= 0)
label4.image=img_4

#time zone 5 : ME

clock5 = Label(font=("times", 30), fg="white", compound=TOP)
clock5.grid(row=2, column=1)

img_5=Image.open("world clock/world-clock/japan-flag.png")
img_5=img_5.resize((60,40))
img_5.thumbnail(size)
img_5 = ImageTk.PhotoImage(img_5)

label5 = Label(font=("times", 25),text=" ME!", image=img_5, compound=LEFT)
label5.grid(row=3, column=1)
label5.image=img_5

#time zone 6: Day

clock6 = Label(font=("times", 30), fg="white", compound=TOP)
clock6.grid(row=2, column=2)

img_6=Image.open("world clock/world-clock/1280px-Flag_of_Thailand.svg.png")
img_6=img_6.resize((60,40))
img_6.thumbnail(size)
img_6 = ImageTk.PhotoImage(img_6)

label6 = Label(justify=LEFT, font=("times", 25),text =" DAY", image=img_6, compound=LEFT)
label6.grid(row=3, column=2)
label6.image=img_6

times()

window.mainloop()