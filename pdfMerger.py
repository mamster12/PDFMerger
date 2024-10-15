import PyPDF2
from sys import argv
import os

output = argv[1]

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
      
        merger.append(file)

merger.write(output)