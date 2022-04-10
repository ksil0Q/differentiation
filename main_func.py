import differentiate
arr = []


def diff(expression):
    if expression.operation == "+":
        left = Expression(expression.left)
        right = Expression(expression.right)
        arr.append(Functor(diff(left), "+", diff(right)).make_func())
        return Functor(diff(left), "+", diff(right))

    if expression.operation == "-":
        left = Expression(expression.left)
        right = Expression(expression.right)
        return Functor(diff(left), "-",  diff(right))

    if expression.operation == "*":
        left = Expression(expression.left)
        right = Expression(expression.right)
        left_diff = diff(left)
        right_diff = diff(right)
        return Functor(Functor(left, "*", right_diff),
                       "+",
                       Functor(left_diff, "*", right))

    # if expression.operation == "/":
    #     return Functor(
    #         Functor(
    #             Functor(diff(expression.left), expression.right, "*"),
    #             Functor(expression.right, expression.right, "*"), "/"),
    #         Functor(
    #             Functor(diff(expression.right), expression.left, "*"),
    #             Functor(expression.right, expression.right, "*"), "/"),
    #         "-")
    #
    if expression.right == "x":
        return Functor("", "", "1")
    #
    if expression.right == "2" or expression.right == "3":
        return Functor("", "", "0")

    # if expression.operation == "^":
    #     return Functor(expression.right,
    #                    Functor(
    #                        self.diff(expression.left),
    #                        expression.right - 1, "^"),
    #                    "*")
    #
    # if expression.operation == "cos":
    #     return Functor("-sin", self.diff(expression.right), "*")
    #
    # if expression.operation == "sin":
    #     return Functor("cos", self.diff(expression.right), "*")


class Expression:

    left = ''
    right = ''
    operation = ''

    def __init__(self, expr: str):
        self.left, self.right, self.operation = differentiate.parse_expr(expr)


class Functor:

    str_res = ''
    left = ''
    right = ''
    operation = ''

    def __init__(self, sub_func_left, operation, sub_func_right):
        self.left = sub_func_left
        self.right = sub_func_right
        self.operation = operation

    def make_func(self):
        return "{0}{1}{2}".format(self.left, self.operation, self.right)


if __name__ == '__main__':
    expr = Expression('2*x + 3')
    res = diff(expr)
    print(arr)


