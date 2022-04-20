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

# Parameters
line_length_limit = 28
pin_top = "M104" # Hotend Temp
pin_top_max = "255" # Hotend Max Temp
pin_mid = "M106" # Fan On
pin_mid_off = "M107" # Fan Off
pin_bot = "M140" # Bed Temp
pin_bot_max = "140" # Bed Max Temp
delay_time = 150 # miliseconds
move_delay_time = 150 # miliseconds
col_spacing = 2.7 # mm
char_spacing = 3.8 # mm
line_spacing = 7 # for 200 steps/mm
x_margin = 40.3
header_margin = 7
initial_feeder_scroll = 52.5
init_e, init_y, init_z = 23, 53, 43
spacing_e, spacing_y, spacing_z = 8, 24, 24

# Boilerplate code
preamble = f"""G21 ; Set units to milimeters
G90 ; Set to absolute 
G28 X ; Home axis against endstop
G0 X{x_margin} ; Set x position to margin
G91 ; Set to relative
G0 E{initial_feeder_scroll} Y{initial_feeder_scroll} Z{initial_feeder_scroll} ;
M226 PA11 
G0 E{init_e} Y{init_y} Z{init_z} ; Move Z axis to header margin
G4 P10
G0 E{spacing_e} Y{spacing_y} Z{spacing_z}
G4 P200 ; Wait to start
G0 Z{header_margin}
"""

postamble = """G90 ; Set to absolute
G28 X ; Set x position to margin
G0 Z{} ; Scroll remaining paper out
""".format(x_margin, header_margin)

afterline = f"""G90 ; Set to absolute
G28 X ; Home x-axis
G0 X{x_margin} ; Set x position to margin
G4 P500 ; Wait to set
G91 ; Set to relative
G0 Z{line_spacing} ; Scroll Z axis paper
G4 P500 ; Wait to set
"""

afterpage = f"""G0  Y{spacing_y} Z{spacing_z} ; Scroll it out
G4 P200
G0  Y{spacing_y} Z{spacing_z} ; Scroll it out
G90 ; Set to absolute 
G28 X ; Home axis against endstop
G0 X{x_margin} ; Set x position to margin
G91 ; Set to relative
G0 E{initial_feeder_scroll} Y{initial_feeder_scroll} Z{initial_feeder_scroll} ;
M226 PA11 
G0 E{init_e} Y{init_y} Z{init_z} ; Move Z axis to header margin
G4 P10
G0 E{spacing_e} Y{spacing_y} Z{spacing_z}
G4 P200 ; Wait to start
G0 Z{header_margin}
"""

# One at a time
def convert_braille_text_to_gcode(filename, input_text):
    fileName = ("{}".format(filename) + ".gcode")
    machineCode = open(fileName, "a")
    
    # Write starting boilerplate code
    machineCode = open(fileName, "a")
    machineCode.write(preamble)
    
    # Convert string to array
    # paragraphs = createParagraph(input_text)
    pages = createPages(input_text) 
    
    # Text to Braille conversion
    printing_list = []

    for paragraph in pages:
        para_lines = []
        for line in paragraph:
            line_chars = []
            for char in line:
                line_chars.append(characters[char])
            para_lines.append(line_chars)
        printing_list.append(para_lines)
    
    # print(paragraphs)

    # Braille to GCode conversion
    for braille_page in printing_list:
        for braille_line in braille_page:
            for braille_letter in braille_line:
                for count, cell_column in enumerate(braille_letter):
                    if cell_column[0]: # Top dot
                        machineCode = open(fileName, "a")
                        machineCode.write("{} S{} ; Punch top dot \n".format(pin_top, pin_top_max))
                        machineCode.write("G4 P{} ; Wait \n".format(delay_time))
                        machineCode.write("{} S0 ; Retract top dot \n".format(pin_top))
                    if cell_column[1]: # Middle dot
                        machineCode = open(fileName, "a")
                        machineCode.write("{} ; Punch mid dot \n".format(pin_mid))
                        machineCode.write("G4 P{} ; Wait \n".format(delay_time))
                        machineCode.write("{} ; Retract mid dot \n".format(pin_mid_off))
                    if cell_column[2]: # Bottom dot
                        machineCode = open(fileName, "a")
                        machineCode.write("{} S{} ; Punch bot dot \n".format(pin_bot, pin_bot_max))
                        machineCode.write("G4 P{} ; Wait \n".format(delay_time))
                        machineCode.write("{} S0 ; Retract bot dot \n".format(pin_bot))
                    
                    if count % 2 == 0:
                        machineCode = open(fileName, "a")
                        machineCode.write("G4 P{}\n".format(move_delay_time))
                        machineCode.write("G0 X{} ; Move to next col \n".format(col_spacing))
                        machineCode.write("G4 P{}\n".format(move_delay_time))
                    elif count % 2 == 1:
                        machineCode = open(fileName, "a")
                        machineCode.write("G4 P{}\n".format(move_delay_time))                    
                        machineCode.write("G0 X{} ; Move to next char \n".format(char_spacing))
                        machineCode.write("G4 P{}\n".format(move_delay_time)) 
            machineCode = open(fileName, "a")
            machineCode.write(afterline)
        machineCode = open(fileName, "a")
        machineCode.write(afterpage)

    # Write ending boilerplate code
    machineCode = open(fileName, "a")
    machineCode.write(postamble)

    pages_to_print = len(printing_list)
    print("Number of pages to print: " + pages_to_print)



