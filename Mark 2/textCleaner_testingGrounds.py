# Text Cleaning
characters = {
    "a" : [ [1, 0, 0] , [0, 0, 0] ],
    "b" : [ [1, 1, 0] , [0, 0, 0] ],
    "c" : [ [1, 0, 0] , [1, 0, 0] ],
    "d" : [ [1, 0, 0] , [1, 1, 0] ],
    "e" : [ [1, 0, 0] , [0, 1, 0] ],
    "f" : [ [1, 1, 0] , [1, 0, 0] ],
    "g" : [ [1, 1, 0] , [1, 1, 0] ],
    "h" : [ [1, 1, 0] , [0, 1, 0] ],
    "i" : [ [0, 1, 0] , [1, 0, 0] ],
    "j" : [ [0, 1, 0] , [1, 1, 0] ],
    "k" : [ [1, 0, 1] , [0, 0, 0] ],
    "l" : [ [1, 1, 1] , [0, 0, 0] ],
    "m" : [ [1, 0, 1] , [1, 0, 0] ],
    "n" : [ [1, 0, 1] , [1, 1, 0] ],
    "o" : [ [1, 0, 1] , [0, 1, 0] ],
    "p" : [ [1, 1, 1] , [1, 0, 0] ],
    "q" : [ [1, 1, 1] , [1, 1, 0] ],
    "r" : [ [1, 1, 1] , [0, 1, 0] ],
    "s" : [ [0, 1, 1] , [1, 0, 0] ],
    "t" : [ [0, 1, 1] , [1, 1, 0] ],
    "u" : [ [1, 0, 1] , [0, 0, 1] ],
    "v" : [ [1, 1, 1] , [0, 0, 1] ],
    "w" : [ [0, 1, 0] , [1, 1, 1] ],
    "x" : [ [1, 0, 1] , [1, 0, 1] ],
    "y" : [ [1, 0, 1] , [1, 1, 1] ],
    "z" : [ [1, 0, 1] , [0, 1, 1] ],
    " " : [ [0, 0, 0] , [0, 0, 0] ], # Space
    "(caps)" : [ [0, 0, 0] , [0, 0, 1] ],
    "(letter)" : [ [0, 0, 0] , [0, 1, 1] ],
    "(number)" : [ [0, 0, 1] , [1, 1, 1] ],
    "," : [ [0, 1, 0] , [0, 0, 0] ],
    ";" : [ [0, 1, 1] , [0, 0, 0] ],
    ":" : [ [0, 1, 0] , [0, 1, 0] ],
    "." : [ [0, 1, 0] , [0, 1, 1] ],
    "(decimal)":[ [0, 0, 0] , [1, 0, 1] ],
    "!" : [ [0, 1, 1] , [0, 1, 0] ],
    "|" : [ [0, 0, 1] , [1, 1, 0] ],
    "*" : [ [0, 0, 1] , [0, 1, 0], [0, 0, 1] , [0, 1, 0] ],
    "&" : [ [1, 1, 1] , [1, 0, 1] ],
    "'" : [ [0, 0, 1] , [0, 0, 0] ],
    "‘" : [ [0, 0, 0] , [0, 0, 1] , [0, 1, 1] , [0, 0, 1] ],
    "’" : [ [0, 0, 1] , [0, 1, 1] , [0, 0, 1] , [0, 0, 0] ],
    "(" : [ [1, 1, 1] , [0, 1, 1] ],
    ")" : [ [0, 1, 1] , [1, 1, 1] ],
    "[" : [ [0, 0, 0] , [0, 0, 1] , [0, 1, 1] , [0, 1, 1] ],
    "]" : [ [0, 1, 1] , [0, 1, 1] , [0, 0, 1] , [0, 0, 0] ],
    "{" : [ [0, 0, 0] , [1, 1, 1] , [0, 1, 0] , [1, 0, 1] ],
    "}" : [ [0, 0, 0] , [1, 1, 1] , [1, 1, 0] , [1, 1, 1] ],
    "?" : [ [0, 1, 1] , [0, 0, 1] ],
    """“""" : [ [0, 1, 1] , [0, 0, 1] ],
    """"”""" : [ [0, 0, 1] , [0, 1, 1] ],
    "/" : [ [0, 0, 1] , [1, 0, 0] ],
    " \ " : [ [1, 1, 0] , [0, 1, 1] ],
    """""""" : [ [0, 1, 1] , [0, 0, 1] ],
    "-" : [ [0, 0, 1] , [0, 0, 1] ],
    "–" : [ [0, 0, 1] , [0, 0, 1] , [0, 0, 1] , [0, 0, 1] ],
    "—" : [ [0, 0, 1] , [0, 0, 1] , [0, 0, 1] , [0, 0, 1] , [0, 0, 1] , [0, 0, 1] , [0, 0, 1] , [0, 0, 1] ],
    "1" : [ [1, 0, 0] , [0, 0, 0] ],
    "2" : [ [1, 1, 0] , [0, 0, 0] ],
    "3" : [ [1, 0, 0] , [1, 0, 0] ],
    "4" : [ [1, 0, 0] , [1, 1, 0] ],
    "5" : [ [1, 0, 0] , [0, 1, 0] ],
    "6" : [ [1, 1, 0] , [1, 0, 0] ],
    "7" : [ [1, 1, 0] , [1, 1, 0] ],
    "8" : [ [1, 1, 0] , [0, 1, 0] ],
    "9" : [ [0, 1, 0] , [1, 0, 0] ],
    "0" : [ [0, 1, 0] , [1, 1, 0] ],
    " " : [ [0, 0, 0] , [0, 0, 0] ],
}

