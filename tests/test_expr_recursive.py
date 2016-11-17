import pytest
from scripts.expr_recursive import *


@pytest.fixture()
def expr():
	# 1 + 2 * (3 - 4) / 5
	t1 = Sub(Number(3), Number(4))
	t2 = Mul(Number(2), t1)
	t3 = Div(t2, Number(5))
	t4 = Add(Number(1), t3)
	return t4


def test_evaluator(expr):
	e = Evaluator()
	assert (1 + 2 * (3 - 4) / 5) == e.visit(expr)


def test_code_generator(expr):
	generator = StackCode()
	code = generator.generate_code(expr)

	assert code == [
		Instruction('PUSH', 1),
		Instruction('PUSH', 2),
		Instruction('PUSH', 3),
		Instruction('PUSH', 4),
		Instruction('SUB', None),
		Instruction('MUL', None),
		Instruction('PUSH', 5),
		Instruction('DIV', None),
		Instruction('ADD', None),
	]


