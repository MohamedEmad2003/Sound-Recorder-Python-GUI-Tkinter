from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from pathlib import Path
import shutil


root = Tk()
root.geometry("600x600+400+40")
root.resizable(False,False)
root.title("Voice Recorder")
root.configure(bg="#4a4a4a")


def destination():
    saved_file = filedialog.asksaveasfilename(
    filetypes=[("audio file", ".wav")],
    defaultextension=".wav")
    print(saved_file)
    audio_file_name=Path(saved_file).name
    print(Path(saved_file).name)
    print("\n here")
    print(audio_file_name)
    return audio_file_name,saved_file
    
    
        
   

def Record():
    freq=44100
    dur=int(duration.get())*60
    recording=sound.rec(dur*freq,samplerate=freq,channels=2)

    #timer
    try:
        temp=int(duration.get())*60
    except:
        print("please enter the right value")
    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1

        if (temp==0):
            messagebox.showinfo("Time Countdown", "Time's up")
        Label(text=f"{str(temp)}",font="arial 40",width=4,background="#4a4a4a").place(x=240,y=500)
    sound.wait()
    audio_file_name,saved_file = destination()
    write(audio_file_name,freq,recording)
    shutil.move(audio_file_name, saved_file) #to change file path


    

    
#icon
image_icon = PhotoImage(file="Record.png")
root.iconphoto(False, image_icon)

#logo
photo=PhotoImage(file="Record.png")
myimage=Label(image=photo,background="#4a4a4a")
myimage.pack(padx=5, pady=5)

#name
Label(text="Mohamed Emad \n Shoubra faculty of engineering",font="arial 11 bold", background="#4a4a4a", fg="white").place(x=6,y=6)
Label(text="Voice Recorder",font="arial 30 bold", background="#4a4a4a", fg="white").pack()

#entrybox
duration=StringVar()
entry=Entry(root,textvariable=duration,font="arial 30",width=15).pack(pady=10)
Label(text="Enter the duration to record in minutes",font="arial 15", background="#4a4a4a", fg="white").pack()

#button
record=Button(root,font="arial 20",text="Record",bg="#111",fg="white",border=0,command=Record).pack()


root.mainloop()
