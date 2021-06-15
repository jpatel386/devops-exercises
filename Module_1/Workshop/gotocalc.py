with open("step_3.txt", 'r') as f:
    text = f.read().splitlines()

got_dupe = False

curIndex = 0

def calculator(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "x":
        return num1 * num2
    elif op == "/":
        return num1 // num2
    else:
        return "That operation is not valid"

def getNextLine(input):
    res = input.split()
    if 2 == len(res):
        return int(res[1])
    else:
        return calculator(res[2], int(res[3]), int(res[4]))


def addAndCheckIfDupe(index):
    seen_statements.append(text[index])
    if len(seen_statements) == len(set(seen_statements)):
            return False
    else:
            return True


seen_statements = []
seen_statements.append(text[curIndex])




while not got_dupe == True:
    print(f"Curindex is {curIndex}")
    nextIndex = getNextLine(text[curIndex]) - 1
    print(f"next index is {nextIndex}")
    is_dupe = addAndCheckIfDupe(nextIndex)
    if is_dupe:
        got_dupe = True
    curIndex = nextIndex

print(f"Dupe line number is {curIndex+1}")
print(text[curIndex])

