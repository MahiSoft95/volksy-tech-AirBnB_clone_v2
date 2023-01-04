#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvlist = sys.argv[1:]
    if len(argvlist) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    from mahifuns import add, sub, mul, div
    a = int(args_list[0])
    b = int(args_list[2])
    opr = int(args_list[1])
    if opr == '+':
        res=add(a,b)
    elif opr == '-':
        res=sub(a,b)
    elif opr == '*':
        res=mul(a,b)
    elif opr == '/':
        res=div(a,b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{}+{}={}".div(a, b, res))
    exit()
