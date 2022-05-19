from tokenizer import tokenize


def get_priority(signs):
    dict_of_sign = {}
    min_value = 10
    key = ""
    for sign in signs:
        if sign == "+" or sign == "-":
            dict_of_sign[sign] = 0
        if sign == "*" or sign == "/":
            dict_of_sign[sign] = 1
        if sign == "^":
            dict_of_sign[sign] = 2
        if sign == "cos" or sign == "sin" or sign == "tg" or sign == "ctg":
            dict_of_sign[sign] = 3
    for k in dict_of_sign.keys():
        if min_value > dict_of_sign[k]:
            min_value = dict_of_sign[k]
            key = k
    return key


def parse_expr(expr):
    part = ''
    list_of_parts = []
    list_sign = []

    for token in tokenize(expr):
        if token.kind == 1:
            list_sign.append(token.txt)

    operation = get_priority(list_sign)
    oper = operation

    for token in tokenize(expr):
        if token.kind == 23:
            token.txt = token.txt.replace('x', '*x')
        if token.txt != oper:
            part += token.txt
        else:
            list_of_parts.append(part)
            part = ''
            oper = 'Time'
            list_of_parts.append(operation)

    if part:
        list_of_parts.append(part)
    return list_of_parts

