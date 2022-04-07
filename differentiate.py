from tokenizer import tokenize, TOK


class Expression:  # учимся брать производную x^2

    expr = ''

    def __init__(self, expr: str):
        self.expr = expr
        self.parse_expr(expr)

    def parse_expr(self, expr):
        # 2x^2 + 4
        for token in tokenize(expr):
            kind, txt, val = token
            print(TOK.descr[kind], txt, val)

        # return что-то: дерево? если храним в дереве, то оператор в узле.

    def make_parts(self, ):
        # return ifфами или switchом рекурсивно вызывать - make_parts()
        # дифференцировать отдельные части - make_derivative()
        pass

    def make_derivative(self, part):
        pass


if __name__ == '__main__':
    a = Expression('x^2 + 2*x')
