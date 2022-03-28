from pyautogui import *
import pyautogui
import time
import keyboard
import random
import winsound
import win32api, win32con
import cv2
import pytesseract
import datetime as dt
import sys
import ctypes  # An included library with Python install.


def specialCase(number):
    lis = []
    vowel = ["", "่", "้", "๊", "๋", "์", "็"]
    word_with_vowel_1 = ["ศูนย", "หนึ", "สี", "ห", "เจ", "เก"]
    word_with_vowel_2 = ["", "ง", "", "า", "ด", "า"]

    special_number = ["ศูนย์", "หนึ่ง", "สี่", "ห้า", "เจ็ด", "เก้า"]

    if number in special_number:
        if number == "ศูนย์":
            for position in vowel:
                lis.append(word_with_vowel_1[0] + position + word_with_vowel_2[0])
            return lis


        elif number == "หนึ่ง":
            for position in vowel:
                lis.append(word_with_vowel_1[1] + position + word_with_vowel_2[1])
            return lis


        elif number == "สี่":
            for position in vowel:
                lis.append(word_with_vowel_1[2] + position + word_with_vowel_2[2])
            return lis

        elif number == "ห้า":
            for position in vowel:
                lis.append(word_with_vowel_1[3] + position + word_with_vowel_2[3])
            return lis


        elif number == "เจ็ด":
            for position in vowel:
                lis.append(word_with_vowel_1[4] + position + word_with_vowel_2[4])
            return lis


        elif number == "เก้า":
            for position in vowel:
                lis.append(word_with_vowel_1[5] + position + word_with_vowel_2[5])
            return lis


    else:
        lis.append(number)
        return lis

def click(x, y):
    win32api.SetCursorPos((x, y))  # this is in tuple
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # pressdown the mouse
    time.sleep(0.1)  # pause script for 0.01 second, otherwise some unexpected event may occur.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # release the mouse


def screenshot(x, y, width, height, name):
    version = 1
    if version ==1:
        iml = pyautogui.screenshot(region=(x, y, width, height))
        path = "C:\\Users\\supaw\\Google Drive\\Computer science Portfolio\\Asura Online cheat\\AsuraOnlineAutoDesktopEdition\\"
        name = name + ".png"
        fullname = path + name
        # iml = pyautogui.screenshot(region = (1075,825,150,136))#same size as sample

        iml.save(r"{}".format(fullname))
    elif version ==2:

        iml = pyautogui.screenshot(region=(313, 211, 183, 120))
        # iml = pyautogui.screenshot(region = (1075,825,150,136))#same size as sample
        iml.save(
            r"C:\\Users\\supaw\\Google Drive\\Computer science Portfolio\\Asura Online cheat\\AsuraOnlineAutoDesktopEdition\\diescreen.png")



def sound():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def getTheTextFromImageBottom(location):
    option = 1
    trial = 0

    while True:
        try:
            if trial >=10:
                print("Could not translate the bottom layer")

                time.sleep(1)
                print("Exceed trial")
                return "[สาม]"

            if option ==1:
                trial+=1
                option =2
                print("Im in option1")
                pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

                img = cv2.imread("bottom_word_number.png")  # pytesseract only take in RGB but the orginal cv2 image is BGR
                #
                # thresh = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                #
                # result = pytesseract.image_to_string(thresh, lang="tha")
                # print(result)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
                thresh = cv2.GaussianBlur(thresh, (3, 3), 0)


                result = pytesseract.image_to_string(thresh, lang='tha',config="bottom_line_words.txt")
                print(result)
                number_word = result.split(" ")[1]
                number = word_to_number_dict[number_word]

                return number_word
            elif option ==2:
                trial += 1
                option =1
                print("Im in option2")
                pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

                img = cv2.imread("bottom_word_number.png")  # pytesseract only take in RGB but the orginal cv2 image is BGR

                thresh = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                result = pytesseract.image_to_string(thresh, lang="tha")
                print(result)
                number_word = result.split(" ")[1]
                number = word_to_number_dict[number_word]
                return number_word
        except:
            print("Wrong text use another option")


