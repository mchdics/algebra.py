def parseEq(parts):
    p0, p1, p2, p3, p4 = parts

    #p0 p1 p2 = p4
    if p3 == '=':
        lhs = (p0, p1, p2)
        rhs = p4
        b = int(p4)
        if p1 == "+" or p1 == "-" or p1 == "*" or p1 == "/":
            op = p1
        else:
            print("You do not have an operator or it is misplaced.")
            return None
        
        #Determining a and x position
        if 'a' <= p2 <= 'z':
            varLetter = p2
            a = int(p0)
        elif 'a' <= p0 <= 'z':
            varLetter = p0
            a = int(p2)
            if op == '-':
                b = -b
        else:
            print("Terms not in correct positions.")
            return None
    #p0 = p2 p3 p4
    elif p1 == '=':
        lhs = p0
        rhs = (p2, p3, p4)
        b = int(p0)
        if p3 == "+" or p3 == "-" or p3 == "*" or p3 == "/":
            op = p3
        else:
            print("You do not have an operator or it is misplaced.")
            return None
        
        if 'a' <= p4 <= 'z':
            varLetter = p4
            a = int(p2)
        elif 'a' <= p2 <= 'z':
            varLetter = p2
            a = int(p4)
            if op == '-':
                b = -b
        else:
            print("Terms not in correct positions.")
            return None
    return a, b, op, varLetter

def solveEq(a, b, op):
    varValue = 0
    if op == '+': varValue = b - a
    if op == '-': varValue = a - b
    if op == '*': varValue = b // a
    if op == '/': varValue = a * b
    return varValue

