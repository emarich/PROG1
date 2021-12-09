import re # for regex

# text file with fucked up code from AIS exam
codeTxt = r"C:\Users\emari\Desktop\projects\PROG1\Test\code.txt"
# when error occurres during edited code execution, save edited code to this file
codePy = r"C:\Users\emari\Desktop\projects\PROG1\Test\new_code.py"

with open(codeTxt, 'r') as file:
    lines = []
    for line in file:
        # if string or bool values are found, save it and replace it after lowering every character in code
        printStrBool = re.findall('([\'\"].+?[\'\"]|True|False)', line)
        printStrBool = printStrBool[0] if printStrBool else ""
        line = line.lower().replace('_',' ').replace(printStrBool.lower(), printStrBool)
        lines.append(line)

try:
    exec("".join(lines)) # execute edited code
except Exception as e:
    with open(codePy, 'w') as file:
        file.write("".join(lines))
    print(f'>>> Error: {e}\n>>> You can find code in {codePy}')