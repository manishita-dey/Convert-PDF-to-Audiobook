# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file(Included in the project. To run include your own file or change path name)
path = open('file.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# Using getNumPages() we can count the total no of pages.
from_page = pdfReader.getPage(0)
# extracting the text from the PDF
text = from_page.extractText()
print(text)
# reading the text
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')

# Changes Speech voice
for voice in voices[1:]:
   engine.setProperty('voice', voice.id)

   # saving the audiobook created
   engine.save_to_file(text, 'audiobook_psychology.mp3')
   # Changes Speech rate
   engine.setProperty('rate', rate-20)
   engine.say(text)
engine.runAndWait()