import differentiate


def diff(expression):
    if expression.operation == "+":
        left = Expression(expression.left)
        right = Expression(expression.right)
        return diff(left), "+", diff(right)

    if expression.operation == "-":
        left = Expression(expression.left)
        right = Expression(expression.right)
        return diff(left), "-", diff(right)

    if expression.operation == "*":
        left = Expression(expression.left)
        right = Expression(expression.right)
        return tuple(
            left, "*" , diff(Expression(expression.right)) , " +",
            diff(Expression(expression.left)), "*", right
        )

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
        return Expression("", "", "1")
    #
    if expression.right == "2" or expression.right == "3":
        return Expression("", "", "0")

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

    def __init__(self, expr : str):
        self.left, self.operation, self.right = differentiate.parse_expr(expr)

    def prnt(self):
        print(self.left, self.operation, self.right)


if __name__ == '__main__':
    expr = Expression('2*x + 3')
    res = diff(expr)
    print()


