

import sys
import cv2
import os
from tkinter import *

window=Tk()

window.configure(background='AntiqueWhite1')
window.title("Running Python Script")
window.geometry('550x200')

def run():
    os.system('RENUM.py')

btn = Button(window, text="START RENUM CODE", bg="black", fg="white",command=run)
btn.grid(column=0, row=0)


window.mainloop()

