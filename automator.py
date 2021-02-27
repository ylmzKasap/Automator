import time
import os
import sys
import copy
import re
import pprint
from pathlib import Path

import pyautogui

import keyinfo
from runit import variableDict, run_commands, process_variable


ACTION_DURATION = 0.65  # Action time for each command

currentProjects = [
    folder for folder in os.listdir(f"{os.getcwd()}\\Projects")
    if os.path.isdir(f"{os.getcwd()}\\Projects\\{folder}")]

allCommands = []  # List of commands for all episodes, to be saved later
allEpisodeNames = []  # List of names for all episodes, to be saved later
commands = []  # List of commands for CURRENT episode
turn = 1  # command number for the current episode
error = 0  # Switches to "1" if there is an error. Prevents os.system("cls").
recursionError = 0  # Switches to "1" if there is more than 1 subsequent repeat previous command assignments.

commandsRegex = re.compile(r"-.*")
episodesRegex = re.compile(r"[^\d]+")

originalScreenSize = (pyautogui.size().width, pyautogui.size().height)


def correct_project_name(project_name):
    forbiddenCharacters = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]  # To create a folder
    nameError = 0
    try:
        while True:
            if project_name == "" or project_name.isspace():
                project_name = pyautogui.prompt("Please provide a name for the project.")
                continue
            for character in forbiddenCharacters:
                if character in project_name:
                    project_name = pyautogui.prompt(
                        f"Project name cannot include '{i}'. Enter a new name."
                        )
                    nameError = 1
                    break
            if nameError == 1:
                nameError = 0
                continue
            break
    except AttributeError:
        print("\nThe program is terminated as no valid project name has been provided.")
        input()
        sys.exit()


def key_to_action(keyToPress, change, insertion):
    global turn
    currentPosition = pyautogui.position()

    if insertion == 1:
        commands.insert(turn-1, [])
        commands[turn-1] = ([f"{turn}{keyinfo.keyToText[keyToPress]}"])
        commands[turn-1].append(
            list((currentPosition.x, currentPosition.y)))
        while True:
            try:
                commands[turn-1].append(
                    pyautogui.pixel(currentPosition.x, currentPosition.y))
                break
            except OSError:
                time.sleep(0.2)
                continue
        for index, i in enumerate(commands):
            commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
        turn = len(commands) + 1
        insertion = 0
        return change, insertion

    if change == 0:
        commands.append([])
    commands[turn-1] = ([f"{turn}{keyinfo.keyToText[keyToPress]}"])
    commands[turn-1].append(list((currentPosition.x, currentPosition.y)))
    while True:
        try:
            commands[turn-1].append(
                pyautogui.pixel(currentPosition.x, currentPosition.y))
            break
        except OSError:
            time.sleep(0.2)
            continue

    if change == 1:
        change = 0
        turn = len(commands) + 1
        return change, insertion
    turn += 1
    return change, insertion


def key_to_image_action(key, imageName, change, insertion):
    global turn

    if insertion == 1:
        commands.insert(turn-1, [])
        commands[turn-1] = ([f"{turn}{keyinfo.keyToTextImage[key]}"])
        commands[turn-1].append(f"{os.getcwd()}\\Pictures\\{imageName}")
        for index, i in enumerate(commands):
            commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
        turn = len(commands) + 1
        insertion = 0
        return change, insertion

    if change == 0:
        commands.append([])
    commands[turn-1] = ([f"{turn}{keyinfo.keyToTextImage[key]}"])
    commands[turn-1].append(f"{os.getcwd()}\\Pictures\\{imageName}")

    if change == 1:
        change = 0
        turn = len(commands) + 1
        return change, insertion
    turn += 1
    return change, insertion


def check_recursion(commandsList):
    for i in range(len(commandsList)):
        try:
            if '-repeatPrevious' in commandsList[i][0] and '-repeatPrevious' in commandsList[i+1][0]:
                return True
        except IndexError:
            return False


if len(currentProjects) == 0:
    projectName = pyautogui.prompt(
        "Enter a name to start a new project."
        )
    correct_project_name(projectName)
