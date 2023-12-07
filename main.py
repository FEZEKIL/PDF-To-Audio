import PyPDF2,pyttsx3

path = open('clcoding.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(path)

speak = pyttsx3.init()

for pages in range(pdfReader.numPages):
    text = pdfReader.getPage(pages).extractText()
    speak.say(text)
    speak.runAndWait()

speak.stop()
