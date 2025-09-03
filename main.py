from logic import parseEq, solveEq

#Takes input
def inputEq():
    eq = input("Enter an equation: ")
    parts = eq.split()

    #Exit condition
    if eq == '0':
        return 0
    #Validation
    elif len(parts) != 5:
        print("Your equation is not composed of exactly 5 parts. Try again: ")
        return None
    else:
        p0, p1, p2, p3, p4 = parts
        if p3 != '=' and p1 != '=':
            print("Your equation does not contain an equal sign or it is misplaced. Try again: ")
            return None
        else:
            return parts

def printSolution(varLetter, varValue):
    print(f"{varLetter} = {varValue}")

def main():
    #Prompt for equation until exit
    while True:
        eq = inputEq()
        if eq == 0:
            break
        if eq == None:
            continue
        else:
            parsed = parseEq(eq)
        if parsed == None:
            continue
        else:
            a, b, op, varLetter = parsed 
        varValue = solveEq(a, b, op)
        printSolution(varLetter, varValue)


if __name__ == "__main__":
    main()