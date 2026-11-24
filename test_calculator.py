from calculator import add, subtract, multiply, divide, CircleArea


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


