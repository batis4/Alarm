from tkinter.ttk import *
from tkinter import *
from datetime import datetime

import _thread

import threading

from time import sleep

from pygame import mixer

from PIL import ImageTk, Image
#colors
bg_color = '#FFFFFF'
rr_color = '#9923e1'


window = Tk()
window.title(" ")
window.geometry('350x150')

#windows
window.configure(bg=bg_color)

#frames

frame_line = Frame(window, width=400, height=5, bg=rr_color)
frame_line.grid(row=0, column=0)

frame_body = Frame(window,width=400,height=290,bg= '#FFFFFF')
frame_body.grid(row=1,column=0)

#Configuring frame body
img = Image.open('icon.png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height= 100, image=img, bg='#FFFFFF')
app_image.place(x=10,y=10)

name = Label(frame_body,text='Alarm', height=1, font=('Ivy 18 bold'), bg='#FFFFFF', fg= '#cd78cd')

name.place(x=125,y=10)

hour = Label(frame_body,text=' hour', height=1, font=('Ivy 10 bold'), bg= '#ffffff', fg= '#c262b5')

hour.place(x=127,y=40)

c_hour = Combobox(frame_body, width=2, font= ('arial 17') )
c_hour['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12')
c_hour.current(0)
c_hour.place(x=130,y=58)

minutes = Label(frame_body,text='minute', height=1, font=('Ivy 10 bold'), bg= '#ffffff', fg= '#c262b5')
minutes.place(x=177,y=40)

c_minutes = Combobox(frame_body, width=2, font= ('arial 17') )
c_minutes['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12' , '13' , '14' ,
                       '15','16','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34'
                       ,'35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54',
                       '55','56','57','58','59','60')
c_minutes.current(0)
c_minutes.place(x=180,y=58)

seconds = Label(frame_body,text='second', height=1, font=('Ivy 10 bold'), bg= '#ffffff', fg= '#c262b5')
seconds.place(x=227,y=40)

G_seconds = Combobox(frame_body, width=2, font= ('arial 17') )
G_seconds['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12' , '13' , '14' ,
                       '15','16','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34'
                       ,'35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54',
                       '55','56','57','58','59','60')
G_seconds.current(0)
G_seconds.place(x=227,y=58)

period = Label(frame_body,text='period', height=1, font=('Ivy 10 bold'), bg= '#ffffff', fg= '#c262b5')
period.place(x=277,y=40)

G_period = Combobox(frame_body, width=3, font= ('arial 15') )
G_period['values'] = ('AM','PM')
G_period.current(0)
G_period.place(x=277,y=58)

def activate():
    t = threading.Thread(target=alarm)
    t.start()

def deactivate():
    print("Deactivated alarm: ", selected.get())
    mixer.music.stop()

selected = IntVar()

rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text='activate', bg='#FFFFFF', command=activate,
                       variable=selected)

rad1.place(x=125, y=95)

def sound_alarm():
    mixer.music.load('musical_alarm.mp3')
    mixer.music.play()
    selected.set(0)

    rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value=2, text='Deactivate', bg='#FFFFFF', command=deactivate,
                       variable=selected)
    rad2.place(x=210, y=95)

def alarm():
    while True:
        control = selected.get()
        print(control)

        alarm_hour= c_hour.get()
        alarm_minute = c_minutes.get()
        alarm_sec = G_seconds.get()
        alarm_period = G_period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time to take a break!")
                            sound_alarm()
        sleep(1)


mixer.init()
#frame_line.configure(bg=rr_color)
window.mainloop()