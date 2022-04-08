class Main:

    inp = 'x*3 + const'

    def __init__(self, expr: str):
        self.inp = expr
        self.parse_expr(expr)

    def parse_expr(self, ex):
        inp = ex.split("+")
        exp = Functor(inp[0], inp[1], "+")
        self.diff(exp)

    def diff(self, expression):
        if expression.operation == "+":
            return Functor(self.diff(expression.left),
                           self.diff(expression.right), "+")

        if expression.operation == "+":
            return Functor(self.diff(expression.left),
                           self.diff(expression.right), "-")

        if expression.operation == "*":
            return Functor(Functor(self.diff(expression.left),
                                   expression.right, "*"),
                           Functor(expression.left,
                           self.diff(expression.right), "*"), "+")

        if expression.operation == "/":
            return Functor(
                Functor(
                    Functor(self.diff(expression.left), expression.right, "*"),
                    Functor(expression.right, expression.right, "*"), "/"),
                Functor(
                    Functor(self.diff(expression.right), expression.left, "*"),
                    Functor(expression.right, expression.right, "*"), "/"),
                "-")

        if expression.operation == "^":
            return Functor(expression.right,
                           Functor(
                               self.diff(expression.left),
                               expression.right - 1, "^"),
                           "*")

        if expression.operation == "cos":
            return Functor("-sin", self.diff(expression.right), "*")

        if expression.operation == "sin":
            return Functor("cos", self.diff(expression.right), "*")

        if expression.operation == "x":
            return Functor("1", "", "")

        if expression.operation == "const":
            return Functor("0", "", "")

    def make_derivative(self, part):
        pass


class Functor:

    right = ""
    left = ""
    operation = ""

    def __init__(self, sub_expr_left, sub_expr_right, operation):
        self.right = sub_expr_right
        self.left = sub_expr_left
        self.operation = operation

    def make_func(self):
        return "{0}{1}{2}".format(self.left, self.operation, self.right)
    print(right,left,operation)

