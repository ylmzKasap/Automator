import importlib
import os
from pathlib import Path
import random
import sys
import time
import webbrowser

import pyautogui
import pyperclip

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from pygame import mixer, error

if __name__ == "__main__":
    from data import varsettings, copywildcards, searchinfo
    import projectinfo
    import savedProject
else:
    from . import projectinfo
    varsettings = importlib.import_module(f"projects.{projectinfo.projectName}.data.varsettings")
    copywildcards = importlib.import_module(f"projects.{projectinfo.projectName}.data.copywildcards")
    searchinfo = importlib.import_module(f"projects.{projectinfo.projectName}.data.searchinfo")


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


def file_not_found(wait, image):
    waitTime = wait
    for i in range(waitTime):
        os.system("cls")
        print(f"\n{image} is not in 'images' folder.")
        print(f"\nNew attempt in {waitTime} seconds.")
        waitTime -= 1
        time.sleep(1)


def image_not_found(wait):
    waitTime = wait
    for i in range(waitTime):
        os.system("cls")
        print("\nImage is not found on screen.")
        print(f"\nNew attempt in {waitTime} seconds.")
        waitTime -= 1
        time.sleep(1)
    print("\nLocating the image...")


skipCommands = 0


def run_commands(actions, aTime, *args):
    if __name__ == "main":
        if searchinfo.databaseDecision == "v":
            rowsOfWildcards = varsettings.get_vars(f"{projectinfo.projectPath}\\data", "wildcard")[1]
            if searchinfo.copyState:
                variableDb = varsettings.get_vars(f".\\data", "search")[0]
            else:
                variableDb = varsettings.get_vars(f".\\data", "variable")[0]
        elif searchinfo.databaseDecision == "w":
            variableDb = varsettings.get_vars(f"{projectinfo.projectPath}\\data", "variable")[0]
            if searchinfo.copyState:
                rowsOfWildcards = varsettings.get_vars(f".\\data", "search")[1]
            else:
                rowsOfWildcards = varsettings.get_vars(f".\\data", "wildcard")[1]
    else:
        if searchinfo.databaseDecision == "v":
            rowsOfWildcards = varsettings.get_vars(f"{projectinfo.projectPath}\\data", "wildcard")[1]
            if searchinfo.copyState:
                variableDb = varsettings.get_vars(f"{projectinfo.projectPath}\\data", "search")[0]
            else:
                variableDb = varsettings.get_vars(f"{projectinfo.projectPath}\\data", "variable")[0]
        elif searchinfo.databaseDecision == "w":
            variableDb = varsettings.get_vars(f"{projectinfo.projectPath}\\data", "variable")[0]
            if searchinfo.copyState:
                rowsOfWildcards = varsettings.get_vars(f"{projectinfo.projectPath}\\data", "search")[1]
            else:
                rowsOfWildcards = varsettings.get_vars(f"{projectinfo.projectPath}\\data", "wildcard")[1]

    columnIndex = 0
    for index, point in enumerate(actions):
        try:
            if skipCommands >= 1:
                skipCommands -= 1
                continue
        except UnboundLocalError:
            pass
        colorNotFound = 0
        if point[0] == "left_click":
            pyautogui.click(point[1], duration=aTime)
        elif point[0] == "click_color":
            while True:
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.click(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == "click_color_else_pass":
            while True:
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

        elif point[0] == "move_cursor":
            pyautogui.moveTo(point[1], duration=aTime)
        elif point[0] == "move_cursor_color":
            while True:
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.moveTo(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == "move_cursor_color_else_pass":
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

        elif point[0] == "double_click":
            pyautogui.doubleClick(point[1], duration=aTime)
        elif point[0] == "double_click_color":
            while True:
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.doubleClick(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == "double_click_color_else_pass":
            while True:
                try:
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

        elif point[0] == "right_click":
            pyautogui.rightClick(point[1], duration=aTime)
        elif point[0] == "right_click_color":
            while True:
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.rightClick(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == "right_click_color_else_pass":
            while True:
                try:
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

        elif point[0] == "middle_click":
            pyautogui.middleClick(point[1], duration=aTime)
        elif point[0] == "middle_click_color":
            while True:
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.middleClick(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == "middle_click_color_else_pass":
            while True:
                try:
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

        elif point[0] == "drag_to":
            pyautogui.dragTo(point[1], duration=aTime)
        elif point[0] == "drag_to_color":
            while True:
                if pyautogui.pixelMatchesColor(point[1][0], point[1][1], point[2]):
                    pyautogui.dragTo(point[1], duration=aTime)
                    break
                else:
                    incorrect_color(point)
        elif point[0] == "drag_to_color_else_pass":
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

        elif point[0] == "scroll_up":
            time.sleep(0.2)
            for i in range(3):
                pyautogui.scroll(500)
        elif point[0] == "scroll_down":
            time.sleep(0.2)
            for i in range(3):
                pyautogui.scroll(-500)

        elif point[0] == "comment":
            continue

        elif point[0] == "image_conditional":
            while True:
                if __name__ == "__main__":
                    try:
                        if point[3] == "if":
                            if pyautogui.locateOnScreen(str(Path("images", point[1]))) is not None:
                                run_commands(point[2], aTime)
                                break
                            else:
                                break
                        elif point[3] == "if not":
                            if pyautogui.locateOnScreen(str(Path("images", point[1]))) is None:
                                run_commands(point[2], aTime)
                                break
                            else:
                                break
                        elif point[3] == "while":
                            while pyautogui.locateOnScreen(str(Path("images", point[1]))) is not None:
                                run_commands(point[2], aTime)
                            break
                        elif point[3] == "while not":
                            while pyautogui.locateOnScreen(str(Path("images", point[1]))) is None:
                                run_commands(point[2], aTime)
                            break
                    except FileNotFoundError:
                        file_not_found(10, point[1])
                else:
                    try:
                        if point[3] == "if":
                            if pyautogui.locateOnScreen(
                                    str(Path(projectinfo.projectPath, "images", point[1]))
                                    ) is not None:
                                run_commands(point[2], aTime)
                                break
                            else:
                                break
                        elif point[3] == "if not":
                            if pyautogui.locateOnScreen(
                                    str(Path(projectinfo.projectPath, "images", point[1]))
                                    ) is None:
                                run_commands(point[2], aTime)
                                break
                            else:
                                break
                        elif point[3] == "while":
                            while pyautogui.locateOnScreen(
                                    str(Path(projectinfo.projectPath, "images", point[1]))
                                    ) is not None:
                                run_commands(point[2], aTime)
                            break
                        elif point[3] == "while not":
                            while pyautogui.locateOnScreen(
                                    str(Path(projectinfo.projectPath, "images", point[1]))
                                    ) is None:
                                run_commands(point[2], aTime)
                            break
                    except FileNotFoundError:
                        file_not_found(10, point[1])
            continue

        elif point[0] == "click_image":
            while True:
                if __name__ == "__main__":
                    try:
                        pyautogui.click(str(Path("images", point[1])), duration=aTime)
                        break
                    except TypeError:
                        image_not_found(5)
                    except FileNotFoundError:
                        file_not_found(10, point[1])
                else:
                    try:
                        pyautogui.click(str(Path(projectinfo.projectPath, "images", point[1])), duration=aTime)
                        break
                    except TypeError:
                        image_not_found(5)
                    except FileNotFoundError:
                        file_not_found(10, point[1])
            continue

        elif point[0] == "click_image_else_pass":
            while True:
                if __name__ == "__main__":
                    try:
                        pyautogui.click(str(Path("images", point[1])), duration=aTime)
                        for i in range(1, point[2]):
                            pyautogui.click(duration=0)
                        break
                    except TypeError:
                        break
                    except FileNotFoundError:
                        file_not_found(10, point[1])
                else:
                    try:
                        pyautogui.click(str(Path(projectinfo.projectPath, "images", point[1])), duration=aTime)
                        for i in range(1, point[2]):
                            pyautogui.click(duration=0)
                        break
                    except TypeError:
                        break
                    except FileNotFoundError:
                        file_not_found(10, point[1])
            continue

        elif point[0] == "move_cursor_on_image":
            while True:
                if __name__ == "__main__":
                    try:
                        pyautogui.moveTo(str(Path("images", point[1])), duration=aTime)
                        break
                    except TypeError:
                        image_not_found(5)
                    except FileNotFoundError:
                        file_not_found(10, point[1])
                else:
                    try:
                        pyautogui.moveTo(str(Path(projectinfo.projectPath, "images", point[1])), duration=aTime)
                        break
                    except TypeError:
                        image_not_found(5)
                    except FileNotFoundError:
                        file_not_found(10, point[1])
            continue

        elif point[0] == "cursor_on_image_else_pass":
            while True:
                if __name__ == "__main__":
                    try:
                        pyautogui.moveTo(str(Path("images", point[1])), duration=aTime)
                    except TypeError:
                        break
                    except FileNotFoundError:
                        file_not_found(10, point[1])
                else:
                    try:
                        pyautogui.moveTo(str(Path(projectinfo.projectPath, "images", point[1])), duration=aTime)
                    except TypeError:
                        break
                    except FileNotFoundError:
                        file_not_found(10, point[1])
            continue

        elif point[0] == "double_click_image":
            while True:
                if __name__ == "__main__":
                    try:
                        pyautogui.doubleClick(str(Path("images", point[1])), duration=aTime)
                        break
                    except TypeError:
                        image_not_found(5)
                    except FileNotFoundError:
                        file_not_found(10, point[1])
                else:
                    try:
                        pyautogui.doubleClick(str(Path(projectinfo.projectPath, "images", point[1])), duration=aTime)
                        break
                    except TypeError:
                        image_not_found(5)
                    except FileNotFoundError:
                        file_not_found(10, point[1])
            continue

        elif point[0] == "double_click_image_else_pass":
            while True:
                if __name__ == "__main__":
                    try:
                        pyautogui.doubleClick(str(Path("images", point[1])), duration=aTime)
                    except TypeError:
                        break
                    except FileNotFoundError:
                        file_not_found(10, point[1])
                else:
                    try:
                        pyautogui.doubleClick(str(Path(projectinfo.projectPath, "images", point[1])), duration=aTime)
                    except TypeError:
                        break
                    except FileNotFoundError:
                        file_not_found(10, point[1])
            continue

        elif point[0] == "right_click_image":
            while True:
                if __name__ == "__main__":
                    try:
                        pyautogui.rightClick(str(Path("images", point[1])), duration=aTime)
                        break
                    except TypeError:
                        image_not_found(5)
                    except FileNotFoundError:
                        file_not_found(10, point[1])
                else:
                    try:
                        pyautogui.rightClick(str(Path(projectinfo.projectPath, "images", point[1])), duration=aTime)
                        break
                    except TypeError:
                        image_not_found(5)
                    except FileNotFoundError:
                        file_not_found(10, point[1])
            continue

        elif point[0] == "right_click_image_else_pass":
            while True:
                if __name__ == "__main__":
                    try:
                        pyautogui.rightClick(str(Path("images", point[1])), duration=aTime)
                    except TypeError:
                        break
                    except FileNotFoundError:
                        file_not_found(10, point[1])
                else:
                    try:
                        pyautogui.rightClick(str(Path(projectinfo.projectPath, "images", point[1])), duration=aTime)
                    except TypeError:
                        break
                    except FileNotFoundError:
                        file_not_found(10, point[1])
            continue

        elif point[0] == "drag_to_image":
            while True:
                if __name__ == "__main__":
                    try:
                        pyautogui.dragTo(str(Path("images", point[1])), duration=aTime)
                        break
                    except TypeError:
                        image_not_found(5)
                    except FileNotFoundError:
                        file_not_found(10, point[1])
                else:
                    try:
                        pyautogui.dragTo(str(Path(projectinfo.projectPath, "images", point[1])), duration=aTime)
                        break
                    except TypeError:
                        image_not_found(5)
                    except FileNotFoundError:
                        file_not_found(10, point[1])
            continue

        elif point[0] == "blind_click":
            pyautogui.click()
            continue

        elif point[0] == "wait":
            waitingTime = point[1]
            if int(waitingTime) == waitingTime:  # If it is not a float value
                waitingTime = int(waitingTime)
                try:
                    for i in range(waitingTime, 0, -1):
                        os.system("cls")
                        if waitingTime == 1:
                            timeExpression = "second"
                        else:
                            timeExpression = "seconds"
                        print(f"\n{waitingTime} {timeExpression} left. Waiting...")
                        time.sleep(1)
                        waitingTime -= 1
                except KeyboardInterrupt:
                    continue
            else:
                time.sleep(waitingTime)
        elif point[0] == "wait_random":
            randomWaitingTime = random.randint(point[1], point[2])
            try:
                for i in range(randomWaitingTime, 0, -1):
                    os.system("cls")
                    if randomWaitingTime == 1:
                        timeExpression = "second"
                    else:
                        timeExpression = "seconds"
                    print(f"\n{randomWaitingTime} {timeExpression} left. Waiting...")
                    time.sleep(1)
                    randomWaitingTime -= 1
            except KeyboardInterrupt:
                continue

        elif point[0] == "maximize_window":
            time.sleep(0.2)
            activeWindow = pyautogui.getActiveWindow()
            activeWindow.maximize()

        elif point[0] == "hold_mouse":
            pyautogui.mouseDown()
            time.sleep(point[1])
            pyautogui.mouseUp()

        elif point[0] == "write_text":
            pyperclip.copy(point[1])
            pyautogui.hotkey("ctrl", "v")

        elif point[0] == "hotkey":
            separatedHotkey = point[1].split()
            pyautogui.hotkey(*separatedHotkey)

        elif point[0] == "press_key":
            pyautogui.press(point[1])

        elif point[0] == "play_sound":
            abortSound = 0
            mixer.init()
            while True:
                try:
                    if __name__ == "__main__":
                        mixer.music.load(Path("sounds", point[1]))
                    else:
                        mixer.music.load(Path(projectinfo.projectPath, "sounds", point[1]))
                    break
                except error:
                    os.system("cls")
                    print(
                        f"\n'{point[1]}' is not found."
                        f"\n\nPlease make sure that '{point[1]}' is in the directory above."
                        "\nPress enter to try again, press some other key to skip this step."
                    )
                    decision = input("> ")
                    if decision == "":
                        os.system("cls")
                        continue
                    else:
                        abortSound = 1
                        break
            if abortSound == 1:
                continue
            os.system("cls")
            try:
                print("\nPlaying sound...")
                mixer.music.play()
                if point[2] == "wait":
                    while mixer.music.get_busy():
                        time.sleep(1)
            except KeyboardInterrupt:
                os.system("cls")
                mixer.music.stop()
                continue

        elif point[0] == "write_variable":
            try:
                pyperclip.copy(variableDb[point[1]])
                pyautogui.hotkey("ctrl", "v")
            except KeyError:
                keyNumber = point[1].strip('v')
                print(f"\nVariable {keyNumber} is not found."
                      "\nPlease check the number of variables you entered to the database and here."
                      "\nPress enter to continue. The program will not run."
                      )
                input("> ")
                return

        elif point[0] == "hold_click":
            time.sleep(0.2)
            pyautogui.keyDown(point[1])
            pyautogui.click(point[2], duration=aTime)
            pyautogui.keyUp(point[1])

        elif point[0] == "move_relative":
            pyautogui.move(point[1], point[2], duration=aTime)

        elif point[0] == "repeat_previous":
            try:
                if point[1] == "infinite":
                    while True:
                        run_commands([actions[index - 1]], point[2])
                else:
                    for command in range(point[1]):
                        run_commands([actions[index - 1]], point[2])
            except pyautogui.FailSafeException:
                continue

        elif point[0] == "repeat_pattern":
            try:
                if point[1] == "infinite":
                    while True:
                        run_commands(actions[(point[2]-1):index], aTime)
                else:
                    for pattern in range(point[1]):
                        run_commands(actions[(point[2]-1):index], aTime)
            except pyautogui.FailSafeException:
                continue

        elif point[0] == "repeat_commands_for_wildcards":
            uniqueVariableCount = len(rowsOfWildcards)
            wildcardRow = 0
            for i, cmd in enumerate(actions[index+1:]):
                if actions[index + i+1][0] == "end_repeat_commands_for_wildcards":
                    wildcardGap = i+1
                    break
            try:
                wildcardLoopList = actions[(index + 1):(index + wildcardGap + 1)]
            except UnboundLocalError:
                os.system("cls")
                print(
                    "\nError: Please make sure that wildcard repetition assignments"
                    + " start and end correctly."
                )
                input("> ")
                break
            for i in range(uniqueVariableCount):
                wildcardColumn = 0
                run_commands(wildcardLoopList, aTime, wildcardRow, wildcardColumn)
                wildcardRow += 1
            skipCommands = wildcardGap
            continue

        elif point[0] == "end_repeat_commands_for_wildcards":
            continue

        elif point[0] == "wildcard":
            argsList = list(args)
            try:
                wildRow = argsList[0]
                wildColumn = argsList[1]
            except IndexError:
                os.system("cls")
                print("\nIndexError: Wildcard assignments need to be wrapped by 'rfw' command.")
                input("> ")
                break
            wildColumn += columnIndex
            try:
                pyperclip.copy(str(rowsOfWildcards[wildRow][wildColumn]))
                time.sleep(0.1)
                pyautogui.hotkey("ctrl", "v")
            except IndexError:
                break
            columnIndex += 1

        elif point[0] == "go_website":
            webbrowser.open(point[1])

        elif point[0] == "launch":
            os.startfile(point[1])

        else:
            print(f"\nCould not find {point[0]} in the execution file.")
            input("> ")


if __name__ == "__main__":
    if searchinfo.databaseDecision == "w" or searchinfo.databaseDecision == "v":
        fileCondition = copywildcards.copy_wildcards(projectinfo.projectPath)
        if fileCondition[1] is False:
            print(fileCondition[0])
            input("> ")
            sys.exit()
    for command in savedProject.allCommandsSave:
        run_commands(command, projectinfo.actionTime)
