import tkinter as tk
import os
root = tk.Tk()
root.title("File manager by Galanteria")

head = tk.Label(root,text='File Manager')
head.grid(row=0,column=0,columnspan=5)
os.chdir('/home/shanu')
dir = os.listdir()
j=1
k=1
h=1
for i in dir:
    if j>4:
        j=1
        k+=1
    tk.Button(root,text='Button'+str(h)).grid(row=k,column=j)
    j+=1
    h+=1

print(dir)


root.mainloop()