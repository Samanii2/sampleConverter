import ffmpeg
from tkinter import *
import os
from tkinter.filedialog import askopenfilename
import sys


def WAVtoMP3():
      lst = [filename]
      for file in lst:
	os.system(f"""ffmpeg -i {file} -vn -ar 44100 -ac 2 -b:a 192k {file[:-4]}.mp3""")

def browseFile():
      global filename
      filename = askopenfilename()

#GUI
root = Tk()
root.title("Sample Converter Alpha 0.1")

labelHeader = Label(root, text="Sample Converter")
labelHeader.config(font=("Courier", 25))
labelHeader.grid(row=0 ,column=1)

labelInstruction = Label(root, text="Browse sample to convert.")
labelInstruction.config(font=("Courier", 10))
labelInstruction.grid(row=1, column=1)

buttonSort = Button(text="Convert", command = WAVtoMP3)
buttonSort.grid(row=4, column=2)
                      
removing = StringVar()
labelRemoved = Label(master=root,textvariable=removing)
labelRemoved.grid(row=5, column=1)

buttonBrowse = Button(text="Browse", command = browseFile)
buttonBrowse.grid(row=3, column=2)

mainloop()
