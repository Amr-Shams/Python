import os
import sys
import threading
from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from tkinter import font
from threading import Thread
from datetime import datetime
import ctypes
import time
from tkinter import filedialog
no_of_windows = 1
class StickyNotes(Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user32 = ctypes.windll.user32
        self.user32.SetProcessDPIAware()
        self.w =self.user32.GetSystemMetrics(0)
        self.h=self.user32.GetSystemMetrics(1)
        self.xclick = 0
        self.yclick = 0
        self.iconphoto(False,PhotoImage(file=os.getcwd()+"\\sticky-note-5.png"))

        # master (root) window
        self.overrideredirect(True)
        global no_of_windows

        #load the content if the file exist
        self.filename=str(no_of_windows)+".txt"
        self.TxtFile=open(os.getcwd()+"\\"+".data"+"\\"+self.filename,'a+')
        if os.path.exists(os.getcwd()+"\\"+".data"+"\\"+self.filename):
            self.TxtFile=open(os.getcwd()+"\\"+".data"+"\\"+self.filename, 'r+')
        else:
            self.TxtFile=open(os.getcwd()+"\\"+".data"+"\\"+self.TxtFile,'w+')


        #widget gemotry
        self.fixedX=250
        self.fixedY=250
        self.geometry(f'{self.fixedX}x{self.fixedY}+' + str(1150+no_of_windows*(-30)) + '+' + str(-10 + no_of_windows*20))
        self.config(bg = '#838383')
        self.attributes('-topmost', 'true')
        self.resizable(True,True)

        # titlebar
        self.titlebar = Frame(self, bg = '#F8F796', relief = 'flat', bd = 3)
        self.titlebar.bind('<Button-1>', self.get_pos)
        self.titlebar.bind('<B1-Motion>', self.move_window)
        self.titlebar.pack(fill = X, expand = 1, side = TOP)
        self.titlebar.bind("<Map>",self.frame_mapped)

        self.closebutton = Label(self.titlebar, text = 'X', bg = '#F8F7B6', relief = 'flat',font=('Comic Sans MS',10, 'italic'))
        self.closebutton.bind('<Button-1>', self.quit_window)
        self.closebutton.pack(side = RIGHT)
        self.changeOnHover(self.closebutton)

        self.resizebutton = Label(self.titlebar, text = '◯', bg = '#F8F7B6', relief = 'flat',font=('Comic Sans MS',10, 'italic'))
        self.resizebutton.bind('<Button-1>', self.minimize)
        self.resizebutton.pack(side = RIGHT,padx=5)
        self.changeOnHover(self.resizebutton)

        self.newbutton = Label(self.titlebar, text = '+', bg = '#F8F7B6', relief = 'flat',font=('Comic Sans MS',10, 'italic'),cursor="plus")
        self.newbutton.pack(side = LEFT)
        self.newbutton.bind('<Button-1>', self.another_window)
        self.changeOnHover(self.newbutton)

        self.tit = Label(self.titlebar, text = str(no_of_windows), bg = '#F8F7B6', relief = 'flat',font=('Comic Sans MS',10, 'italic'))
        self.tit.pack(side = TOP,padx=5)

        # main text area
        self.mainarea = tkst.ScrolledText(self, bg = '#FDFDCA', font=('Comic Sans MS', 10, 'italic'), relief = 'flat', padx = 5, pady = 10,undo=True)
        self.mainarea.pack(fill = BOTH, expand = 1)
        self.mainarea.insert(INSERT,self.TxtFile.read())

        # frames to introduce shadows
        self.shadow = Frame(self).pack(side=BOTTOM)
        self.shadow = Frame(self).pack(side=RIGHT)

        self.saver=Thread(target=self.autosave)
        self.saver.setDaemon(True)
        self.saver.start()
        no_of_windows += 1
    def get_pos(self, event):
        self.xclick = event.x
        self.yclick = event.y

    def move_window(self, event):
        deltx=event.x_root-self.xclick
        delty=event.y_root-self.yclick
        if deltx+250<=self.w and delty+250<=self.h and deltx>=0 and delty>=0:
            self.geometry('+{0}+{1}'.format(event.x_root-self.xclick, delty))

    def another_window(self, event):
        sticky = StickyNotes(root)

    def quit_window(self, event):
        self.closebutton.config(relief = 'flat', bd = 0)
        self.TxtFile.close()
        if os.path.getsize(os.getcwd()+"\\"+".data"+"\\"+self.filename)==0:
            os.remove(os.getcwd()+"\\"+".data"+"\\"+self.filename)
        global no_of_windows
        self.destroy()
        no_of_windows -= 1
        if(no_of_windows == 1):
            root.destroy()
    def changeOnHover(self,button):

        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            bg='#F2E3DF'))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            bg='#F8F7B6'))
    def minimize(self, event):
        self.update_idletasks()
        self.overrideredirect(False)
        #root.state('withdrawn')
        self.state('iconic')
    def autosave(self):
        while True:
            if self.TxtFile.closed==False:
                self.TxtFile.seek(0)
                self.TxtFile.write(self.mainarea.get('1.0', 'end-1c'))
                self.TxtFile.truncate()
            time.sleep(1)
    def openfile(self,v):
        if not self.mainarea.edit_modified():
            try:
                path = filedialog.askopenfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
                self.title('Notepad - ' + path)
                with open(path, 'r') as f:
                    content = f.read()
                    self.mainarea.delete('1.0', self.END)
                    self.mainarea.insert('1.0', content)
                    self.mainarea.edit_modified(0)

            except:
                pass
    def frame_mapped(self,e):
        self.update_idletasks()
        self.overrideredirect(True)
        self.state('normal')
root = Tk()
root.withdraw()
# make the first note.
sticky = StickyNotes(root)
root.mainloop()
