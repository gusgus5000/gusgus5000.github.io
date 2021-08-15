from tkinter import  messagebox, simpledialog, Tk

root = Tk()


g = float(simpledialog.askstring("Number 1", "give my a number"))
h = float(simpledialog.askstring("Number 2", "give my a second number"))
j = simpledialog.askstring("Sign", "-or+")

if j == "-":
    messagebox._show("Test", g-h)
    #messagebox.showinfo(g-h)
elif j == "+":
    messagebox.showinfo(g+h)
else:
    for counter in range(1, 11):
        messagebox.showinfo("wrong")


