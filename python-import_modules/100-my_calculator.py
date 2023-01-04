#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvlist = sys.argv[1:]
    if len(argvlist) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    from mahifuns import add, sub, mul, div
    a = int(argvlist[0])
    b = int(argvlist[2])
    opr = argvlist[1]
    if opr == '+':
        res = add(a, b)
    elif opr == '-':
        res = sub(a, b)
    elif opr == '*':
        res = mul(a, b)
    elif opr == '/':
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, opr, b, res))
    exit()
