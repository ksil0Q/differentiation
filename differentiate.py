from tokenizer import tokenize, TOK


class Expression:  # учимся брать производную x^2

    expr = ''
    left = []
    right = []
    operation = ''

    def __init__(self, expr: str):
        self.expr = expr
        self.left, self.right, self.operation = self.parse_expr(expr)

    def parse_expr(self, expr):
        # x^2 + 2x
        part = ''
        list_of_parts = []
        operation = ''
        flag = False
        list_sign = []

        for token in tokenize(expr):
            if token.kind == 1:
                list_sign.append(token.txt)

        operation = self.priority(list_sign)
        part_expr = expr.split(operation)
        part_expr.append(operation)
        print(part_expr)
        for token in tokenize(expr):
            kind_of_sign = token.kind
            sign = token.txt
            if kind_of_sign == 23:
                sign = sign.replace('x', '*x')

        #     if kind_of_sign != 1 or sign == '^' or flag:
        #         part += sign
        #     else:
        #         operation = sign
        #         list_of_parts.append(part)
        #         part = ''
        #         flag = True
        #
        # if part:
        #     list_of_parts.append(part)
        #     list_of_parts.append(operation)
        #     #print(list_of_parts)
        return part_expr[0], part_expr[1], part_expr[2]
    def priority(self, signs):
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