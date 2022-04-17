
from tkinter import *
root = Tk()
root.geometry("650x250")
root.title("Sarcasm Generator")
from random import seed
from random import randint


def button_click():
    # Grab current value in box, then combine current with new
    current = entry.get()
    current.lower()  # Make it all lowercase
    next = ""
    # Clear the text from the box
    entry.delete(0, END)
    seed(1)
    for i in range(len(current)):
        rando = randint(1, 4)
        if rando % 2 == 0:
            next += current[i].upper()
        else:
            next += current[i]

    # These need to be strings currently or else it will add them together to early
    entry.insert(0, str(next))


sarcasmLabel1 = Label(root, text="Enter a sarcastic comment:", justify="center")
sarcasmLabel1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

entry = Entry(root, width=100, borderwidth=5, justify="center")
entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

sarcasticButton1 = Button(root, text="ENGAGE SARCASM", foreground="Red", borderwidth=10, padx=30, pady=5, command=button_click, justify="center")
sarcasticButton1.grid(row=3, column=0, columnspan=3)


# Actually run the GUI Loop
# Create an event loop. Keeps GUI in an everlasting loop, so it keeps functioning until user quits.
root.mainloop()

"""
-When you install python 
-We downloaded from python.org
-Double-click the install executable, and when the first window pops up,
    be sure to check the "Add Python 3.10 to PATH"
-Then click Install
    (You may need to uninstall python, and then reinstall it which can be done from the executable downloaded from Python.org
-After you have installed, and you have your python script done: example 'sarcasm.py'
-Open CMD
-Move to the script location:
-CMD> pip3 install pyinstaller
-CMD> pyinstaller --onefile Sarcasm.py
-You may get a message that says:
-----Installing collected packages: pyinstaller
-----WARNING: The scripts pyi-archive_viewer.exe, pyi-bindepend.exe, pyi-grab_version.exe, pyi-makespec.exe, pyi-set_version.exe 
-----and pyinstaller.exe are installed in:
-----'C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' 
-----which is not on PATH.
-----Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
-On our machine, we had to copy the script that we were making executable to:
'C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts'
-Then move CMD to that same location
-CMD> cd 'C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts'
-Then make that target py script an executable
-CMD> pyinstaller --onefile Sarcasm.py
-If complete, 'sarcasm.py' will still be there but there will be a directory in that location also named 'dist'
-Move into 'dist'
"""