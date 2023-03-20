import pip
pip.main(['install', 'tkinter'])
# PyPdf2 pathlib Pillow pytesseract PIL fitz googletrans
pip.main(['install', 'PyPdf2'])
pip.main(['install', 'pathlib'])
pip.main(['install', 'Pillow'])
pip.main(['install', 'pytesseract'])
pip.main(['install', 'zipfile'])
pip.main(['install', 'fitz'])
pip.main(['install', 'googletrans'])
print("Done!!!")

from zipfile import ZipFile
  
# loading the temp.zip and creating a zip object
with ZipFile(".\package.zip", 'r') as zObject:
  
    # Extracting all the members of the zip 
    # into a specific location.
    zObject.extractall(
        path=".\\")
import os
os.chdir("./v0.2/")
os.system("python main.py")
