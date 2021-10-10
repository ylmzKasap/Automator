import os
from openpyxl.utils import get_column_letter

helpMenu = {
    "epi": "List all episodes",
    "name": "Rename an episode",
    "save": "Save the episode and move next one",
    "saves": "Save the episode and stay",
    "go": "Go to a specific episode",
    "copy": "Copy the content of an episode to the current one",
    "del": "Delete a specific episode",
    "insep": "Insert an episode after a specific episode",
    "runep": "Run all instructions from a specified episode to the current one",
    "run": "Run current episode",
    "runF": "Run all commands starting from a particular command",
    "rep": "Replace a command",
    "ins": "Insert a new command after a specified one",
    "-": "Delete last command",
    "--": "Delete a specific command",
    "z": "Move the cursor where it was one command ago",
    "zz": "Move the cursor where it was two commands ago",
    "zzz": "Move the cursor a specific pixel",
    "vdb": "Start Excel to edit the variable database",
    "wdb": "Start Excel to edit wildcard database",
    "search": "Adjust the file search settings and copy the necessary files",
    "sc": "Search and copy the files in a specified database & adjust variables and wildcards",
    "maxW": "Maximize current window in 3 seconds",
    "qq": "Quit program"
    }

allAssignments = [
    ".", "d", "r", "m", "dt", "c", "click",
    "..", "dd", "rr", "mm", "dtt", "cc",
    "...", "ddd", "rrr", "mmm", "dttt", "ccc", "sound",
    "v", "k", "hot", "p", "max", "w", "wRandom", "i", "web",
    "su", "sd", "h", "hc", "mr", "repeat", "repeatpattern",
    "icon", "wild", "rfw", "l", "com", "hk"
]

allAssignmentsExplained = {
    "Common Mouse Commands": "",
    ".": "Left click",
    "d": "Double click",
    "r": "Right click",
    "m": "Middle click",
    "dt": "Click and drag to coordinate",
    "c": "Move cursor to",
    "mr": "Move cursor relative to its position",
    "\nRepeat the last letter to perform the action if both color values match": "",
    "dd": "Double clicks where the cursor is, if the colors match, else throws an error and waits.",
    "ddd": "Double clicks if the colors match, if not, continues like nothing happened.",

    "\nKeyboard Commands": "",
    "v": "Assign a variable",
    "k": "Assign a text",
    "hk": "Hold a key",
    "hot": "Assign a hotkey",
    "p": "Assign a key to press",
    "wild": "Assign a wildcard",

    "\nOther": "",
    "max": "Maximize current window",
    "l": "Launch a file",
    "w": "Wait * seconds",
    "wRandom": "Wait for random seconds between two values",
    "i": "Image recognition",
    "icon": "Conditional image recognition",
    "su": "Scroll up",
    "sd": "Scroll down",
    "click": "Click wherever the cursor is",
    "h": "Hold left click for * seconds",
    "hc": "Hold and click",
    "web": "Open a website in the default browser",
    "sound": "Play a sound located in sounds folder",
    "repeat": "Repeat previous command",
    "repeatpattern": "Repeat specified pattern",
    "rfw": "Repeat the pattern for the rows of wildcards available",
    "split": "Split the cells of wildcard database.",
    "com": "Leave a comment"
    }

imageCommandsExplained = {
    "\nSearch until the image is found and then": "",
    "'.'": "Left click",
    "'r'": "Right click",
    "'d'": "Double click",
    "'dt'": "Drag to",
    "'c'": "Move cursor",

    "\nSearch the image once, if exists": "",
    "'..'": "Left click",
    "'rr'": "Right click",
    "'dd'": "Double click",
    "'cc'": "Move cursor"
}

imageConditionalAssignments = [
    ".", "d", "r", "m", "dt", "c", "mr", "v", "k", "click",
    "hot", "p", "max", "w", "wRandom", "web", "i", "l", "hk",
    "su", "sd", "h", "hc", "sound", "repeat", "repeatpattern", "com"
]

