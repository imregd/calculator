from calculator import add, subtract, multiply, divide, CircleArea

from batch_calculator import process_calculation

def test_add():
	assert add(2,3) == 5

def test_divide():
	assert divide(6,2) == 3

def test_subtract():
	assert subtract(6,2) == 4

def test_multiply():
	assert multiply(6,2) == 12

def test_multiply_zero():
	# Arrange
	a, b = 5, 0
	#Act
	result = multiply(a,b)
	#assert
	assert result == 0

def test_circleArea():
	assert CircleArea(-4) == "Error"


def test_process_calculation():
	status, result, error_code = process_calculation("add", "2", "3")
	assert status == "OK"
	assert result == 5
	assert error_code == ""