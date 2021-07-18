from tkinter import *
import hgh

root = Tk()
root.title('Ня!')
root.geometry("300x250")

def click_button():
   hgh.start()

btn = Button(text="Запустить сброс доски",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             command=click_button
             )

btn.pack()
root.mainloop()