charactersInLine=28
maxIndents=charactersInLine*2-2
linesInPage=23

def textCleaner(inputText):
    output=[]
    isCaps=False
    isNum=False
    isWordCapped=False
    wordList=[]
    prunedText=""
    
    for char in inputText:
        if char.lower() in characters:
            prunedText=prunedText+char
    
    wordList=prunedText.split()
    wordListIndex=0
    
    for i,char in enumerate(inputText):
        if char==" ":
            output.append(char)
            if i==0:
                wordListIndex=0
            elif inputText[i-1]!=" ":
                wordListIndex+=1
                if wordList[wordListIndex].isupper() and len(wordList[wordListIndex])>1:
                    isWordCapped=True
                    output.append("(caps)")
                    output.append("(caps)")
                    isCaps=True
        elif char.lower() in characters: 
            if isCaps==False:
                isCaps=char.isupper()
                if isCaps:
                    output.append("(caps)")
            elif isCaps==True:
                if isWordCapped:
                    isCaps=True
                else:
                    isCaps=char.isupper()
            if isNum==False:
                isNum=char.isnumeric()
                if isNum:
                    output.append("(number)")
            elif isNum==True:
                isNum=char.isnumeric() or char=="," or char=="." 
                if isNum==False:    
                    if char.islower():
                        output.append("(letter)")
                        
            if char=="." and isNum:
                output.append("(decimal)")
            else:
                output.append(char.lower())
    return output

def lineSplitter(charList):
    out=[[" "," "]]
    linecount=0
    indentCount=4
    for i, char in enumerate(charList):
        indentNum=len(characters[char])
        if indentCount==0 and char==" ":  #first character is space, ignore it
            continue
        elif indentCount+indentNum<=maxIndents:
            out[linecount].append(char)
            indentCount+=indentNum
        else: #will exceed 2nd last char
            if i==len(charList)-1: #last character, add it
                if indentCount+indentNum==maxIndents+2:
                    out[linecount].append(char)
                    return out
                else:
                    out[linecount].append("-")
                    linecount+=1
                    indentCount=0
                    out.append([])
                    out[linecount].append(char)
                    return out
            elif charList[i+1]==" ": #last character of word on last indent
                out[linecount].append(char)
                indentCount=0
                linecount+=1
                out.append([])
            elif (char.isalnum() or indentNum>2) and char!="-" and out[linecount][-1]!=" ": #middle char that will exceed, create next line, add to next line
                out[linecount].append("-")
                linecount+=1
                out.append([])
                indentCount=0
                indentCount+=indentNum
                out[linecount].append(char)
            elif out[linecount][-1]==" ": #first character of a word, no need hyphen
                linecount+=1
                out.append([])
                indentCount=0
                indentCount+=indentNum
                out[linecount].append(char)
            else: #is a natrual hyphen at the end
                out[linecount].append(char)
                linecount+=1
                out.append([])
                indentCount=0
    return out
        
def createParagraph(inputText):
    charList = textCleaner(inputText)
    return lineSplitter(charList)

def createSpacerLine(): #DEPRECIATED
    out=[]
    for i in range(charactersInLine):
        out.append(" ")
    return out

def createPages(inputText):
    out=[[]]
    pageCount=0
    length=0
    paragraphList=inputText.split("\n\n")
    # print(paragraphList)
    
    for i,paragraph in enumerate(paragraphList):
        paragraphList[i]=createParagraph(paragraph)
        
    rawLineList=[]
    for i, paragraph in enumerate(paragraphList):
        length=len(paragraphList)
        for line in paragraph:
            rawLineList.append(line)
        # if i!=length-1:
        #     rawLineList.append(createSpacerLine())
    
    for line in rawLineList:
        if len(out[pageCount])<linesInPage:
            out[pageCount].append(line)
        else:
            if line is not createSpacerLine():
                pageCount+=1
                out.append([])
                out[pageCount].append(line)
    return out

inputText="""I am Iron Man.

The suit and I are one. You want my property? Well you can't have it!"""

pages=createPages(inputText)
for i, page in enumerate(pages):
    # print(page)
    print("PAGE " + str(i+1))
    for line in page:
        # for char in line:
        #     print(char)
        print(line)
        # print(len(line))
# print(pages)


# printing_list = []
# for paragraph in pages:
#     para_lines = []
#     printing_list.append("start of paragraph")
#     for line in paragraph:
#         line_chars = []
#         # line_chars.append("alpaca")
#         for char in line:
#             line_chars.append(characters[char])
#         line_chars.append("end of line")
#         # print(line_chars)
#         para_lines.append(line_chars)
#     printing_list.append(para_lines)
#     printing_list.append("end of paragraph")

# print(printing_list)



# import easygui
# file = easygui.fileopenbox()
# print(file)