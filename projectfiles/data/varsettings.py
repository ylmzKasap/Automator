import openpyxl


def get_vars(projectPath, workbookType):
    if workbookType == "variable":
        workbookName = "Variable Database.xlsx"
    elif workbookType == "wildcard":
        workbookName = "Wildcard Database.xlsx"
    elif workbookType == "search":
        workbookName = "Searched Database.xlsx"

    wb = openpyxl.load_workbook(f"{projectPath}\\{workbookName}")
    sheet = wb.active

    allRows = list(sheet.rows)
    words = []
    wordsDict = {}

    # Get all words in the file, separated by rows
    for row in allRows:
        words.append([])
        for index, column in enumerate(row):
            if column.value is not None:
                words[-1].append(column.value)

    # Delete empty rows
    for i, row in enumerate(words):
        if not row:
            del words[i]

    variableIndex = 0
    for rows in words:
        for column in rows:
            wordsDict[f"v{variableIndex+1}"] = str(column)
            variableIndex += 1

    return wordsDict, words
