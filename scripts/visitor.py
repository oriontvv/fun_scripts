from collections import namedtuple
import types


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


# class AbstractVisitor(metaclass=ABCMeta):

#     @abstractmethod
#     def visit(self, node):
#         return NotImplemented

#     @abstractmethod
#     def generic_visit(self, node):
#         return NotImplemented


class NodeVisitorRecursive():

    def visit(self, node):
        methodname = 'visit_' + type(node).__name__
        method = getattr(self, methodname, None)
        if method is None:
            method = self.generic_visit
        return method(node)

    def generic_visit(self, node):
        methodname = 'visit_' + type(node).__name__
        raise RuntimeError("Method {} not found".format(methodname))


class NodeVisitorYield():

    def visit(self, node):
        stack = [node]
        last_result = None

        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()

        return last_result

    def _visit(self, node):
        methodname = 'visit_' + type(node).__name__
        method = getattr(self, methodname, None)
        if method is None:
            method = self.generic_visit(node)
        return method(node)

    def generic_visit(self, node):
        methodname = 'visit_' + type(node).__name__
        raise RuntimeError('Method {} not found'.format(methodname))


class EvaluatorMixin:

    def visit_Number(self, node):
        return node.value

    def visit_Negate(self, node):
        return -self.visit(node.operand)

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)


class EvaluatorRecursive(NodeVisitorRecursive, EvaluatorMixin):
    pass


class EvaluatorYield(NodeVisitorYield, EvaluatorMixin):
    pass


Instruction = namedtuple('Instruction', ['name', 'value'])


class StackCodeGeneratorMixin:

    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def visit_unary(self, node):
        self.visit(node.operand)
        self.instructions.append(Instruction('NEG', None))

    def visit_binary(self, node, instruction_name):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append(Instruction(instruction_name, None))

    def visit_Number(self, node):
        return self.instructions.append(Instruction('PUSH', node.value))

    def visit_Negate(self, node):
        return -self.visit(node.operand)

    def visit_Add(self, node):
        return self.visit_binary(node, 'ADD')

    def visit_Sub(self, node):
        return self.visit_binary(node, 'SUB')

    def visit_Mul(self, node):
        return self.visit_binary(node, 'MUL')

    def visit_Div(self, node):
        return self.visit_binary(node, 'DIV')


class StackCodeGeneratorRecursive(NodeVisitorRecursive,
                                  StackCodeGeneratorMixin):
    pass


class StackCodeGeneratorYield(NodeVisitorYield,
                              StackCodeGeneratorMixin):
    pass
