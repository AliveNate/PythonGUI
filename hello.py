# Use everything from tkinter (GUI)
from tkinter import *
root = Tk()


# Create a label widget. Define the labels
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="Ben will be here later.")
myLabel3 = Label(root, text="                      ")


# Now put the label into the root window. This will just default to the top left.
#myLabel1.pack()
# Or put labels in the specified grid space
# Remember this is all relative, if you have nothing in column 2,3,4 then column 5 will just look like column 2
myLabel1.grid(row=0, column=0)
myLabel3.grid(row=1, column=1)
myLabel2.grid(row=2, column=2)


# Input Box
e = Entry(root, width=50)
#e.pack  # Pack into screen if not using grid
e.grid(row=9, column=1)
# Put a caption in the entrybox
e.insert(0, "Enter Your Name: ")
# Grab input from the e. "e.get()" Putting this in the button function


# Function to be called when button is clicked
# Var will increase by 1 each time the button is clicked.
count = 0
def myClick():
    # Want value to go up each time we click. State we are using the global var in the function.
    global count
    count = count + 1
    # Call count var and place in text. Also place text from input box in the text.
    myLabel4 = Label(root, text=("Look I clicked a button {} times!\nInput = " + e.get()).format(count))

    myLabel4.grid(row=8, column=1)


myButton1 = Button(root, text="Click Me")
myButton2 = Button(root, text="Disabled Button", state=DISABLED)  # Button shows, but cannot be clicked.
# Text on button is blue, the button itself is red.
myButton3 = Button(root, text="Sized Button", padx=30, pady=20, foreground="blue", background="red")
# Button will call the function above.
# Normally a function will have () after it, but not when you use the 'command' as seen here.
myButton4 = Button(root, text="Call a function", command=myClick)
# Place buttons in GUI location
myButton1.grid(row=4, column=2)
myButton2.grid(row=5, column=2)
myButton3.grid(row=6, column=2)
myButton4.grid(row=7, column=1)



# Actually run the GUI Loop
# Create an event loop. Keeps GUI in an everlasting loop, so it keeps functioning until user quits.
root.mainloop()

