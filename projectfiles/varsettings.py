import openpyxl


def get_vars(projectPath):
    workbookName = "Variable Dictionary.xlsx"

    wb = openpyxl.load_workbook(f"{projectPath}\\{workbookName}")
    sheet = wb.active

    allColumns = list(sheet.columns)
    words = []
    wordsDict = {}

    for column in allColumns:  # Get words
        for index, row in enumerate(column):
            if row.value is not None:
                words.append(row.value)

    for index, word in enumerate(words):
        wordsDict[f"v{index+1}"] = word
    return wordsDict
