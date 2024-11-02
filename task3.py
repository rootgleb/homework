def calculate(spisok):
    stack = []
    for spisok in spisok:
        if spisok in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()
            if spisok == "+":
                stack.append(a + b)
            elif spisok == "-":
                stack.append(a - b)
            elif spisok == "*":
                stack.append(a * b)
            elif spisok == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(spisok))

    return stack[0]


print(calculate(["3", "5", "+"]))
