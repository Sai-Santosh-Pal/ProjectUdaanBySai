import tkinter, PyPDF2
from tkinter import filedialog , messagebox
import sys
import random
val = []
theFileName = str(sys.argv[1])
def convertToPdf(txt, lang): 
    pass
#     # from fpdf import FPDF
    
#     # pdf = FPDF()
    
#     # # Add a page
#     # pdf.add_page()
    
#     # if lang == "Hindi" or lang == "Marathi":
#     #     pdf.add_font('MANGAL', '', 'MANGAL.ttf', uni=True)
#     #     pdf.set_font('MANGAL', '', 14)
#     # if lang == "Telegu":
#     #     pdf.add_font('Gautami', '', 'Gautami.ttf', uni=True)
#     #     pdf.set_font('Gautami', '', 14)
#     # if lang == "Odia":
#     #     pdf.add_font('odiya', '', 'odiya.ttf', uni=True)
#     #     pdf.set_font('odiya', '', 14)
#     # if lang == "Punjabi":
#     #     pdf.add_font('Raavi', '', 'Raavi.ttf', uni=True)
#     #     pdf.set_font('Raavi', '', 14)
#     # if lang == "Tamil":
#     #     pdf.add_font('Latha', '', 'Latha.ttf', uni=True)
#     #     pdf.set_font('Latha', '', 14)
#     # if lang == "Kannada":
#     #     pdf.add_font('Tunga', '', 'Tunga.ttf', uni=True)
#     #     pdf.set_font('Tunga', '', 14)
#     # if lang == "Gujrati":
#     #     pdf.add_font('shruti', '', 'shruti.ttf', uni=True)
#     #     pdf.set_font('shruti', '', 14)
#     # if lang == "Bengali":
#     #     pdf.add_font('vrindab', '', 'vrindab.ttf', uni=True)
#     #     pdf.set_font('vrindab', '', 14)
#     # if lang == "Malayalam":
#     #     pdf.add_font('Kartika', '', 'Kartika.ttf', uni=True)
#     #     pdf.set_font('Kartika', '', 14)
#     # txt_list=[]
#     # last = 0
#     # x = 0
#     # for i in txt:
#     #     if x%35 == 0:
#     #         txt_list.append(txt[last:x])
#     #         last = x
#     #     else:
#     #         pass
#     #     x+=1
#     # txt_list.remove('')
#     # print(txt_list)

#     # for i in txt_list:
#     #     i = i+"\n"
#     #     print(i)
#     #     txt = i
#     # # # create a cell
#     # # # pdf.multi_cell(0, 10, txt, align="L")
#     # # pdf.output(str(random.randint(1, 1000000000000000000000000000000000000000000000))+".pdf")
#     # from pdfme import PDF

#     # pdf = PDF()
#     # pdf.add_page()
#     # pdf.text(txt)

#     # with open(f'output{random.randint(0, 100000000000000000000000)}.pdf', 'wb') as f:
#     #     pdf.output(f)
#     with open(f'file{random.randint(1, 10000000000000)}.txt', 'w', encoding="utf-8") as f:
#         f.write(str(txt))
def menuValue():
    if menu.get() == "Select Any Language":
        messagebox.showerror('Select Language', 'Please Select A Language To Continue')
    else:
        print(menu.get())
        openFile(menu.get())


def openFile(lang):
    entry_1.delete("1.0","end")
    entry_1.insert(tkinter.END, "Please Wait....")
    try:
        filename = theFileName
        print(filename)
           
        entry_1.delete("1.0", tkinter.END)
        reader = PyPDF2.PdfReader(filename)
        
        for i in range (len(reader.pages)):
            current_text = reader.pages[i].extract_text()
            
            
            # val.append(current_text + str(i + 1))
            # print(val)
            try:
                from googletrans import Translator
                translator = Translator()
                result = translator.translate(current_text, dest=lang)
                val.append(str(result)[33:][:-47] + f"\n-------Page {i + 1}-------\n")
            except Exception as e:
                messagebox.showerror("Internet Error", "Please connect to a good internet connection." + " " + str(e))
        
        entry_1.delete("1.0","end")
        for i in val:
#             print(i)
            entry_1.insert(tkinter.END, i)
            convertToPdf(str(i), lang)

    except FileNotFoundError:
        messagebox.showerror('File Error', 'Please select a valid PDF file')


window = tkinter.Tk()
window.title("Project Udaan - Machine Readable")
window.iconbitmap("icon.ico")

def module():
    menuValue()
    
    


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



