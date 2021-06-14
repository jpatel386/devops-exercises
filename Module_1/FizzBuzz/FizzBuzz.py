#stop_number = 105

stop_number = int(input("Please choose an end number: "))

def getFizzBuzz(num):
    res = ""
    if (num % 11) == 0:
        return "BONG"
    if (num % 3) == 0:
        res = res + "FIZZ"
    if (num % 5) == 0:
        res = res + "BUZZ"
    if (num % 7) == 0:
        res = res + "BANG"
    if res == "":
        res = num
    return res

counter = 1

while counter <= stop_number:
    res = getFizzBuzz(counter)
    print(res)
    counter += 1
