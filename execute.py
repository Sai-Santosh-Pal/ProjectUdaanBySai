import pip
pip.main(['install', 'tkinter'])
pip.main(['install', 'PyPdf2'])
pip.main(['install', 'pathlib'])
pip.main(['install', 'Pillow'])
pip.main(['install', 'pytesseract'])
pip.main(['install', 'zipfile'])
pip.main(['install', 'fitz'])
pip.main(['uninstall', 'googletrans'])
pip.main(['install', 'googletrans==4.0.0rc1', '--user'])

import os
os.chdir("./v0.2/")
os.system("python main.py")