imageConditionalAssignmentsExplained = {
    "Common Mouse Commands": "",
    ".": "Left click",
    "d": "Double click",
    "r": "Right click",
    "m": "Middle click",
    "dt": "Click and drag to coordinate",
    "c": "Move cursor to",
    "mr": "Move cursor relative to its position",

    "\nKeyboard Commands": "",
    "v": "Assign a variable",
    "k": "Assign a text",
    "hk": "Hold a key",
    "hot": "Assign a hotkey",
    "p": "Assign a key to press",

    "\nOther": "",
    "max": "Maximize current window",
    "l": "Launch a file",
    "w": "Wait * seconds",
    "wRandom": "Wait for random seconds between two values",
    "web": "Open a website in the default browser",
    "i": "Image recognition",
    "su": "Scroll up",
    "sd": "Scroll down",
    "click": "Click wherever the cursor is",
    "h": "Hold left click for * seconds",
    "hc": "Hold and click",
    "sound": "Play a sound located in sounds folder",
    "repeat": "Repeat previous command",
    "repeatpattern": "Repeat specified pattern",
    "com": "Leave a comment"
    }

# For assignments which are used in key_to_action function
keyToText = {
    ".": "left_click",
    "..": "click_color",
    "...": "click_color_else_pass",
    "c": "move_cursor",
    "cc": "move_cursor_color",
    "ccc": "move_cursor_color_else_pass",
    "d": "double_click",
    "dd": "double_click_color",
    "ddd": "double_click_color_else_pass",
    "r": "right_click",
    "rr": "right_click_color",
    "rrr": "right_click_color_else_pass",
    "m": "middle_click",
    "mm": "middle_click_color",
    "mmm": "middle_click_color_else_pass",
    "dt": "drag_to",
    "dtt": "drag_to_color",
    "dttt": "drag_to_color_else_pass",
    "su": "scroll_up",
    "sd": "scroll_down",
    }

keyToTextImage = {
    ".": "click_image",
    "c": "move_cursor_on_image",
    "d": "double_click_image",
    "r": "right_click_image",
    "dt": "drag_to_image",
    "..": "click_image_else_pass",
    "cc": "cursor_on_image_else_pass",
    "dd": "double_click_image_else_pass",
    "rr": "right_click_image_else_pass"
    }

hotkeyExamples = [
    "ctrl c", "ctrl v", "ctrl a", "win d"
    "ctrl shift s", "alt f4", "alt tab"
    ]

availableHotkeys = [
    "ctrl c", "ctrl v",  "ctrl x", "ctrl a", "ctrl z",
    "alt tab", "win d", "ctrl w", "ctrl n", "ctrl s",
    "ctrl shift n", "win .", "win b", "win m", "ctrl enter",
    "ctrl alt delete", "win r", "win shift s", "ctrl b",
    "ctrl u", "ctrl I",  "ctrl shift a", "shift enter",
    "ctrl shift s", "alt f4", "ctrl shift t", "ctrl r",
    "ctrl shift c", "ctrl shift o", "win alt g", "ctrl p"
]

keyboardKeysExamples = [
    "esc", "delete", "backspace", "enter",
    "tab", "up", "down", "right", "left",
    "home", "end", "f1", "a", "b", "c",
    "1", "2", "3", "win", "volumemute", "volumeup",
    "volumedown",  "printscreen", "space"
    ]

availableKeyboardKeys = [
    "esc", "del", "backspace", "enter", "tab", "up", "down",
    "right", "left", "home", "end", "volumemute", "volumeup",
    "volumedown", "f1", "f2", "f3", "f4", "f5", "f6", "f7",
    "f8", "f9", "f10", "f11", "f12", "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "w", "z", "0",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", ".", ",", "\"",
    "printscreen", "win", "space"
]

