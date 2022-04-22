import easygui
import os
import textract
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from braille_slicer_mk2 import convert_braille_text_to_gcode
from time import sleep

def startup_message():
    print("Welcome to the Project Mimir printing interface!\n")

def option_menu():
    print("""Option Menu for printing:
        1. Import a document 
        2. Type a custom message
        3. Use speech to text
    """)
    command = input("Please type a command number from the option menu given above and press Enter:\n")
    return command

def open_txt():
    file = easygui.fileopenbox()
    if file == None:
        print("File import cancelled, closing Mimir slicer...")
        sleep(5)
        quit()
    text = textract.process(file)
    # print(text)
    return str(text)[1:]

def speech_to_text():
    valid_yes = ['1', 1, 'yes', 'y', 'YES', 'Y', 'Yes', '']
    valid_nos = ['0', 0, 'no', 'n', 'NO', 'N', 'No']
    r = sr.Recognizer()
    recordtime = int(input("Please input how long you would like to speak for (in seconds):\n"))
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Recording...")
        audio_data = r.record(source, duration=recordtime)
        print("Recognizing...")
        # if audio_data == None:
        #     command = input("Error! No audio recorded. Rerecord?")
        #     if command in valid_yes:
        #         audio_data = r.record(source, duration=recordtime)
        #     else:
        #         quit()
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)
        return text

def extract_string_from_command(command_input):
    if command_input == "1":
        return open_txt()
    elif command_input == "2":
        manual_input_text = input("Type the custom message that you wish to print:\n")
        return manual_input_text
    elif command_input == "3":
        return speech_to_text()
    elif command_input == "cancel":
        quit()
    else:
        print("Invalid input, please try again.")
        return 1 

def text_playback(printing_material):
    valid_yes = ['1', 1, 'yes', 'y', 'YES', 'Y', 'Yes', '']
    valid_nos = ['0', 0, 'no', 'n', 'NO', 'N', 'No']
    command = input("Would you like to display the printing text for screen reader verification? Type yes or no:\n")
    if command in valid_yes:
        print(printing_material)
    elif command.lower() == "cancel":
        quit()
    else:
        print("Skipping...")

def audio_playback(printing_material):
    valid_yes = ['1', 1, 'yes', 'y', 'YES', 'Y', 'Yes', '']
    valid_nos = ['0', 0, 'no', 'n', 'NO', 'N', 'No']
    command = input("Would you like to play back the audio for the printing text? Type yes or no:\n")
    if command in valid_yes:
        speech = gTTS(printing_material)
        audio_filename = "playback.mp3"
        speech.save(audio_filename)
        playsound(audio_filename)
    elif command in valid_nos:
        print("Audio play back skipped.")
    elif command.lower() == "cancel":
        quit()
    else:
        print("Invalid input.")

def savefile():
    file_name_path = easygui.filesavebox("Where would you like to save the print output?") #d3
    return file_name_path

def clear():
    if os.name == 'nt':
        _ = os.system('cls')


if __name__ == "__main__":
    startup_message()
    
    while True:
        command_input = option_menu()
        printing_material = extract_string_from_command(command_input)

        if printing_material == 1:
            printing_material = extract_string_from_command(option_menu())
        else:
            text_playback(printing_material)
            print("""Please select a printing option:
            1. Save the output file locally or to external storage
            2. Send print directly to printer (requires USB connection)
            """)
            command = input("Please type a command number from the option menu given above and press Enter:\n")
            if command == "1":
                print("Where would you like to save the print output? (This will open the file saving dialogue where you can name your output file)")
                file_name_path = savefile()
            elif command == "2":
                print("Sorry! This feature is currently a work in progress. The slicer will save the output print file instead.")
                sleep(3)
                print("Where would you like to save the print output? (This will open the file saving dialogue where you can name your output file)")
                file_name_path = savefile()
            convert_braille_text_to_gcode(file_name_path, printing_material)
            print("Done! Returning to option menu...")
            sleep(1)
            print("3...")
            sleep(1)
            print("2...")
            sleep(1)
            print("1...")
            sleep(1.5)
            clear()


