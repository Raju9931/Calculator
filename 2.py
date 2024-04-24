import tkinter as tk
from time import strftime
root = tk.Tk()
root.title("Digital Clock")
# root.geometry('500*800')

def time():
    string = strftime('%H:%M:%S %p\n %D')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font=('calibri',50, 'bold' ),background='skyblue',foreground='black' )
label.pack(anchor='center')

time()

root.mainloop()