import os

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
    "write_text": "Type",
    "hotkey": "Press",
    "press_key": "Press",
    "write_variable": "Type variable:",
    "hold_click": "Hold {} key and click on {}",
    "move_relative": "Move mouse",
    "repeat_previous": "Repeat previous command",
    "repeat_pattern": "Repeat all commands",
    "go_website": "Go to website:",
    "play_sound": "Play"
}


def format_commands(command):
    if command[0] == "left_click" or command[0] == "move_cursor" or command[0] == "double_click" \
            or command[0] == "right_click" or command[0] == "middle_click" or command[0] == "drag_to":
        return f"{readableCommands[command[0]]}" \
               + f" | x: {command[1][0]} y: {command[1][1]}"

    elif command[0] == "wait" or command[0] == "hold_mouse":
        if command[1] >= 2:
            return readableCommands[command[0]] + f" for {command[1]} seconds"
        elif command[1] < 2:
            return readableCommands[command[0]] + f" for {command[1]} second"

    elif command[0] == "wait_random":
        return readableCommands[command[0]].format(command[1], command[2])

    elif command[0] == "play_sound":
        return readableCommands[command[0]] + f" '{os.path.basename(command[1])}'"

    elif command[0] == "write_text":
        return readableCommands[command[0]] + f" '{command[1]}'"
    elif command[0] == "hotkey":
        return readableCommands[command[0]] + f" '{hotkeys[command[1]][1]}' hotkey"
    elif command[0] == "press_key":
        return readableCommands[command[0]] + f" '{command[1]}' key"
    elif command[0] == "write_variable":
        return readableCommands[command[0]] + f" {command[1]}"
    elif command[0] == "hold_click":
        return readableCommands[command[0]].format(f"'{command[1]}'", ', '.join(str(i) for i in command[2]))

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
        elif command[1] > 1:
            return readableCommands[command[0]] + f" {command[1]} times, starting from command {command[2]}"
        elif command[1] <= 1:
            return readableCommands[command[0]] + f" {command[1]} time, starting from command {command[2]}"

    elif command[0] == "scroll_up" or command[0] == "scroll_down" or command[0] == "maximize_window":
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

    elif command[0] == "click_image" or command[0] == "move_cursor_on_image" or command[0] == "drag_to_image" \
            or command[0] == "double_click_image" or command[0] == "right_click_image":
        return readableCommands[command[0]] + f" '{os.path.basename(command[1])}', else wait"

    elif command[0] == "click_image_else_pass":
        if command[2] > 1:
            return readableCommands[command[0]] + f" '{os.path.basename(command[1])}' {command[2]} times, else pass"
        elif command[2] <= 1:
            return readableCommands[command[0]] + f" '{os.path.basename(command[1])}' {command[2]} time, else pass"

    elif command[0] == "cursor_on_image_else_pass" \
            or command[0] == "double_click_image_else_pass" or command[0] == "right_click_image_else_pass":
        return readableCommands[command[0]] + f" '{os.path.basename(command[1])}', else pass"

    elif command[0] == "click_color" or command[0] == "click_color_else_pass" \
            or command[0] == "move_cursor_color" or command[0] == "move_cursor_color_else_pass" \
            or command[0] == "double_click_color" or command[0] == "double_click_color_else_pass" \
            or command[0] == "right_click_color" or command[0] == "right_click_color_else_pass" \
            or command[0] == "middle_click_color" or command[0] == "middle_click_color_else_pass" \
            or command[0] == "drag_to_color" or command[0] == "drag_to_color_else_pass":
        spaceBonus = 7 - (len(str(command[1][0])) + len(str(command[1][0])))
        return f"{readableCommands[command[0]]}" \
               + f" | x: {command[1][0]} y: {command[1][1]} {' ' * (spaceBonus-1)}| rgb{command[2]}"

    elif command[0] == "go_website":
        return readableCommands[command[0]] + f" {command[1]}"


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

hotkeys = {
    "copy": ["copy", "ctrl+C"],
    "paste": ["paste", "ctrl+V"],
    "sAll": ["select all", "ctrl+A"],
    "cut": ["cut", "ctrl+X"],
    "undo": ["undo", "ctrl+Z"],
    "redo": ["redo", "ctrl+Y"],
    "save": ["save", "ctrl+S"],
    "save as": ["save as", "ctrl+shift+S"],
    "exit": ["exit", "alt+f4"]
    }

keyboard = {
    "esc": ["pressEscape", "escape"],
    "del": ["pressDelete", "delete"],
    "backspace": ["pressBackspace", "backspace"],
    "enter": ["pressEnter", "enter"],
    "tab": ["pressTab", "tab"],
    "up": ["pressUp", "up arrow"],
    "down": ["pressDown", "down arrow"],
    "right": ["pressRight", "right arrow"],
    "left": ["pressLeft", "left arrow"],
    "home": ["pressHome", "home"],
    "end": ["pressEnd", "end"]
    }

allAssignments = [
    ".", "d", "r", "m", "dt", "c",
    "..", "dd", "rr", "mm", "dtt", "cc",
    "...", "ddd", "rrr", "mmm", "dttt", "ccc", "sound",
    "v", "k", "hot", "p", "max", "w", "wRandom", "i", "web",
    "su", "sd", "h", "hc", "mr", "repeat", "repeatpattern",
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
    "v": "Assign a value",
    "k": "Assign a text",
    "hot": "Assign a hotkey",
    "p": "Assign a key to press",

    "\nOther": "",
    "max": "Maximize current window",
    "w": "Wait * seconds",
    "wRandom": "Wait for random seconds between two values",
    "i": "Initiate image recognition",
    "su": "Scroll up",
    "sd": "Scroll down",
    "h": "Hold left click for * seconds",
    "hc": "Hold and click",
    "web": "Open a website in the default browser",
    "sound": "Play a sound located in sounds folder",
    "repeat": "Repeat previous command",
    "repeatpattern": "Repeat specified pattern"
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

helpMenu = {
    "epi": "List all episodes",
    "name": "Rename an episode",
    "save": "Save the episode and move next one",
    "go": "Go to a specific episode",
    "copy": "Copy the content of an episode to the current one",
    "del": "Delete a specific episode",
    "insep": "Insert an episode after a specific episode",
    "runep": "Run all instructions from a specified episode to the current one",
    "run": "Run current episode",
    "rep": "Replace a command",
    "ins": "Insert a new command after a specified one",
    "-": "Delete last command",
    "--": "Delete a specific command",
    "z": "Move the cursor where it was one command ago",
    "zz": "Move the cursor where it was two commands ago",
    "zzz": "Move the cursor a specific pixel",
    "vdict": "Start Excel to edit the variable dictionary.",
    "maxW": "Maximize current window in 3 seconds",
    "qq": "Quit program"
    }
