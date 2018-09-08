#!/usr/bin/env python3

cipher = """
PNK{4ultpa pnk}
"""

char_dic = {
        "U":"C",
        "j":"p",
        "e":"a",
        "d":"w",
        "U":"C",
        "F":"T",
        "G":"F",
        "l":"h",
        "f":"t",
        "j":"p",
        "o":"s",
        "c":"e",
        "b":"l",
        "a":"o",
        "r":"m",
        "t":"i",
        "i":"r",
        "h":"v",
        "z":"d",
        "m":"y",
        "q":"g",
        "n":"k",
        "p":"n",
        "w":"u",
        "s":"b",
        "x":"q",
        "y":"x",
        "v":"z",
        "k":"j",
        }

char = [ord(char_dic[i].lower()) for i,_ in char_dic.items()]
char.sort()
print(char)

tmp_dic = {}
for k,v in char_dic.items():
    tmp_dic[k.upper()] = v.upper()
    tmp_dic[k.lower()] = v.lower()
char_dic.update(tmp_dic)

plain = ''
for i in cipher:
    if i in char_dic:
        plain += char_dic[i]
    elif i.isalpha():
        plain += "*"
        plain += i
    else:
        plain += i

print(plain)
