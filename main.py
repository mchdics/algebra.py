from logic import inputEq, parseEq, solveEq, printSolution

def main():
    parts = inputEq()
    a, b, op, varLetter = parseEq(parts)
    varValue = solveEq(a, b, op)
    printSolution(varLetter, varValue)

if __name__ == "__main__":
    main()