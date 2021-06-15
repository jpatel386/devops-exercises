#operator = input("What calculation would you like to do? ")
#number_1 = int(input("What is the first number? "))
#number_2 = int(input("What is the second number? "))

def calculator(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "x":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "That operation is not valid"

#print(f"{number_1} {operator} {number_2} = {calculator(operator, number_1, number_2)}")



with open("step_2.txt", 'r') as f:
    text = f.read().splitlines()
#don't need to close this since we start with a "with" and when we exit the block it takes care of that for us

results = []

for i in text:
    r = i.split()
    ans = calculator(r[1], int(r[2]), int(r[3]))
    results.append(ans)


print(sum(results))

