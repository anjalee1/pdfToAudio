# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
path = open('test.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 15th page.
from_page = pdfReader.getPage(15)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()