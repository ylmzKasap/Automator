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
        colorNotFound = 0
        if point[0] == 'left_click':
            pyautogui.click(point[1], duration=aTime)
        elif point[0] == 'click_color':
            while True:
                time.sleep(0.2)
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.click(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == 'click_color_else_pass':
            while True:
                time.sleep(0.2)
                try:
                    if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                        pyautogui.click(point[1], duration=aTime)
                        break
                    else:
                        colorNotFound = 1
                        break
                except OSError:
                    continue
            if colorNotFound == 1:
                continue

        elif point[0] == 'move_cursor':
            pyautogui.moveTo(point[1], duration=aTime)
        elif point[0] == 'move_cursor_color':
            time.sleep(0.2)
            while True:
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.moveTo(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == 'move_cursor_color_else_pass':
            time.sleep(0.2)
            while True:
                try:
                    if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                        pyautogui.moveTo(point[1], duration=aTime)
                        break
                    else:
                        colorNotFound = 1
                        break
                except OSError:
                    continue
            if colorNotFound == 1:
                continue

        elif point[0] == 'double_click':
            pyautogui.doubleClick(point[1], duration=aTime)
        elif point[0] == 'double_click_color':
            while True:
                time.sleep(0.2)
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.doubleClick(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == 'double_click_color_else_pass':
            while True:
                try:
                    time.sleep(0.2)
                    if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                        pyautogui.doubleClick(point[1], duration=aTime)
                        break
                    else:
                        colorNotFound = 1
                        break
                except OSError:
                    continue
            if colorNotFound == 1:
                continue

        elif point[0] == 'right_click':
            pyautogui.rightClick(point[1], duration=aTime)
        elif point[0] == 'right_click_color':
            while True:
                time.sleep(0.2)
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.rightClick(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == 'right_click_color_else_pass':
            while True:
                try:
                    time.sleep(0.2)
                    if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                        pyautogui.rightClick(point[1], duration=aTime)
                        break
                    else:
                        colorNotFound = 1
                        break
                except OSError:
                    continue
            if colorNotFound == 1:
                continue

        elif point[0] == 'middle_click':
            pyautogui.middleClick(point[1], duration=aTime)
        elif point[0] == 'middle_click_color':
            while True:
                time.sleep(0.2)
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.middleClick(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == 'middle_click_color_else_pass':
            while True:
                try:
                    time.sleep(0.2)
                    if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                        pyautogui.middleClick(point[1], duration=aTime)
                        break
                    else:
                        colorNotFound = 1
                        break
                except OSError:
                    continue
            if colorNotFound == 1:
                continue

        elif point[0] == 'drag_to':
            time.sleep(0.2)
            pyautogui.dragTo(point[1], duration=aTime)
        elif point[0] == 'drag_to_color':
            time.sleep(0.2)
            while True:
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.dragTo(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == 'drag_to_color_else_pass':
            time.sleep(0.2)
            while True:
                try:
                    if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                        pyautogui.dragTo(point[1], duration=aTime)
                        break
                    else:
                        colorNotFound = 1
                        break
                except OSError:
                    continue
            if colorNotFound == 1:
                continue

        elif point[0] == 'scroll_up':
            time.sleep(0.5)
            for i in range(3):
                pyautogui.scroll(500)
        elif point[0] == 'scroll_down':
            time.sleep(0.5)
            for i in range(3):
                pyautogui.scroll(-500)

        elif point[0] == 'click_image':
            time.sleep(0.5)
            while True:
                try:
                    pyautogui.click(point[1], duration=aTime)
                    break
                except TypeError:
                    image_not_found(5)
                except FileNotFoundError:
                    file_not_found(10, point[1])

        elif point[0] == 'click_image_else_pass':
            time.sleep(0.5)
            try:
                pyautogui.click(point[1], duration=aTime)
                for i in range(1, point[2]):
                    pyautogui.click(duration=0)
            except TypeError:
                continue
            except FileNotFoundError:
                file_not_found(10, point[1])

        elif point[0] == 'move_cursor_on_image':
            time.sleep(0.5)
            while True:
                try:
                    pyautogui.moveTo(point[1], duration=aTime)
                    break
                except TypeError:
                    image_not_found(5)
                except FileNotFoundError:
                    file_not_found(10, point[1])

        elif point[0] == 'cursor_on_image_else_pass':
            time.sleep(0.5)
            try:
                pyautogui.moveTo(point[1], duration=aTime)
            except TypeError:
                continue
            except FileNotFoundError:
                file_not_found(10, point[1])

        elif point[0] == 'double_click_image':
            time.sleep(0.5)
            while True:
                try:
                    pyautogui.doubleClick(point[1], duration=aTime)
                    break
                except TypeError:
                    image_not_found(5)
                except FileNotFoundError:
                    file_not_found(10, point[1])

        elif point[0] == 'double_click_image_else_pass':
            time.sleep(0.5)
            try:
                pyautogui.doubleClick(point[1], duration=aTime)
            except TypeError:
                continue
            except FileNotFoundError:
                file_not_found(10, point[1])

        elif point[0] == 'right_click_image':
            time.sleep(0.5)
            while True:
                try:
                    pyautogui.rightClick(point[1], duration=aTime)
                    break
                except TypeError:
                    image_not_found(5)
                except FileNotFoundError:
                    file_not_found(10, point[1])

        elif point[0] == 'right_click_image_else_pass':
            time.sleep(0.5)
            try:
                pyautogui.rightClick(point[1], duration=aTime)
            except TypeError:
                continue
            except FileNotFoundError:
                file_not_found(10, point[1])

        elif point[0] == 'drag_to_image':
            time.sleep(0.5)
            while True:
                try:
                    pyautogui.dragTo(point[1], duration=aTime)
                    break
                except TypeError:
                    image_not_found(5)
                except FileNotFoundError:
                    file_not_found(10, point[1])

        elif point[0] == 'wait':
            time.sleep(point[1])

        elif point[0] == 'maximize_window':
            time.sleep(0.2)
            activeWindow = pyautogui.getActiveWindow()
            activeWindow.maximize()

        elif point[0] == 'hold_mouse':
            pyautogui.mouseDown()
            time.sleep(point[1])
            pyautogui.mouseUp()

        elif point[0] == 'write_text':
            pyautogui.write(point[1], 0.01)

        elif point[0] == 'hotkey':
            if point[1] == 'copy':
                pyautogui.hotkey('ctrl', 'c')
            elif point[1] == 'paste':
                pyautogui.hotkey('ctrl', 'v')
            elif point[1] == 'select all':
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

        elif point[0] == 'press_key':
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

        elif point[0] == 'write_variable':
            pyautogui.write(variableDict[point[1]], 0.01)

        elif point[0] == 'hold_click':
            time.sleep(0.2)
            pyautogui.keyDown(point[1])
            pyautogui.click(point[2], duration=aTime)
            pyautogui.keyUp(point[1])

        elif point[0] == 'move_relative':
            pyautogui.move(point[1], point[2], duration=aTime)

        elif point[0] == 'repeat_previous':
            try:
                if point[1] == 'infinite':
                    while True:
                        run_commands([actions[index - 1]], point[2])
                else:
                    for command in range(1, point[1]):
                        run_commands([actions[index-1]], point[2])
            except pyautogui.FailSafeException:
                continue

        elif point[0] == 'repeat_pattern':
            try:
                if point[1] == 'infinite':
                    while True:
                        run_commands(actions[(point[2]-1):index], aTime)
                else:
                    for pattern in range(1, point[1]):
                        run_commands(actions[(point[2]-1):index], aTime)
            except pyautogui.FailSafeException:
                continue
        else:
            print(f"\nCould not find {point[0]} in the execution file.")
            input()
