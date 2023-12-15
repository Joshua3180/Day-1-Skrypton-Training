from tkinter import *
from tkinter import messagebox

KI = Tk()
KI.title("Keyboard Inputs")
KI.geometry("600x400")


def submitted():
    KI = KInputentry.get()

    if KI=="":
        messagebox.showerror("Input Error", "Please Give Input From Keyboard")
    else:
        confirm = messagebox.askyesno("Confirmation", "Are you sure to submit your data?")
        if confirm == True:
            KInputentry.delete(0, 'end')
            KI.destroy()

KInput = Label(KI, text="Key Board Inputs")
KInput.place(x=20, y=20)

KInputentry = Entry(KI)
KInputentry.place(x=140, y=20)

submit = Button(KI, text="Submit", command=submitted)
submit.place(x=125, y=60)

KI.mainloop()