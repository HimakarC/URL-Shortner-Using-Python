from tkinter import *
import pyshorteners
import webbrowser
import os

root = Tk()
root.title("URL Shortner using Python")
root.geometry("4000x3000")
url_label = Label(root, text="URL Shortner", font="Helvtica 25 bold", height=2).pack()
entry1 = Entry(root, width=70, border=2, borderwidth=2, relief=FLAT)
entry1.pack()
def bc():
    url = entry1.get()
    if url == '':
        Label(root, text="Link should not be blank").pack()
    else:
        win_url = pyshorteners.Shortener().tinyurl.short(url)
        lab = Label(root, text="Your Short URL", height=2)
        lab.pack()
        entry = Entry(root, width=70, border=2, borderwidth=2)
        entry.insert(0, win_url)
        entry.pack()
        Button(root, text="Open ShortLink in Browser", command=ob, padx=10, pady=10).pack()
        return None
def cw():
    root.destroy()
def ob():
    url = entry1.get()
    webbrowser.open(pyshorteners.Shortener().tinyurl.short(url))
def cal():
    root.destroy()
    os.popen("python gui-url-shortner.py")
Button(root, text=" Click to get Shortened URL ", command=bc, padx=10, pady=10).pack(side=LEFT)
Button(root, text="Quit", command=cw, padx=10, pady=10).pack(side=RIGHT)
Button(root, text="Clear All", command=cal, padx=10, pady=10).pack(side=LEFT)
author = Label(root, text=" GUI Application By Himakar C")
author.place(relx=0.0, rely=1.0, anchor='sw')
root.mainloop()
