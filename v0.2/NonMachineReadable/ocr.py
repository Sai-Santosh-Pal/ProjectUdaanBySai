import tkinter
from tkinter import messagebox
import sys 
val = []
lister = []
theFileName = str(sys.argv[1])

def menuValue():
    if menu.get() == "Select Any Language":
        messagebox.showerror('Select Language', 'Please Select A Language To Continue')
    else:
        print(menu.get())
        openFile(menu.get())


def openFile(lang):
    #,"Hindi","Tamil","Telegu","Odia","Kannada", "Urdu", "Bengali", "Marathi", "Malayalam")
    entry_1.delete("1.0","end")
    entry_1.insert(tkinter.END, "Please Wait....")
    try:
        # filename = filedialog.askopenfilename(title="Open Image or PDF file", filetypes=[ ('JPG files', '*.jpg'), ('PNG files', '*.png'), ('PDF files', '*.pdf')])
        filename = theFileName
        from PIL import ImageTk, Image
        import pytesseract
        if str(str(filename)[-4] + str(filename)[-3] + str(filename)[-2] + str(filename)[-1])  == ".pdf":
            import random
            import fitz
            doc = fitz.open(filename)
            import pytesseract
            val = random.randint(1, 100000)
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            for page in doc:
                img = page.get_pixmap(matrix=fitz.Identity, dpi=None,
                                    colorspace=fitz.csRGB, clip=None, alpha=True, annots=True)
                img.save(str(val) + ".jpg")
                text = pytesseract.image_to_string(str(val) + ".jpg")
                print(text)
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(text, dest=lang)
                page_no = str(page)[5]
                result = str(translator.translate(text, dest=lang))[33:][:-47] + '\n[----------Page'+ str(int(page_no) + 1) + '----------]\n'
                lister.append(result)
            entry_1.delete("1.0","end")
            for i in lister:
                entry_1.insert(tkinter.END, i)   
        else:
            print('''other''')
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            
            img = Image.open(filename)
            try:
                text = pytesseract.image_to_string(img)
                print(text)
            except Exception as e:
                print(str(e))
                import os
                os.system("start tesseract-ocr-w64-setup-5.3.0.20221222.exe") 
                text = pytesseract.image_to_string(img)
                print(text)
            try:
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(text, dest=lang)
            except Exception as e:
                messagebox.showerror("Internet Error", "Please connect to a good internet connection.")
            entry_1.delete("1.0","end")
            entry_1.insert(tkinter.END, str(str(result)[33:])[:-47])
    except FileNotFoundError:
        messagebox.showerror('File Error', 'Please select a valid PDF file')
    
def module():
    menuValue()
    
window = tkinter.Tk()
window.title("Project Udaan - Non Machine Readable")

menu= tkinter.StringVar()
menu.set("Select Any Language")

#Create a dropdown Menu


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
drop= tkinter.OptionMenu(window, menu,"Hindi", "Punjabi","Tamil","Telegu","Odia","Kannada", "Urdu", "Gujrati", "Bengali", "Marathi", "Malayalam")


drop.place(x=90.0, y=100)
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    225.0,
    275.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    242.0,
    292.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=85.0,
    y=160.0,
    width=315.0,
    height=250.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=module,
    relief="flat"
)
button_1.place(
    x=66.0,
    y=470.0,
    width=146.0,
    height=53.0
)
window.resizable(False, False)
window.mainloop()



