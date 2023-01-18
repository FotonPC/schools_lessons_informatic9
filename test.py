def format_out(s, base=10):
    res = ""
    if base == 2:
        if len(s) > 4:
            while len(s) > 4:
                res = s[-4::] + ' ' + res
                s = s[:-4:]
            res = s + ' ' + res
            #res = res[:-2:]
        else:
            res = s
    elif base == 10:
        if len(s) > 3:
            while len(s) > 3:
                res = s[-3::] + ' ' + res
                s = s[:-3:]
            res = s + ' ' + res
            #res = res[:-2:]
        else:
            res = s
    elif base == 16:
        if len(s) > 2:
            while len(s) > 2:
                res = s[-2::] + ' ' + res
                s = s[:-2:]
            res = s + ' ' + res
            #res = res[:-2:]
        else:
            res = s
    else:
        res = s
    return res.strip()
print(format_out(input()))