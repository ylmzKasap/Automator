import time
import os
import re

import pyautogui


def incorrect_color(point):
    while True:
        try:
            while not pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                print(f"\nColor values do not match for {point[0]}.")
                print(f"Expected value: {point[2]}")
                print(f"Current value: {pyautogui.pixel(point[1][0], point[1][1])}")
                time.sleep(4)
                os.system("cls")
            break
        except OSError:
            time.sleep(0.2)
            continue


def file_not_found(wait, picture):
    waitTime = wait
    os.system("cls")
    print(f"\n{os.path.basename(picture)}, is not in 'Pictures' folder.")
    for i in range(waitTime):
        print(f"\nNew attempt in {waitTime} seconds.")
        waitTime -= 1
        time.sleep(1)


def image_not_found(wait):
    waitTime = wait
    os.system("cls")
    print("\nImage is not found on screen")
    for i in range(waitTime):
        print(f"\nNew attempt in {waitTime} seconds.")
        waitTime -= 1
        time.sleep(1)


# --- For specific projects, delete or change when needed --- Required to create a variable dictionary
imageDestination = f"{os.getcwd()}\\Files\\Image Files"
soundDestination = f"{os.getcwd()}\\Files\\Sound Files"

directoryError = 0
variableDict = {}
variableSymbol = "v"

try:
    imageDestinationContents = os.listdir(imageDestination)
    soundDestinationContents = os.listdir(soundDestination)
    words = []
    getTillDot = re.compile(r"[^.]+")

    for i in imageDestinationContents:
        words.append(getTillDot.search(i).group())

    index = 1
    words.sort(key=str.lower)
    imageDestinationContents.sort(key=str.lower)
    soundDestinationContents.sort(key=str.lower)

    for i in range(len(imageDestinationContents)):
        variableDict[variableSymbol + str(index)] = words[i]
        index += 1
        variableDict[variableSymbol + str(index)] = imageDestinationContents[i]
        index += 1
        variableDict[variableSymbol + str(index)] = soundDestinationContents[i]
        index += 1

    variableDict[variableSymbol + str(len(list(variableDict.keys())) + 1)] = imageDestination
    variableDict[variableSymbol + str(len(list(variableDict.keys())) + 1)] = soundDestination

except FileNotFoundError:
    directoryError = 1

# --- For specific projects, delete or change when needed ---


def process_variable(variableDictionary):
    if directoryError == 1:
        print("\nCouldn't find the directory to collect variables. This method will not be usable.")
        print(f"\nDirectories searched:\n{imageDestination}\n{soundDestination}")
        input()
        return
    allowedRange = len(list(variableDictionary.keys()))
    numberError, numberErrorMessage = 0, "\nEnter a number."
    rangeError, rangeErrorMessage = 0, f"\nThe number must be between 1 and {allowedRange}."
    if allowedRange == 0:
        print("\nThere are no variables in the variable dictionary.")
        time.sleep(2)
        return
    while True:
        variable = 0
        try:
            os.system("cls")
            if numberError == 1:
                print(numberErrorMessage)
                numberError = 0
            if rangeError == 1:
                print(rangeErrorMessage)
                rangeError = 0
            print("\nEnter a variable number.")
            print("Current variables:\n")
            for index, v in enumerate(variableDictionary.values()):
                print(f"{index+1}. {v}")
            variable = input()
            variable = int(variable)
        except ValueError:
            numberError = 1
            continue
        if variable < 1 or variable > allowedRange:
            rangeError = 1
            continue
        break
    variableTranslation = variableSymbol + str(variable)
    return variableTranslation