def setupTheDict():

    position_two = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    position_one = ["หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    fullList = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    dict = {}
    counter = 0
    for number in fullList:
        value = specialCase(number)
        for i in value:
            dict[f"[{i}]"] = counter
        counter += 1
    for one in position_one:
        for two in position_two:
            position1 = specialCase(one)
            position2 = specialCase(two)
            for i in position1:
                for j in position2:
                    dict[f"[{i}{j}]"] = counter
            counter += 1

    return dict


def getTheNumberFromImageRight(name):
    option = 1
    trial = 1
    while True:
        try:
            if trial >=10:

                break
            if option ==1:
                trial +=1
                print("Option1")
                option =2
                #performing a bit of preprocessing
                pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
                # Load image, grayscale, Otsu's threshold(two pixel return, foreground and backgroun, making the image really clear to computer.)
                img = cv2.imread(name + ".png")  # pytesseract only take in RGB but the orginal cv2 image is BGR
                #GaussiaBlur is use to remove noise,edges.
                #Gaussian smoothing is also used as a pre-processing stage in computer vision algorithms in order to enhance image structures at different scales
                #by reducing noise, there is less variation of pixel and the computer then can easier pick the character.
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
                thresh = cv2.GaussianBlur(thresh, (3, 3), 0)
                data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
                print(data)
                return int(data.split("\n")[0])
                break
            elif option ==2:
                option =3
                print("Option2")
                trial +=1
                #performing a bit of preprocessing

                pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
                # Load image, grayscale, Otsu's threshold(two pixel return, foreground and backgroun, making the image really clear to computer.)
                img = cv2.imread(name + ".png")  # pytesseract only take in RGB but the orginal cv2 image is BGR



                thresh = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
                print(data)
                return int(data.split("\n")[0])
                break
            elif option ==3:
                option =1
                print("Option3")
                trial +=1
                #performing a bit of preprocessing

                pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
                # Load image, grayscale, Otsu's threshold(two pixel return, foreground and backgroun, making the image really clear to computer.)
                img = cv2.imread(name + ".png")  # pytesseract only take in RGB but the orginal cv2 image is BGR



                thresh = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789')
                print(data)
                return int(data.split("\n")[0])

        except:
            print("Invalid answer")
    return



def processWholeSequence(expand_x,expand_y,process_sleep,screen_number):
    shaman_location_screen = []


    process_sleep =2

    print("Found the pic")
    # the image being detected

    # click on the warning big screen
    print("Click on warning button")
    click(801, 693)
    click(801, 693)
    time.sleep(0.5)
    print("Click to expand the question")
    click(998,684)
    time.sleep(2)
    # screen shot the screen at the bottom
    print("Screenshot bottom layer")
    screenshot(305, 742, 459, 57, "bottom_word_number")

    # screen shot the three number on the right

    print("Screenshot 3 number")
    screenshot(884, 366, 49, 49, "position1")
    screenshot(884, 428, 49, 49, "position2")
    screenshot(884, 490, 49, 49, "position3")

    # use the image recognition to convert the bottom to the text and use dict to find the value.
    print("convert image to text")
    result = word_to_number_dict[getTheTextFromImageBottom(screen_number)]

    # use the image recognition to convert the right 3 number to the text.
    print("convert image to number")
    val1 = getTheNumberFromImageRight("position1")
    val2 = getTheNumberFromImageRight("position2")
    val3 = getTheNumberFromImageRight("position3")
    if result == val1:
        click(913, 392)
        click(913, 392)


    elif result == val2:
        click(913, 457)
        click(913, 457)


    elif result == val3:
        click(913, 514)
        click(913, 514)

    else:
        click(913, 556)
        click(913, 556)





    time.sleep(process_sleep)





    time.sleep(1)

def writeTimeAndDate(note,screen_location):
    time = dt.datetime.now()
    f = open("record.txt","a")
    f.write(f"{note} : Screen Location {screen_location} ,Time: {time} \n")
    f.close()

process_sleep = 0.5
word_to_number_dict = setupTheDict()
# This version of the image recognition use the sound instead of automation
# to tell the user that the warning has been pop and it require user attention
# by making the sound.
counter = 0
try:
    while keyboard.is_pressed("q") !=True:

        app_location = [(89, 838), (156, 838), (214, 838), (274, 838), (336, 838), (405, 838), (473, 838), (521, 838),
                        (583, 838), (645, 838)
            , (779, 838), (829, 838), (892, 838), (965, 838), (1027, 838), (1078, 838), (1146, 838), (1200, 838),
                        (1263, 838), (1335, 838)
            , (89, 885), (156, 885), (214, 885), (274, 885), (336, 885), (405, 885), (473, 885), (521, 885), (583, 885),
                        (645, 885)
            , (779, 885), (829, 885), (892, 885), (965, 885), (1027, 885), (1078, 885), (1146, 885), (1200, 885),
                        (1263, 885), (1335, 885)]



        #     1. Find all the nine position
        #     2.get the size and confidence
        #     3.check if the image is the same.
        # 4.use the key f to do the action and we can use the mouse to exit the prison.
        try:
            for x,y in app_location:
                click(x,y)


                if counter==40:
                    print("I am at counter40")
                    time.sleep(1)
                    click(1399,889)
                    time.sleep(1)
                    click(1399,889)
                if counter ==80:
                    print("I am at counter80")
                    time.sleep(1)
                    counter=0
                    click(1399,829)
                    time.sleep(1)
                    click(1399, 829)
                if counter==40 or counter == 80:
                    print("You have 10 second to exit the program by pressing Ctrl+C in the running program  ")
                    time.sleep(10)
                for _ in range(5):
                    time.sleep(0.2)
                    if pyautogui.locateOnScreen("savedimage.png", region=(900, 717, 120, 105), confidence=0.50) != None:

                        processWholeSequence(505,19,2,1)
                        # writeTimeAndDate("Prison",1)
                        print("found the image")
                counter+=1

        except KeyboardInterrupt:
            print("Ctrl + C is pressed")
            sys.exit("Key pressed")
        except:
            print("wrong try again")

except KeyboardInterrupt:
    print("Interupt")

#
# app_location = [(89,838),(156,838),(214,838),(274,838),(336,838),(405,838),(473,838),(521,838),(583,838),(645,838)
#                 ,(779,838),(829,838),(892,838),(965,838),(1027,838),(1078,838),(1146,838),(1200,838),(1263,838),(1335,838)
#                 ,(89,885),(156,885),(214,885),(274,885),(336,885),(405,885),(473,885),(521,885),(583,885),(645,885)
#                 ,(779,885),(829,885),(892,885),(965,885),(1027,885),(1078,885),(1146,885),(1200,885),(1263,885),(1335,885)]