else:
    projectName = pyautogui.prompt(
        "Choose a project:"
        "\n\nCurrent projects:\n"
        + "\n".join(currentProjects)
        + "\n\nYou can create a new project by entering a different name."
        )
    correct_project_name(projectName)

try:
    projectPath = Path.cwd() / "Projects" / projectName
except TypeError:
    print("\nThe program is terminated as no valid project name has been provided.")
    input()
    sys.exit()

projectPathAlternative = f"{os.getcwd()}\\Projects\\{projectName}"

if not projectPath.exists():
    os.makedirs(projectPath)

saveName = "savedProject.py"

if (projectPath / saveName).exists():
    sys.path.insert(1, projectPathAlternative)
    import savedProject
    allCommands = savedProject.allCommandsSave
    allEpisodeNames = savedProject.allEpisodeNamesSave
    commands = copy.deepcopy(allCommands[-1])
    episode = len(allCommands)
else:
    episode = len(allCommands) + 1

changeInPlace = 0
insertionInPlace = 0
firstTime = 0

while True:
    if error == 0:
        os.system("cls")
    error = 0

    if firstTime == 0:
        print(f"\nProject: {projectName}")
        firstTime = 1

    try:
        print(f"\n{allEpisodeNames[episode-1]}\n")
    except IndexError:
        print(f"\n{episode}. Unnamed Episode")
    if len(commands) > 0:
        pprint.pprint(commands)

    if check_recursion(commands):
        recursionError = 1
    else:
        recursionError = 0
    if recursionError == 1:
        print(
            "\nWARNING! There are more than one subsequent repeat assignments."
            + "\nExecuting these commands will cause a recursion error."
        )

    command = input()

    if command == "zzz":
        while True:
            print("\nEnter a value for the cursor to go on x coordinate.")
            x = input()
            print("\nEnter a value for the cursor to go on y coordinate.")
            y = input()
            try:
                pyautogui.moveTo(x=int(x), y=int(y), duration=1)
            except ValueError:
                os.system("cls")
                print("\nPlease enter a number.\n")
                continue
            os.system("cls")
            print(f"\nEpisode {episode}\n")
            if len(commands) > 0:
                pprint.pprint(commands)
            command = input()
            if command != "zzz":
                break
    if command == "z":
        try:
            pyautogui.moveTo(commands[-1][1], duration=1)
        except:
            continue
        continue
    if command == "zz":
        try:
            pyautogui.moveTo(commands[-2][1], duration=1)
        except:
            continue
        continue

    if command == "help":
        os.system("cls")
        print()
        for k, v in keyinfo.helpMenu.items():
            print(f"{k}: {v}")
            error = 1
        print("\nCommand: A single automation instruction.")
        print(
            "\nEpisode: A series of commands which constitute a meaningful part of the automation process."
        )
        continue

    if command == "epi":
        os.system("cls")
        if len(allEpisodeNames) > 0:
            print("\nAll episodes:")
            print()
            for i in allEpisodeNames:
                print(i)
        else:
            print("\nThere are no saved episodes.")
        print()
        error = 1
        continue

    abortReplace = 0

    if command == "rep":
        if len(commands) == 0:
            print("\nThere is no command to replace.")
            time.sleep(2)
            continue
        notFound = 0
        while True:
            os.system("cls")
            if notFound == 1:
                print("\nThere is no such command.")
                notFound = 0
            print("\nAll commands:")
            pprint.pprint(commands)
            print("\nEnter a command number to replace. 'q' cancels the process.")
            allCommandsForReplacement = []
            for i in range(1, len(commands)+1):
                allCommandsForReplacement.append(str(i))
            replacedCommand = input()
            if replacedCommand == "q":
                abortReplace = 1
                break
            if replacedCommand not in allCommandsForReplacement:
                notFound = 1
                continue
            replacedCommand = int(replacedCommand)
            turn = replacedCommand
            changeInPlace = 1
            break

    if abortReplace == 1:
        continue

    if changeInPlace == 1:
        os.system("cls")
        # noinspection PyUnboundLocalVariable
        print(f"\nEnter the command which will replace {commands[replacedCommand-1]}")
        command = input()
        while command not in keyinfo.allAssignments:
            os.system("cls")
            print("\nAll commands:")
            for k, v in keyinfo.allAssignmentsExplained.items():
                print(f"{k}: {v}")
            print(f"\nThere is no command called '{command}'. Please check the keys above.")
            command = input()

    abortInsertion = 0

    if command == "ins":
        if len(commands) == 0:
            print("\nThere is no command to insert after.")
            time.sleep(2)
            continue
        notFound = 0
        while True:
            os.system("cls")
            if notFound == 1:
                print("\nThere is no such command.")
                notFound = 0
            print("\nAll commands:")
            pprint.pprint(commands)
            print("\nEnter a command number to insert after. 'q' cancels the process.")
            allCommandsForInsertion = []
            for i in range(0, len(commands)+1):
                allCommandsForInsertion.append(str(i))
            insertionCommand = input()
            if insertionCommand == "q":
                abortInsertion = 1
                break
            if insertionCommand not in allCommandsForInsertion:
                notFound = 1
                continue
            insertionCommand = int(insertionCommand)
            turn = insertionCommand+1
            insertionInPlace = 1
            break

    if abortInsertion == 1:
        continue

    if insertionInPlace == 1:
        os.system("cls")
        # noinspection PyUnboundLocalVariable
        if insertionCommand == 0:
            print(f"\nEnter the command which will precede {commands[insertionCommand]}.")
            command = input()
            while command not in keyinfo.allAssignments:
                os.system("cls")
                print("\nAll commands:")
                for k, v in keyinfo.allAssignmentsExplained.items():
                    print(f"{k}: {v}")
                print(f"\nThere is no command called '{command}'. Please check the keys above.")
                command = input()
        else:
            print(f"\nEnter the command which will be executed after {commands[insertionCommand-1]}.")
            command = input()
            while command not in keyinfo.allAssignments:
                os.system("cls")
                print("\nAll commands:")
                for k, v in keyinfo.allAssignmentsExplained.items():
                    print(f"{k}: {v}")
                print(f"\nThere is no command called '{command}'. Please check the keys above.")
                command = input()

    if command == "name":
        print("\nEnter a new episode name.")
        episodeName = input()
        try:
            allEpisodeNames[episode-1] = f"{str(episode)}. {episodeName}"
        except IndexError:
            allEpisodeNames.append(f"{str(episode)}. {episodeName}")
        continue

    if command == "run":
        print("\nThe episode will run in 3 seconds.")
        time.sleep(3)
        try:
            run_commands(commands, ACTION_DURATION)
        except pyautogui.FailSafeException:
            pass
        continue

    if command == "runep":
        if len(allCommands) == 0:
            os.system("cls")
            print("\nThere is no episode to run.")
            error = 1
            continue
        os.system("cls")
        print("\nAll episodes:")
        print()
        previousEpisodes = []
        for i in allEpisodeNames:
            print(i)
        print(f"\nRun all commands from which episode? There are {episode-1} episodes behind.\n")
        print("'q' cancels the process.")
        for i in range(1, episode):
            previousEpisodes.append(str(i))
        runEpisode = input()
        if runEpisode == "q":
            continue
        while runEpisode not in previousEpisodes:
            os.system("cls")
            print("\nAll episodes:")
            print()
            for i in allEpisodeNames:
                print(i)
            print(f"\nThere is no such episode. There are {episode-1} episodes behind.")
            print("Run all commands from which episode?")
            runEpisode = input()
        runEpisode = int(runEpisode)
        print(f"\nAll commands from episode {runEpisode} to current episode will run in 3 seconds.")
        time.sleep(3)
        try:
            for permittedCommands in allCommands[runEpisode-1:episode]:
                run_commands(permittedCommands, ACTION_DURATION)
            try:
                if commands != allCommands[episode-1]:
                    run_commands(commands, ACTION_DURATION)
            except IndexError:
                pass
        except pyautogui.FailSafeException:
            pass
        continue

    if command == "save":
        saveFile = open(projectPath / "savedProject.py", "w", encoding="utf8")
        saveFile.write("\nscreenSize = " + pprint.pformat(originalScreenSize) + "\n")
        try:
            allCommands[episode-1] = copy.deepcopy(commands)
        except IndexError:
            allCommands.append(copy.deepcopy(commands))
        saveFile.write("\nallCommandsSave = " + pprint.pformat(allCommands))
        commands = []
        turn = 1
        try:
            episodeName = allEpisodeNames[episode-1]
        except IndexError:
            episodeName = f"{episode}. Unnamed Episode"
        try:
            allEpisodeNames[episode-1] = episodeName
        except IndexError:
            allEpisodeNames.append(episodeName)
        saveFile.write("\n\nallEpisodeNamesSave = " + pprint.pformat(allEpisodeNames))
        episode = len(allCommands)+1
        saveFile.close()
        continue

    if command == "go":
        if len(allEpisodeNames) > len(allCommands):
            del allEpisodeNames[-1]
        if len(allCommands) == 0:
            os.system("cls")
            print("\nThere are no episodes to go.")
            error = 1
            continue
        os.system("cls")
        print("\nAll episodes:")
        print()
        for i in allEpisodeNames:
            print(i)
        print(f"\n\nChoose an episode to go. There are {len(allCommands)} episodes in total.\n")
        print("Unsaved progress within current episode will be lost. 'q' cancels the process.")
        currentEpisodes = []
        for i in range(1, len(allCommands)+1):
            currentEpisodes.append(str(i))
        goEpisode = input()
        if goEpisode == "q":
            continue
        while goEpisode not in currentEpisodes:
            os.system("cls")
            print("\nAll episodes:")
            print()
            for i in allEpisodeNames:
                print(i)
            print(f"\nThere is no such episode. There are {len(allCommands)} episodes in total.")
            print("Choose an episode to go.")
            goEpisode = input()
        episode = int(goEpisode)
        commands = copy.deepcopy(allCommands[episode-1])
        turn = len(commands)+1
        continue

    if command == "copy":
        os.system("cls")
        print("\nAll episodes:")
        print()
        for i in allEpisodeNames:
            print(i)
        print(
            f"\n\nCopy which episode's content to current one? "
            + f"There are {len(allCommands)} episodes in total.\n"
            )
        copyEpisode = input()
        if copyEpisode == "q":
            continue
        currentEpisodes = []
        for i in range(1, len(allCommands)+1):
            currentEpisodes.append(str(i))
        while copyEpisode not in currentEpisodes:
            os.system("cls")
            print("\nAll episodes:")
            print()
            for i in allEpisodeNames:
                print(i)
            print(f"\nThere is no such episode. There are {len(allCommands)} episodes in total.")
            print("Which episode would you like to copy to the current one?")
            copyEpisode = input()
        copyEpisode = int(copyEpisode)
        commands = copy.deepcopy(allCommands[copyEpisode-1])
        turn = len(commands)+1
        continue

    if command == "del":
        if len(allEpisodeNames) > len(allCommands):  # Delete extra episode name if the episode is not saved
            del allEpisodeNames[-1]
        if len(allCommands) == 0:
            os.system("cls")
            print("\nThere is no episode to delete.")
            error = 1
            continue
        os.system("cls")
        print("\nAll episodes:")
        print()
        for i in allEpisodeNames:
            print(i)
        print(f"\n\nDelete which episode? There are {len(allCommands)} episodes in total.\n")
        print("Unsaved progress within current episode will be lost. 'q' cancels the process.")
        currentEpisodes = []
        for i in range(1, len(allCommands)+1):
            currentEpisodes.append(str(i))
        delEpisode = input()
        if delEpisode == "q":
            continue
        while delEpisode not in currentEpisodes:
            os.system("cls")
            print("\nAll episodes:")
            print()
            for i in allEpisodeNames:
                print(i)
            print(f"\nThere is no such episode. There are {len(allCommands)} episodes in total.")
            print("Delete which episode?")
            delEpisode = input()
        delEpisode = int(delEpisode)
        del allCommands[delEpisode-1]
        del allEpisodeNames[delEpisode-1]
        for index, i in enumerate(allEpisodeNames):
            allEpisodeNames[index] = f"{index+1}{episodesRegex.search(i).group()}"
        try:
            commands = copy.deepcopy(allCommands[len(allCommands)-1])
            episode = len(allCommands)
        except IndexError:
            commands = []
            episode = 1
        turn = len(commands)+1
        continue

    if command == "insep":
        if len(allCommands) == 0:
            print("\nThere is no episode to insert after.")
            time.sleep(2)
            continue
        notFound = 0
        while True:
            os.system("cls")
            if notFound == 1:
                print("\nThere is no such episode.")
                notFound = 0
            print("\nAll episodes:")
            for i in allEpisodeNames:
                print(i)
            print(
                    "\nAdd a new episode after which one? "
                    + "\nUnsaved progress within current episode will be lost. 'q' cancels the process."
                  )
            allEpisodesForInsertion = []
            for i in range(0, len(allCommands)+1):
                allEpisodesForInsertion.append(str(i))
            insertionCommand = input()
            if insertionCommand == "q":
                abortInsertion = 1
                break
            if insertionCommand not in allEpisodesForInsertion:
                notFound = 1
                continue
            insertionCommand = int(insertionCommand)
            allCommands.insert(insertionCommand, [])
            allEpisodeNames.insert(insertionCommand, [])
            allEpisodeNames[insertionCommand] = "9999. Unnamed Episode"
            for index, i in enumerate(allEpisodeNames):
                allEpisodeNames[index] = f"{index+1}{episodesRegex.search(i).group()}"
            commands = []
            episode = insertionCommand+1
            turn = len(commands)+1
            break
        continue

    if abortInsertion == 1:
        continue

    if command == "v":
        os.system("cls")
        variableToBeWritten = process_variable(variableDict)
        if variableToBeWritten is None:
            if changeInPlace == 1:
                turn = len(commands) + 1
                changeInPlace = 0
            if insertionInPlace == 1:
                turn = len(commands) + 1
                insertionInPlaceInPlace = 0
            continue
        if insertionInPlace == 1:
            commands.insert(turn-1, [])
            commands[turn-1] = ([f"{turn}-writeVariable"])
            commands[turn-1].append(variableToBeWritten)
            for index, i in enumerate(commands):
                commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
            turn = len(commands) + 1
            insertionInPlace = 0
            continue
        if changeInPlace == 0:
            commands.append([])
        commands[turn-1] = ([f"{turn}-writeVariable"])
        commands[turn-1].append(variableToBeWritten)
        if changeInPlace == 1:
            turn = len(commands) + 1
            changeInPlace = 0
            continue
        turn += 1
        continue

    elif command == "k":
        os.system("cls")
        print("\nEnter a text input.")
        writeIt = input()
        if insertionInPlace == 1:
            commands.insert(turn-1, [])
            commands[turn-1] = ([f"{turn}-writeText"])
            commands[turn-1].append(writeIt)
            for index, i in enumerate(commands):
                commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
            turn = len(commands) + 1
            insertionInPlace = 0
            continue
        if changeInPlace == 0:
            commands.append([])
        commands[turn-1] = ([f"{turn}-writeText"])
        commands[turn-1].append(writeIt)
        if changeInPlace == 1:
            turn = len(commands) + 1
            changeInPlace = 0
            continue
        turn += 1
        continue

    elif command == "hot":
        os.system("cls")
        print("\nChoose a hotkey.")
        print("\nAvailable hotkeys:")
        for hotkey in list(keyinfo.hotkeys.keys()):
            print(f"{hotkey}: {keyinfo.hotkeys[hotkey][1]}")
        hotkeyDecision = input()
        while hotkeyDecision not in list(keyinfo.hotkeys.keys()):
            os.system("cls")
            print(f"\nThere is no hotkey labeled as {hotkeyDecision}.")
            print("\nAvailable hotkeys:")
            for hotkey in list(keyinfo.hotkeys.keys()):
                print(f"{hotkey}: {keyinfo.hotkeys[hotkey][1]}")
            hotkeyDecision = input()
        if insertionInPlace == 1:
            commands.insert(turn-1, [])
            commands[turn-1] = ([f"{turn}-hotkey"])
            commands[turn-1].append(hotkeyDecision)
            for index, i in enumerate(commands):
                commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
            turn = len(commands) + 1
            insertionInPlace = 0
            continue
        if changeInPlace == 0:
            commands.append([])
        commands[turn-1] = ([f"{turn}-hotkey"])
        commands[turn-1].append(hotkeyDecision)
        if changeInPlace == 1:
            turn = len(commands) + 1
            changeInPlace = 0
            continue
        turn += 1
        continue

    elif command == "hc":
        holdKeys = ["ctrl", "shift", "alt"]
        currentPos = pyautogui.position()
        print("\nPress which key before clicking here?")
        print("\nAvailable keys:")
        for i in holdKeys:
            print(i)
        holdKey = input()
        while holdKey not in holdKeys:
            os.system("cls")
            print("\nThere is no such key.")
            print("\nAvailable keys:\n")
            for i in holdKeys:
                print(i)
            holdKey = input()
        if insertionInPlace == 1:
            commands.insert(turn-1, [])
            commands[turn-1] = ([f"{turn}-holdClick"])
            commands[turn-1].append(holdKey)
            commands[turn-1].append(list((currentPos.x, currentPos.y)))
            for index, i in enumerate(commands):
                commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
            turn = len(commands) + 1
            insertionInPlace = 0
            continue
        if changeInPlace == 0:
            commands.append([])
        commands[turn-1] = ([f"{turn}-holdClick"])
        commands[turn-1].append(holdKey)
        commands[turn-1].append(list((currentPos.x, currentPos.y)))
        if changeInPlace == 1:
            turn = len(commands) + 1
            changeInPlace = 0
            continue
        turn += 1
        continue

    elif command == "p":
        os.system("cls")
        print("\nPress which key?")
        print("\nAvailable keys:")
        for key in list(keyinfo.keyboard.keys()):
            print(f"{key}: {keyinfo.keyboard[key][1]}")
        keyDecision = input()
        while keyDecision not in list(keyinfo.keyboard.keys()):
            os.system("cls")
            print(f"\nThere is no such key labeled as {keyDecision}.")
            print("\nAvailable keys:")
            for key in list(keyinfo.keyboard.keys()):
                print(f"{key}: {keyinfo.keyboard[key][1]}")
            keyDecision = input()
        if insertionInPlace == 1:
            commands.insert(turn-1, [])
            commands[turn-1] = ([f"{turn}-pressKey"])
            commands[turn-1].append(keyDecision)
            for index, i in enumerate(commands):
                commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
            turn = len(commands) + 1
            insertionInPlace = 0
            continue
        if changeInPlace == 0:
            commands.append([])
        commands[turn-1] = ([f"{turn}-pressKey"])
        commands[turn-1].append(keyDecision)
        if changeInPlace == 1:
            turn = len(commands) + 1
            changeInPlace = 0
            continue
        turn += 1
        continue

    elif command == "maxW":
        print("Current window will be maximized in 3 seconds.")
        time.sleep(3)
        activeWindow = pyautogui.getActiveWindow()
        activeWindow.maximize()
        continue
    elif command == "max":
        if insertionInPlace == 1:
            commands.insert(turn-1, [])
            commands[turn-1] = ([f"{turn}-maximizeWindow"])
            for index, i in enumerate(commands):
                commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
            turn = len(commands) + 1
            insertionInPlace = 0
            continue
        if changeInPlace == 0:
            commands.append([])
        commands[turn-1] = ([f"{turn}-maximizeWindow"])
        if changeInPlace == 1:
            turn = len(commands) + 1
            changeInPlace = 0
            continue
        turn += 1
        continue

    elif command == "h":
        os.system("cls")
        print("\nHold left click for how many seconds?")
        holdTime = input()
        while True:
            try:
                holdTime = int(holdTime)
                break
            except ValueError:
                os.system("cls")
                print("\nEnter a number.")
                holdTime = input()
        if insertionInPlace == 1:
            commands.insert(turn-1, [])
            commands[turn-1] = ([f"{turn}-holdMouse"])
            commands[turn-1].append(holdTime)
            for index, i in enumerate(commands):
                commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
            turn = len(commands) + 1
            insertionInPlace = 0
            continue
        if changeInPlace == 0:
            commands.append([])
        commands[turn-1] = ([f"{turn}-holdMouse"])
        commands[turn-1].append(holdTime)
        if changeInPlace == 1:
            turn = len(commands) + 1
            changeInPlace = 0
            continue
        turn += 1
        continue

    elif command == "w":
        os.system("cls")
        print("\nWait for how many seconds?")
        waiting = input()
        while True:
            try:
                waiting = int(waiting)
                break
            except ValueError:
                os.system("cls")
                print("\nEnter a number.")
                waiting = input()
        if insertionInPlace == 1:
            commands.insert(turn-1, [])
            commands[turn-1] = ([f"{turn}-wait"])
            commands[turn-1].append(waiting)
            for index, i in enumerate(commands):
                commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
            turn = len(commands) + 1
            insertionInPlace = 0
            continue
        if changeInPlace == 0:
            commands.append([])
        commands[turn-1] = ([f"{turn}-wait"])
        commands[turn-1].append(waiting)
        if changeInPlace == 1:
            turn = len(commands) + 1
            changeInPlace = 0
            continue
        turn += 1
        continue

    elif command == "repeat":
        os.system("cls")
        if len(commands) == 0:
            os.system("cls")
            print("\nThere is no command behind to repeat.")
            continue
        if turn > 1:
            if "-repeatPrevious" in commands[turn-2][0]:
                os.system("cls")
                print("\nRecursion error. Cannot assign another repetition.")
                if insertionInPlace == 1:
                    insertionInPlace = 0
                    turn = len(commands) + 1
                continue
        elif turn <= 1:
            os.system("cls")
            print("\nThere is no command behind to repeat.")
            insertionInPlace = 0
            turn = len(commands) + 1
            continue
        while True:
            print("\nRepeat previous command how many times?")
            repeatCount = input()
            try:
                repeatCount = int(repeatCount)
                if repeatCount < 1:
                    os.system("cls")
                    print("\nEnter a positive number.")
                    continue
                break
            except ValueError:
                os.system("cls")
                print("\nEnter a number.")
                continue
        while True:
            os.system("cls")
            print(
                "\nHow long should each iteration of action take?"
                + f"\nEnter a value in seconds. Default duration is {ACTION_DURATION}."
            )
            repeatInterval = input()
            try:
                repeatInterval = float(repeatInterval)
                if repeatInterval < 0:
                    os.system("cls")
                    print("\nEnter a positive number or a float value.")
                    continue
                break
            except ValueError:
                os.system("cls")
                print("\nEnter a number or a float value.")
                continue
        if insertionInPlace == 1:
            commands.insert(turn-1, [])
            commands[turn-1] = ([f"{turn}-repeatPrevious"])
            commands[turn-1].append(repeatCount)
            commands[turn - 1].append(repeatInterval)
            for index, i in enumerate(commands):
                commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
            turn = len(commands) + 1
            insertionInPlace = 0
            continue
        if changeInPlace == 0:
            commands.append([])
        commands[turn-1] = ([f"{turn}-repeatPrevious"])
        commands[turn-1].append(repeatCount)
        commands[turn - 1].append(repeatInterval)
        if changeInPlace == 1:
            turn = len(commands) + 1
            changeInPlace = 0
            continue
        turn += 1
        continue

    elif command == "mr":
        os.system("cls")
        while True:
            print(
                "\nEnter a value to move the cursor relatively on x-axis."
                + "\n100: Go 100 pixels right."
                + "\n-100: Go 100 pixels left."
            )
            xDirection = input()
            try:
                xDirection = int(xDirection)
                break
            except ValueError:
                os.system("cls")
                print("\nPlease enter a number.")
                continue

        os.system("cls")
        while True:
            print(
                "\nEnter a value to move the. cursor relatively on y-axis."
                + "\n100: Go 100 pixels up."
                + "\n-100: Go 100 pixels down."
            )
            yDirection = input()
            try:
                yDirection = int(yDirection)
                break
            except ValueError:
                os.system("cls")
                print("\nPlease enter a number.")
                continue

        if insertionInPlace == 1:
            commands.insert(turn-1, [])
            commands[turn-1] = ([f"{turn}-moveRelative"])
            commands[turn-1].append(xDirection)
            commands[turn - 1].append(yDirection)
            for index, i in enumerate(commands):
                commands[index][0] = f"{index+1}{commandsRegex.search(i[0]).group()}"
            turn = len(commands) + 1
            insertionInPlace = 0
            continue
        if changeInPlace == 0:
            commands.append([])
        commands[turn-1] = ([f"{turn}-moveRelative"])
        commands[turn - 1].append(xDirection)
        commands[turn - 1].append(yDirection)
        if changeInPlace == 1:
            turn = len(commands) + 1
            changeInPlace = 0
            continue
        turn += 1
        continue

    elif command in list(keyinfo.keyToText.keys()):
        changeInPlace, insertionInPlace = key_to_action(command, changeInPlace, insertionInPlace)
        continue

    elif command == "i":
        os.system("cls")
        print(
            "\nTake a screenshot of the image you wish to be found on the screen."
            "\nThen, copy the image file to 'Pictures' folder which is found in the directory of this program."
            "\nPress enter after completing this process."
        )
        input()
        os.system("cls")
        print("\nEnter the full name of the image file, including its extension.")
        ssName = input()
        while True:
            print(f"\nName of the image file saved as '{ssName}'.")
            print("Press enter to continue.")
            decision = input()
            if decision == "":
                break
            else:
                os.system("cls")
                print("\nEnter the full name of the image file, including its extension.")
                ssName = input()
        os.system("cls")
        print("\nWhich command should be used on this image?")
        print("\n'.': Left click\n'r': Right click\n'd': Double click\n'dt': Drag to\n'c': Move cursor")
        decision = input()
        while decision not in list(keyinfo.keyToTextImage.keys()):
            os.system("cls")
            print("\nThere is no such command. Available commands:")
            print("\n'.': Left click\n'r': Right click\n'd': Double click\n'dt': Drag to\n'c': Move cursor")
            decision = input()
        changeInPlace, insertionInPlace = key_to_image_action(decision, ssName, changeInPlace, insertionInPlace)
        continue

    elif command == "qq":
        break
    elif command == "--":
        if len(commands) == 0:
            os.system("cls")
            print("\nThere is no command to delete.")
            error = 1
            continue
        elif len(commands) == 1:
            turn -= 1
            del commands[-1]
            continue
        else:
            notFound = 0
            abortRemoval = 0
            while True:
                os.system("cls")
                if notFound == 1:
                    print("\nThere is no such command.")
                    notFound = 0
                print("\nAll commands:")
                pprint.pprint(commands)
                print("\nDelete which command? 'q' cancels the process.")
                allCommandsForRemoval = []
                for i in range(1, len(commands)+1):
                    allCommandsForRemoval.append(str(i))
                deletedCommand = input()
                if deletedCommand == "q":
                    abortRemoval = 1
                    break
                if deletedCommand not in allCommandsForRemoval:
                    notFound = 1
                    continue
                deletedCommand = int(deletedCommand)
                break
            if abortRemoval == 1:
                abortRemoval = 0
                continue
            del commands[deletedCommand-1]
            for index, i in enumerate(commands):
                commands[index][0] = f'{index+1}{commandsRegex.search(i[0]).group()}'
            turn -= 1
            continue
    elif command == "-":
        if turn > 1:
            turn -= 1
            del commands[-1]
        continue
    else:
        os.system("cls")
        print("\nAll commands:\n")
        for k, v in keyinfo.allAssignmentsExplained.items():
            print(f"{k}: {v}")
        print(f"\nThere is no command called '{command}'. Please check the keys above.")
        error = 1

input("\nEND")
