def eval_without_bracket(string):
    if 'or' in string:
        string = string + ' '
        re = string.index("or")
        return eval_without_bracket(string[:re:]) or eval_without_bracket(string[re + 2:len(string) - 1])
    if 'and' in string:
        string = string + ' '
        re = string.index("and")
        return eval_without_bracket(string[:re:]) and eval_without_bracket(string[re + 3:len(string) - 1])
    if '!=' in string:
        string = string + ' '
        re = string.index("!=")
        return eval_without_bracket(string[:re:]) != eval_without_bracket(string[re + 2:len(string) - 1])
    if '<' in string:
        string = string + ' '
        re = string.index("<")
        return eval_without_bracket(string[:re:]) < eval_without_bracket(string[re + 1:len(string) - 1])
    if '>' in string:
        string = string + ' '
        re = string.index(">")
        return eval_without_bracket(string[:re:]) > eval_without_bracket(string[re + 1:len(string) - 1])
    if '==' in string:
        string = string + ' '
        re = string.index("==")
        return eval_without_bracket(string[:re:]) == eval_without_bracket(string[re + 2:len(string) - 1])
    if '+' in string:
        string = string + ' '
        re = string.index("+")
        return eval_without_bracket(string[:re:]) + eval_without_bracket(string[re + 1:len(string) - 1])
    if '-' in string:
        string = string + ' '
        re = string.index("-")
        return eval_without_bracket(string[0:re]) - eval_without_bracket(string[re + 1:len(string) - 1])
    if '*' in string:
        string = string + ' '
        re = string.index("*")
        if string[re + 1] != '*':
            return eval_without_bracket(string[0:re]) * eval_without_bracket(string[re + 1:len(string) - 1])
    if '/' in string:
        string = string + ' '
        re = string.index("/")
        if string[re + 1] != '/':
            return eval_without_bracket(string[0:re]) / eval_without_bracket(string[re + 1:len(string) - 1])
    if '%' in string:
        string = string + ' '
        re = string.index("%")
        return eval_without_bracket(string[0:re]) % eval_without_bracket(string[re + 1:len(string) - 1])
    if '//' in string:
        string = string + ' '
        re = string.index("//")
        return eval_without_bracket(string[0:re]) // eval_without_bracket(string[re + 2:len(string) - 1])
    if '**' in string:
        string = string + ' '
        re = string.index("**")
        return eval_without_bracket(string[0:re]) ** eval_without_bracket(string[re + 2:len(string) - 1])
    if not '.' in string:
        return int(string)
    else:
        return float(string)


def evalstr(string):
    string = string.replace(" ", "")
    if not '(' in string:
        return eval_without_bracket(string)
    i = 0
    p0s = False
    pos0s = 0
    s = 0
    res1 = 0
    while i < len(string):
        if p0s and string[i] == '(':
            pos0s = i
        if string[i] == '(':
            s += 1;
            p0s = True
        elif string[i] == ')':
            s -= 1
        if s == 0 and p0s:
            res1 = i
            break
        i += 1
    if pos0s > 0 and res1 < len(string) - 1:
        return evalstr(string[0:pos0s] + str(evalstr(string[pos0s + 1:res1])) + string[res1 + 1::])
    elif pos0s == 0 and res1 < len(string) - 1:
        return evalstr(str(evalstr(string[1:res1])) + string[res1 + 1::])
    elif pos0s > 0 and res1 == len(string) - 1:
        return evalstr(string[0:pos0s] + str(evalstr(string[pos0s + 1:res1])))
    else:
        return evalstr(string[1:-1])


if __name__ == '__main__':

    while True:
        inp = input()
        print(evalstr(inp), eval(inp))
