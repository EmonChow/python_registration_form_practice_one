from tkinter import *

root = Tk()
root.geometry("800x700")
def onSubmit():
    print("Submitted")


Label(root, text="Registration form", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
Phone = Label(root, text="Phone")
Address = Label(root, text="Address")
Email = Label(root, text="Email")
Gender = Label(root, text="Gender")
Payment = Label(root, text="Payment Mode")

name.grid(row=1, column=2)
Phone.grid(row=2, column=2)
Address.grid(row=3, column=2)
Email.grid(row=4, column=2)
Gender.grid(row=5, column=2)
Payment.grid(row=6, column=2)

nameValue = StringVar
phoneValue = StringVar
addressValue = StringVar
emailValue = StringVar
genderValue = StringVar
paymentValue = StringVar


ChekValue = IntVar

nameentry = Entry(root, textvariable=nameValue)
phoneentry = Entry(root, textvariable=phoneValue)
addressentry = Entry(root, textvariable =addressValue)
emailentry = Entry(root, textvariable=emailValue)
genderentry = Entry(root, textvariable=genderValue)
paymententry = Entry(root, textvariable=paymentValue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
addressentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
genderentry.grid(row=5, column=3)
paymententry.grid(row=6, column=3)

checkbtn = Checkbutton(text="remember me?" , variable=ChekValue)
checkbtn.grid(row=7, column=3)

Button(text="Submit", command=onSubmit).grid(row=8, column=3)


root.mainloop()