readableCommands = {
    "left_click": "Left click",
    "click_color": "Click if colors match, else wait",
    "click_color_else_pass": "Click if colors match, else pass",
    "move_cursor": "Move cursor",
    "move_cursor_color": "Move cursor if colors match, else wait",
    "move_cursor_color_else_pass": "Move cursor if colors match, else pass",
    "double_click": "Double click",
    "double_click_color": "Double click if colors match, else wait",
    "double_click_color_else_pass": "Double click if colors match, else pass",
    "right_click": "Right click",
    "right_click_color": "Right click if colors match, else wait",
    "right_click_color_else_pass": "Right click if colors match, else pass",
    "middle_click": "Middle click",
    "middle_click_color": "Middle click if colors match, else wait",
    "middle_click_color_else_pass": "Middle click if color match, else pass",
    "drag_to": "Click and drag to",
    "drag_to_color": "Click and drag if colors match, else wait",
    "drag_to_color_else_pass": "Click and drag if colors match, else pass",
    "scroll_up": "Scroll up",
    "scroll_down": "Scroll down",
    "click_image": "Click on",
    "click_image_else_pass": "Click on",
    "move_cursor_on_image": "Move cursor on",
    "cursor_on_image_else_pass": "Move cursor on",
    "double_click_image": "Double click on",
    "double_click_image_else_pass": "Double click on",
    "right_click_image": "Right click on",
    "right_click_image_else_pass": "Right click on",
    "drag_to_image": "Drag to",
    "wait": "Wait",
    "wait_random": "Wait for random seconds between {} and {}",
    "maximize_window": "Maximize current window",
    "hold_mouse": "Hold left click",
    "hold_key": "Hold '{}' key for {} seconds",
    "write_text": "Type",
    "hotkey": "Press",
    "press_key": "Press",
    "write_variable": "Type variable:",
    "hold_click": "Hold {} key and click on '{}'",
    "move_relative": "Move mouse",
    "repeat_previous": "Repeat previous command",
    "repeat_pattern": "Repeat all commands",
    "go_website": "Go to website:",
    "play_sound": "Play",
    "image_conditional": "",
    "wildcard": "Write wildcard",
    "repeat_commands_for_wildcards": " --Start repeating for wildcards--",
    "end_repeat_commands_for_wildcards": "--End repeating for wildcards--",
    "launch": "Launch",
    "search_files": "Search '{}' for",
    "blind_click": "Click wherever the cursor is",
    "comment": "# {} #"
}


