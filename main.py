from tkinter import *

def press(num):

    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():

    global equation_text
    try:

        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")
        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")
        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
window.title("Mandip's Calculator program")
window.geometry("500x650")
window.configure(bg="lightblue")


equation_text = ""

equation_label = StringVar()



label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=70,
                 command=lambda: press(1))
button1.grid(row=0, column=0)
button1.configure(bg="cyan", fg="black")


button2 = Button(frame, text=2, height=4, width=9, font=70,
                 command=lambda: press(2))
button2.configure(bg="cyan", fg="black")

button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: press(3))
button3.configure(bg="cyan", fg="black")

button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: press(4))
button4.grid(row=1, column=0)
button4.configure(bg="cyan", fg="black")


button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: press(5))
button5.grid(row=1, column=1)
button5.configure(bg="cyan", fg="black")


button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: press(6))
button6.grid(row=1, column=2)
button6.configure(bg="cyan", fg="black")


button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: press(7))
button7.grid(row=2, column=0)
button7.configure(bg="cyan", fg="black")


button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: press(8))
button8.grid(row=2, column=1)
button8.configure(bg="cyan", fg="black")


button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: press(9))
button9.grid(row=2, column=2)
button9.configure(bg="cyan", fg="black")


button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: press(0))
button0.grid(row=3, column=0)
button0.configure(bg="cyan", fg="black")


plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: press('+'))
plus.grid(row=0, column=3)
plus.configure(bg="green", fg="black")

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: press('-'))
minus.grid(row=1, column=3)
minus.configure(bg="yellow", fg="black")

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: press('*'))
multiply.grid(row=2, column=3)
multiply.configure(bg="red", fg="black")

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: press('/'))
divide.grid(row=3, column=3)
divide.configure(bg="green", fg="black")

equal = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3, column=2)
equal.configure(bg="grey", fg="black")

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: press('.'))
decimal.grid(row=3, column=1)
decimal.configure(bg="purple", fg="black")

clear = Button(window, text='clear', height=4, width=12, font=35,
                 command=clear)
clear.configure(bg="pink", fg="black")
clear.pack()

window.mainloop()