# ===============
#   LEGACY CODE  
# ===============


# def size_limiter(array):
#     if len(array) > line_length_limit:
#         return array[:line_length_limit]
#     return array


# checkingtext = 'a a A a a AAA a a a a A A AA A a a A'
# print(len(checkingtext))
# convert_braille_text_to_gcode('full page test 5', checkingtext)

# All three at the same time
# def convert_braille_text_to_gcode(filename, input_text):
#     fileName = ("{}".format(filename) + ".gcode")
#     machineCode = open(fileName, "a")
    
#     # Write starting boilerplate code
#     machineCode = open(fileName, "a")
#     machineCode.write(preamble)
    
#     # Convert string to array 
#     textarray = textCleaner(input_text)
#     textline = size_limiter(textarray) # limits 30 characters per line

#     # Text to Braille conversion
#     printing_list = []
#     for char in textline:
#         printing_list.append(characters[char])
    
#     # Braille to GCode conversion
#     for braille_letter in printing_list:
#         for count, cell_column in enumerate(braille_letter):
#             if cell_column[0]: # Top dot
#                 machineCode = open(fileName, "a")
#                 machineCode.write("{} S{}\n".format(pin_top, pin_top_max))
#             if cell_column[1]: # Middle dot
#                 machineCode = open(fileName, "a")
#                 machineCode.write("{}\n".format(pin_mid))
#             if cell_column[2]: # Bottom dot
#                 machineCode = open(fileName, "a")
#                 machineCode.write("{} S{}\n".format(pin_bot, pin_bot_max))
            
#             # Dwell time
#             machineCode = open(fileName, "a")
#             machineCode.write("G4 P{}\n".format(delay_time))

#             # Retract solenoids
#             if cell_column[0]: # Top dot
#                 machineCode = open(fileName, "a")
#                 machineCode.write("{} S0\n".format(pin_top))
#             if cell_column[1]: # Middle dot
#                 machineCode = open(fileName, "a")
#                 machineCode.write("{}\n".format(pin_mid_off))
#             if cell_column[2]: # Bottom dot
#                 machineCode = open(fileName, "a")
#                 machineCode.write("{} S0\n".format(pin_bot))

#             if count % 2 == 0:
#                 machineCode = open(fileName, "a")
#                 machineCode.write("G0 X{}\n".format(col_spacing))
#                 machineCode.write("G4 P{}\n".format(delay_time))
#             elif count % 2 == 1:
#                 machineCode = open(fileName, "a")
#                 machineCode.write("G0 X{}\n".format(char_spacing))
#                 machineCode.write("G4 P{}\n".format(delay_time)) 

#     # Write ending boilerplate code
#     machineCode = open(fileName, "a")
#     machineCode.write(postamble)
