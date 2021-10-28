import pyttsx3
import PyPDF2


book = open('ms-17.pdf','rb')#in the bracket u have to attach the pdf for which u want to listen
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(1,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
