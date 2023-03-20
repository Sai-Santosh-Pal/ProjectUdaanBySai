import tkinter
import PyPDF2
import os
from tkinter import filedialog
os.chdir("./")
def runOcrForMachineReadable(file):
    os.chdir("./")
    os.chdir('./MachineReadable') 
    try:
        os.system('python main.py "' + file + '"')
    except Exception:
        print("Please download Python and add it to Path!")
    os.chdir("../")
    print(os.getcwd())

def runOcrForNonMachineReadable(file):
    
    os.chdir('./NonMachineReadable') 
    try:
        os.system('python ocr.py "' + file + '"')
    except Exception:
        print("Please download Python and add it to Path!")
    os.chdir("../")
    print(os.getcwd())


def check(file):
    reader = PyPDF2.PdfReader(r"" + file)
    for i in range (len(reader.pages)):
        current_text = reader.pages[i].extract_text()
    if current_text.strip(" ") != "":
        print("Machine Readable")
        runOcrForMachineReadable(file)
    else:
        print("Not Machine Readable")
        runOcrForNonMachineReadable(file)
       
def askForFile():       
    file = filedialog.askopenfilename(title="Open Image or PDF file", filetypes=[ ('JPG files', '*.jpg'), ('PNG files', '*.png'), ('PDF files', '*.pdf')])
    if file[-1].lower() == "f":
        check(file)
    else:
        runOcrForNonMachineReadable(file)

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Project Udaan")
window.geometry("450x550")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 550,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    225.0,
    275.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=askForFile,
    relief="flat"
)
button_1.place(
    x=63.0,
    y=224.0,
    width=294.0,
    height=44.0
)
window.resizable(False, False)
window.mainloop()
