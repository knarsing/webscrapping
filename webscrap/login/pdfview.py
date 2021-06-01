from django.shortcuts import render
from PyPDF2 import PdfFileReader
import PyPDF2

# Create your views here.

def pdfview():

    pdffile = open('C:\\Users\\pimpa\\Desktop\\mbslist.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdffile)
    pages=pdfReader.numPages
    for i in range(pages):
         pageObj=pdfReader.getPage(i)
         print("Page No:",i)
         text=pageObj.extractText().split(" ")
         #text=text.replace('.','')
         #text=text.replace('\x0c','')
         for i in range(len(text)):
             print(text[i].encode(encoding='UTF-16BE'),end="\n\n")
         print()
    pdffile.close()


if __name__ == '__main__':
    pdfview()    
