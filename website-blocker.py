# GUI Website blocker for Windows systems.

from tkinter import *

root = Tk()
root.title("Website Blocker")
root.geometry('500x250')
root.resizable(0,0)
root.eval('tk::PlaceWindow . center')


Label(root, text="Website Blocker", font='roboto 18 bold underline').pack()

hosts = 'C:\Windows\System32\drivers\etc\hosts'
ip = '127.0.0.1'

Label(root, text="\nEnter the websites to be blocked: ", font='roboto 12').pack()
websites = Text(root, font='arial 10', height='2', width = '40', wrap = WORD, padx=5, pady=5)
websites.place(x= 100,y = 80)

def block():
    weblist = websites.get(1.0, END).split(',')
    with open (hosts, 'r+') as h:
        text = h.read()
        for x in weblist:
            if x in text:
                Label(root, text = "The entered website is already blocked.", font='roboto 10').place(x=170, y=130)
                pass
            else:
                h.write(ip + ' ' + x + '\n')
                Label(root, text=x + " successfully blocked.", font='roboto 10').place(x=170, y=130)
                websites.delete(1.0, END)

BlockButton = Button(root, text = "Block", font = 'roboto 14 bold', bg = 'red', activebackground = '#990000', padx=1, pady=5, command = block, width = 6).place(x=200, y=190)

root.mainloop()