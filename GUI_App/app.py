
# Need to install these python libraries to use here
import tkinter as tk
# Adjusting PDF files
# python3 -m pip install --upgrade PyPDF3
import PyPDF2
# Work with images
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow
from PIL import Image, ImageTk
# To let us browse/open a file after button click.
from tkinter.filedialog import askopenfile


# RUN> python app.py
# Main Loop Command All code must be between.... (Start...))
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)  # Split canvas into 3 invisible columns/rows

# Only need the name currently, because the logo is in the same directory.
logo = Image.open('battlescribeLogo.jpg')
# Convert image into a tkinter image
logo = ImageTk.PhotoImage(logo)
# Place image inside a tkinter label widget
logo_label = tk.Label(image=logo)
logo_label.image = logo
# Place logo inside window
logo_label.grid(column=1, row=0)

# Instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all of it's text.", font="Raleway")
# Make sure text goes across all 3 columns
instructions.grid(columnspan=3, column=0, row=1)


# Function for the button
# Using the askopenfile to browse/open a file after button click
def open_file():
    browse_text.set("loading.....")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        # If file was found/accepted
        # Read the pdf in, just view the first page, get text from first page. Print text to terminal
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        # Text box to hold the text collected from the first page of the pdf
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        # Make the text pretty and justified to the center of the text box.
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)
        # Set button back to normal text
        browse_text.set("Browse")


# Browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="dark blue", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

# This is nearly the same as the top. Remove the rowspan
# This just creates a button spacer. The button is still in the original location
# This adds another full, separate, blank section below it.
# If you just made the original space bigger, the button and others would just spread out.
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)  # Split canvas into 3 invisible columns/rows


root.mainloop()
# Main Loop Command All code must be between.... (...End))
