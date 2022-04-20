import easygui
from time import sleep
import textract

def open_txt():
    file = easygui.fileopenbox()
    if file is None:
        print("File import cancelled, closing Mimir slicer...")
        sleep(5)
        quit()
    text = textract.process(file)
    # print(text)
    return str(text)[1:]

print(open_txt())