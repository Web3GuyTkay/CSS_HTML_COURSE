
calculatorLoop = True
storeAnswer = []
while calculatorLoop:
    getInput =input("....  ")
    if getInput == "stop":
        calculatorLoop = False
        print(storeAnswer)
        break
    if getInput == "history":
        print(storeAnswer)
        continue
    if getInput == 0:
        print("You cant give 0")

    print(eval(getInput))
    storeAnswer.append(getInput)

