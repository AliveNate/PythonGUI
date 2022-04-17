from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_clear():
    # Clear the text from the box
    e.delete(0, END)

#e.insert(0, "Enter your name: ")
def button_click(number):
    # Grab current value in box, then combine current with new
    current = e.get()
    # Clear the text from the box
    e.delete(0, END)
    # These need to be strings currently or else it will add them together to early
    e.insert(0, str(current) + str(number))

def button_equal():
    # first num is stored in the global var seen by the button_add. Now grab the second
    second_number = e.get()
    # Clear the screen
    e.delete(0, END)
    global math
    if math == "addition":
        # Add the two ints together, and place in box. At this moment all we have is the add function
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        # Add the two ints together, and place in box. At this moment all we have is the add function
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        # Add the two ints together, and place in box. At this moment all we have is the add function
        e.insert(0, f_num * int(second_number))
    if math == "division":
        # Add the two ints together, and place in box. At this moment all we have is the add function
        e.insert(0, f_num / int(second_number))


def button_add():
    # Grab the value in the box before the + is used
    first_number = e.get()
    # Need a global var so this can be passed to the equal button function
    global math
    math = "addition"
    global f_num
    f_num = int(first_number)
    # Clear box so the second number will be displayed by itself.
    e.delete(0, END)


def button_subtract():
    # Grab the value in the box before the + is used
    first_number = e.get()
    # Need a global var so this can be passed to the equal button function
    global math
    math = "subtraction"
    global f_num
    f_num = int(first_number)
    # Clear box so the second number will be displayed by itself.
    e.delete(0, END)


def button_multiply():
    # Grab the value in the box before the + is used
    first_number = e.get()
    # Need a global var so this can be passed to the equal button function
    global math
    math = "multiplication"
    global f_num
    f_num = int(first_number)
    # Clear box so the second number will be displayed by itself.
    e.delete(0, END)


def button_divide():
    # Grab the value in the box before the + is used
    first_number = e.get()
    # Need a global var so this can be passed to the equal button function
    global math
    math = "division"
    global f_num
    f_num = int(first_number)
    # Clear box so the second number will be displayed by itself.
    e.delete(0, END)


# using the lambda so that we can pass a var to a button function
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
buttonPlus = Button(root, text="+", padx=40, pady=20, command=button_add)
buttonEquals = Button(root, text="=", padx=40, pady=20, command=button_equal)
buttonClear = Button(root, text="Clear", padx=80, pady=20, command=button_clear)
buttonSubtract = Button(root, text="-", padx=42, pady=20, command=button_subtract)
buttonMultiply = Button(root, text="*", padx=42, pady=20, command=button_multiply)
buttonDivide = Button(root, text="/", padx=42, pady=20, command=button_divide)

# Put buttons on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
buttonPlus.grid(row=4, column=1)
buttonEquals.grid(row=4, column=2)
# Spacing can be frustrating. Added columnspace, but it was just guess and check
buttonClear.grid(row=5, column=0, columnspan=2)
buttonSubtract.grid(row=6, column=0)
buttonMultiply.grid(row=6, column=1)
buttonDivide.grid(row=6, column=2)

# Actually run the GUI Loop
# Create an event loop. Keeps GUI in an everlasting loop, so it keeps functioning until user quits.
root.mainloop()