def format_commands(command):
    if (
            command[0] == "left_click"
            or command[0] == "move_cursor"
            or command[0] == "double_click"
            or command[0] == "right_click"
            or command[0] == "middle_click"
            or command[0] == "drag_to"):
        return (
                f"{readableCommands[command[0]]}"
                + f" | x: {command[1][0]} y: {command[1][1]}")

    elif command[0] == "wait" or command[0] == "hold_mouse":
        if command[1] >= 2:
            return readableCommands[command[0]] + f" for {command[1]} seconds"
        elif command[1] < 2:
            return readableCommands[command[0]] + f" for {command[1]} second"

    elif command[0] == "wait_random":
        return readableCommands[command[0]].format(command[1], command[2])

    elif command[0] == "play_sound":
        waitOrPass = ""
        if command[2] == "wait":
            waitOrPass = " and wait until it ends"
        return readableCommands[command[0]] + f" '{command[1]}'{waitOrPass}"

    elif command[0] == "write_text":
        return readableCommands[command[0]] + f" '{command[1]}'"
    elif command[0] == "hotkey":
        return readableCommands[command[0]] + f" '{command[1]}' hotkey"
    elif command[0] == "press_key":
        return readableCommands[command[0]] + f" '{command[1]}' key"
    elif command[0] == "write_variable":
        return readableCommands[command[0]] + f" {command[1]}"
    elif command[0] == "hold_click":
        return readableCommands[command[0]].format(f"'{command[1]}'", ', '.join(str(i) for i in command[2]))
    elif command[0] == "hold_key":
        return readableCommands[command[0]].format(command[1], command[2])

    elif command[0] == "repeat_previous":
        if command[1] == "infinite":
            return readableCommands[command[0]] + f" {command[1]} times"
        elif command[1] > 1:
            return readableCommands[command[0]] + f" {command[1]} times"
        elif command[1] <= 1:
            return readableCommands[command[0]] + f" {command[1]} time"

    elif command[0] == "repeat_pattern":
        if command[1] == "infinite":
            return readableCommands[command[0]] + f" {command[1]} times, starting from command {command[2]}"
        elif command[1] == "wildcard":
            return (
                    readableCommands[command[0]]
                    + f" for the rows of variables, starting from command {command[2]}"
            )
        elif command[1] > 1:
            return readableCommands[command[0]] + f" {command[1]} times, starting from command {command[2]}"
        elif command[1] <= 1:
            return readableCommands[command[0]] + f" {command[1]} time, starting from command {command[2]}"

    elif (
            command[0] == "scroll_up"
            or command[0] == "scroll_down"
            or command[0] == "maximize_window"
            or command[0] == "wildcard"
            or command[0] == "repeat_commands_for_wildcards"
            or command[0] == "end_repeat_commands_for_wildcards"
            or command[0] == "blind_click"
    ):
        return readableCommands[command[0]]

    elif command[0] == "move_relative":
        xDirection = ""
        yDirection = ""
        if command[1] >= 0:
            xDirection = "right"
        elif command[1] < 0:
            xDirection = "left"
        if command[2] >= 0:
            yDirection = "down"
        elif command[2] < 0:
            yDirection = "up"
        return (f"{readableCommands[command[0]]} {abs(command[1])} pixels {xDirection}"
                + f" and {abs(command[2])} pixels {yDirection}")

    elif (
            command[0] == "click_image"
            or command[0] == "move_cursor_on_image"
            or command[0] == "drag_to_image"
            or command[0] == "double_click_image"
            or command[0] == "right_click_image"):
        return readableCommands[command[0]] + f" '{os.path.basename(command[1])}', else wait"

    elif command[0] == "click_image_else_pass":
        if command[2] > 1:
            return readableCommands[command[0]] + f" '{os.path.basename(command[1])}' {command[2]} times, else pass"
        elif command[2] <= 1:
            return readableCommands[command[0]] + f" '{os.path.basename(command[1])}' {command[2]} time, else pass"

    elif (
            command[0] == "cursor_on_image_else_pass"
            or command[0] == "double_click_image_else_pass"
            or command[0] == "right_click_image_else_pass"):
        return readableCommands[command[0]] + f" '{os.path.basename(command[1])}', else pass"

    elif (
            command[0] == "click_color"
            or command[0] == "click_color_else_pass"
            or command[0] == "move_cursor_color"
            or command[0] == "move_cursor_color_else_pass"
            or command[0] == "double_click_color"
            or command[0] == "double_click_color_else_pass"
            or command[0] == "right_click_color"
            or command[0] == "right_click_color_else_pass"
            or command[0] == "middle_click_color"
            or command[0] == "middle_click_color_else_pass"
            or command[0] == "drag_to_color"
            or command[0] == "drag_to_color_else_pass"):
        spaceBonus = 7 - (len(str(command[1][0])) + len(str(command[1][0])))
        return (
                f"{readableCommands[command[0]]}"
                + f" | x: {command[1][0]} y: {command[1][1]} {' ' * (spaceBonus-1)}| rgb{command[2]}")

    elif command[0] == "go_website":
        return readableCommands[command[0]] + f" {command[1]}"

    elif command[0] == "launch":
        return readableCommands[command[0]] + f" '{os.path.basename(command[1])}'"

    elif command[0] == "image_conditional":
        imageCommandsFormatted = []
        for imageCommand in command[2]:
            imageCommandsFormatted.append(format_commands(imageCommand))
        commandBlock = ""
        for index, imageCommand in enumerate(imageCommandsFormatted):
            commandBlock += f"\n{' '  * 4}{get_column_letter(index + 1).lower()}. {imageCommand}"
        if command[3] == "if" or command[3] == "while":
            return (
                    f"{command[3].title()} '{os.path.basename(command[1])}'"
                    f" is on the screen: {commandBlock}"
            )
        elif command[3] == "if not" or command[3] == "while not":
            return (
                    f"{command[3].split()[0].title()} '{os.path.basename(command[1])}'"
                    f" is not on the screen: {commandBlock}"
            )

    elif command[0] == "search_files":
        return (
                readableCommands[command[0]].format(os.path.basename(command[1]))
                + f" {', '.join(command[2])} files and copy all."
        )

    elif command[0] == "comment":
        return (
                readableCommands[command[0]].format(os.path.basename(command[1]))
        )
