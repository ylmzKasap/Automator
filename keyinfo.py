keyToText = {
    '.': '-normal_click',
    '..': '-click_color',
    'c': '-move_cursor',
    'cc': '-moveCursor_color',
    'd': '-double_click',
    'dd': '-doubleClick_color',
    'r': '-right_click',
    'rr': '-rightClick_color',
    'm': '-middle_click',
    'mm': '-middleClick_color',
    'dt': '-drag_to',
    'dtt': '-dragTo_color',
    'su': '-scrollUp',
    'sd': '-scrollDown',
    'mr': '-moveRelative',
    }

keyToTextImage = {
    '.': '-clickImage',
    'c': '-moveCursorImage',
    'd': '-doubleClickImage',
    'r': '-rightClickImage',
    'dt': '-dragToImage'
    }

hotkeys = {
    'copy': ['-copy', 'ctrl+C'],
    'paste': ['-paste', 'ctrl+V'],
    'sAll': ['-selectAll', 'ctrl+A'],
    'cut': ['-cutSelected', 'ctrl+X'],
    'undo': ['-undo', 'ctrl+Z'],
    'redo': ['-redo', 'ctrl+Y'],
    'save': ['-saveIt', 'ctrl+S'],
    'save as': ['-saveAs', 'ctrl+shift+S'],
    'exit': ['-exitIt', 'alt+f4']
    }

keyboard = {
    'esc': ['-pressEscape', 'escape'],
    'del': ['-pressDelete', 'delete'],
    'backspace': ['-pressBackspace', 'backspace'],
    'enter': ['-pressEnter', 'enter'],
    'tab': ['-pressTab', 'tab'],
    'up': ['-pressUp', 'up arrow'],
    'down': ['-pressDown', 'down arrow'],
    'right': ['-pressRight', 'right arrow'],
    'left': ['-pressLeft', 'left arrow'],
    'home': ['-pressHome', 'home'],
    'end': ['-pressEnd', 'end']
    }

allAssignments = [
    '.', 'd', 'r', 'm', 'dt', 'c',
    '..', 'dd', 'rr', 'mm', 'dtt', 'cc',
    'v', 'k', 'hot', 'p', 'max', 'w', 'i',
    'su', 'sd', 'h', 'hc', 'mr'
]

allAssignmentsExplained = {
    'Common Mouse Commands': "",
    '.': 'Left click',
    'd': 'Double click',
    'r': 'Right click',
    'm': 'Middle click',
    'dt': 'Click and drag to coordinate',
    'c': 'Move cursor to',
    'mr': 'Move cursor relative to its position',
    '\nRepeat the last letter to perform the action if the colors match': "",
    'dd': "Double click if the colors match",

    '\nKeyboard Commands': "",
    'v': 'Assign a value',
    'k': 'Assign a text',
    'hot': 'Assign a hotkey',
    'p': 'Assign a key to press',

    '\nOther': "",
    'max': 'Maximize current window',
    'w': 'Wait * seconds',
    'i': 'Initiate image recognition',
    'su': 'Scroll up',
    'sd': 'Scroll down',
    'h': 'Hold left click for * seconds',
    'hc': 'Hold and click',
    }


helpMenu = {
    'epi': 'List all episodes',
    'name': 'Rename an episode',
    'save': 'Save the episode and move next one',
    'go': 'Go to a specific episode',
    'copy': 'Copy the content of an episode to the current one',
    'del': 'Delete a specific episode',
    'insep': 'Insert an episode after a specific episode',
    'runep': 'Run all instructions from a specified episode to the current one',
    'run': 'Run current episode',
    'rep': 'Replace a command',
    'ins': 'Insert a new command after a specified one',
    '-': 'Delete last command',
    '--': 'Delete a specific command',
    'z': 'Move the cursor where it was one command ago',
    'zz': 'Move the cursor where it was two commands ago',
    'zzz': 'Move the cursor a specific pixel',
    'maxW': 'Maximize current window in 3 seconds',
    'qq': 'Quit program'
    }