def run_commands(actions, aTime):
    for index, point in enumerate(actions):
        if '-normal_click' in point[0]:
            pyautogui.click(point[1], duration=aTime)
        elif '-click_color' in point[0]:
            while True:
                time.sleep(0.2)
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.click(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)

        elif '-move_cursor' in point[0]:
            pyautogui.moveTo(point[1], duration=aTime)
        elif '-moveCursor_color' in point[0]:
            time.sleep(0.2)
            while True:
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.moveTo(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)

        elif '-double_click' in point[0]:
            pyautogui.doubleClick(point[1], duration=aTime)
        elif '-doubleClick_color' in point[0]:
            while True:
                time.sleep(0.2)
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.doubleClick(point[1], duration=aTime)
                    break
                else:

                    incorrect_color(point)
        elif '-right_click' in point[0]:
            pyautogui.rightClick(point[1], duration=aTime)
        elif '-rightClick_color' in point[0]:
            while True:
                time.sleep(0.2)
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.rightClick(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)

        elif '-middle_click' in point[0]:
            pyautogui.middleClick(point[1], duration=aTime)
        elif '-middleClick_color' in point[0]:
            while True:
                time.sleep(0.2)
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.middleClick(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)

        elif '-drag_to' in point[0]:
            time.sleep(0.2)
            pyautogui.dragTo(point[1], duration=aTime)
        elif '-dragTo_color' in point[0]:
            time.sleep(0.2)
            while True:
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.dragTo(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)

        elif 'scrollUp' in point[0]:
            time.sleep(0.5)
            for i in range(3):
                pyautogui.scroll(500)
        elif 'scrollDown' in point[0]:
            time.sleep(0.5)
            for i in range(3):
                pyautogui.scroll(-500)

        elif '-clickImage' in point[0]:
            time.sleep(0.5)
            while True:
                try:
                    pyautogui.click(point[1], duration=aTime)
                    break
                except TypeError:
                    image_not_found(5)
                except FileNotFoundError:
                    file_not_found(10, point[1])

        elif '-moveCursorImage' in point[0]:
            time.sleep(0.5)
            while True:
                try:
                    pyautogui.moveTo(point[1], duration=aTime)
                    break
                except TypeError:
                    image_not_found(5)
                except FileNotFoundError:
                    file_not_found(10, point[1])

        elif '-doubleClickImage' in point[0]:
            time.sleep(0.5)
            while True:
                try:
                    pyautogui.doubleClick(point[1], duration=aTime)
                    break
                except TypeError:
                    image_not_found(5)
                except FileNotFoundError:
                    file_not_found(10, point[1])

        elif '-rightClickImage' in point[0]:
            time.sleep(0.5)
            while True:
                try:
                    pyautogui.rightClick(point[1], duration=aTime)
                    break
                except TypeError:
                    image_not_found(5)
                except FileNotFoundError:
                    file_not_found(10, point[1])

        elif '-dragToImage' in point[0]:
            time.sleep(0.5)
            while True:
                try:
                    pyautogui.dragTo(point[1], duration=aTime)
                    break
                except TypeError:
                    image_not_found(5)
                except FileNotFoundError:
                    file_not_found(10, point[1])

        elif '-wait' in point[0]:
            time.sleep(point[1])

        elif '-maximizeWindow' in point[0]:
            time.sleep(0.2)
            activeWindow = pyautogui.getActiveWindow()
            activeWindow.maximize()

        elif '-holdMouse' in point[0]:
            pyautogui.mouseDown()
            time.sleep(point[1])
            pyautogui.mouseUp()

        elif '-writeText' in point[0]:
            pyautogui.write(point[1], 0.01)

        elif '-hotkey' in point[0]:
            if point[1] == 'copy':
                pyautogui.hotkey('ctrl', 'c')
            elif point[1] == 'paste':
                pyautogui.hotkey('ctrl', 'v')
            elif point[1] == 'sAll':
                pyautogui.hotkey('ctrl', 'a')
            elif point[1] == 'cut':
                pyautogui.hotkey('ctrl', 'x')
            elif point[1] == 'undo':
                pyautogui.hotkey('ctrl', 'z')
            elif point[1] == 'redo':
                pyautogui.hotkey('ctrl', 'y')
            elif point[1] == 'save':
                pyautogui.hotkey('ctrl', 's')
            elif point[1] == 'save as':
                pyautogui.hotkey('ctrl', 'shift', 's')
            elif point[1] == 'exit':
                pyautogui.hotkey('alt', 'f4')

        elif '-pressKey' in point[0]:
            time.sleep(0.2)
            if point[1] == 'esc':
                pyautogui.press('esc')
            elif point[1] == 'del':
                pyautogui.press('delete')
            elif point[1] == 'enter':
                pyautogui.press('enter')
            elif point[1] == 'tab':
                pyautogui.press('tab')
            elif point[1] == 'up':
                pyautogui.press('up')
            elif point[1] == 'down':
                pyautogui.press('down')
            elif point[1] == 'right':
                pyautogui.press('right')
            elif point[1] == 'left':
                pyautogui.press('left')
            elif point[1] == 'home':
                pyautogui.press('home')
            elif point[1] == 'end':
                pyautogui.press('end')
            elif point[1] == 'backspace':
                pyautogui.press('backspace')

        elif '-writeVariable' in point[0]:
            pyautogui.write(variableDict[point[1]], 0.01)

        elif '-holdClick' in point[0]:
            time.sleep(0.2)
            pyautogui.keyDown(point[1])
            pyautogui.click(point[2], duration=aTime)
            pyautogui.keyUp(point[1])

        elif '-moveRelative' in point[0]:
            pyautogui.move(point[1], point[2], duration=aTime)

        elif '-repeatPrevious' in point[0]:
            if point[1] == 'infinite':
                while True:
                    run_commands([actions[index - 1]], point[2])
            else:
                for command in range(point[1]):
                    run_commands([actions[index-1]], point[2])

        else:
            print(f"\nCould not find {point[0]} in the execution file.")
            input()
