def main():
    validator = 0
    while validator == 0:
        eq = input("Enter an equation: ")
        parts = eq.split()
        p0, p1, p2, p3, p4 = parts
        #Validation
        if p3 != "=" and p1 != "=":
            print("Your equation does not contain an equal sign. Try again: ")
        else: validator = 1
    
    #p0 p1 p2 = p4
    if p3 == "=":
        lhs = (p0, p1, p2)
        rhs = p4
        b = int(p4)
        op = p1

        #Determining a and x position
        if "a" <= p2 <= "z":
            varLetter = p2
            a = int(p0)
        elif "a" <= p0 <= "z":
            varLetter = p0
            a = int(p2)
        else: print("Variable not in correct position.")
    #p0 = p2 p3 p4
    elif p2 == "=":
        lhs = p0
        rhs = (p2, p3, p4)
        b = int(p0)
        op = p2

        if "a" <= p2 <= "z":
            varLetter = p2
            a = int(p4)
        elif "a" <= p4 <= "z":
            varLetter = p4
            a = int(p2)
        else: print("Variable not in correct position.")
    else:
        print("Equal sign not in correct position.")

    #Logic
    varValue = 0
    if op == "+": varValue = b - a
    if op == "-": varValue = a - b
    if op == "*": varValue = b / a
    if op == "/": varValue = a / b

    #Display
    print(f"{varLetter} = {varValue}")

if __name__ == "__main__":
    main()