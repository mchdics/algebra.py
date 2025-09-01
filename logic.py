def inputEq():
    validator = 0
    while validator == 0:
        eq = input("Enter an equation: ")
        terms = eq.split()
        t0, t1, t2, t3, t4 = terms
        #Validation
        if t3 != "=" and t1 != "=":
            print("Your equation does not contain an equal sign. Try again: ")
        else:
            validator = 1
            return terms

def parseEq(terms):
    t0, t1, t2, t3, t4 = terms

    #t0 t1 t2 = t4
    if t3 == "=":
        lhs = (t0, t1, t2)
        rhs = t4
        b = int(t4)
        op = t1

        #Determining a and x position
        if "a" <= t2 <= "z":
            varLetter = t2
            a = int(t0)
        elif "a" <= t0 <= "z":
            varLetter = t0
            a = int(t2)
        else: print("Variable not in correct position.")

    #t0 = t2 t3 t4
    elif t2 == "=":
        lhs = t0
        rhs = (t2, t3, t4)
        b = int(t0)
        op = t2

        if "a" <= t2 <= "z":
            varLetter = t2
            a = int(t4)
        elif "a" <= t4 <= "z":
            varLetter = t4
            a = int(t2)
        else: print("Variable not in correct position.")
    else:
        print("Equal sign not in correct position.")
    return a, b, op, varLetter

def solveEq(a, b, op):
    varValue = 0
    if op == "+": varValue = b - a
    if op == "-": varValue = a - b
    if op == "*": varValue = b / a
    if op == "/": varValue = a / b
    return varValue

def printSolution(varLetter, varValue):
    print(f"{varLetter} = {varValue}")