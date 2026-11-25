from batch_calculator import process_calculation


def test_process_calculation():
	status, result, error_code = process_calculation("add", "2", "3")
	assert status == "OK"
	assert result == 5
	assert error_code == ""

def test_subtract():
	status, result, error_code = process_calculation("subtract", "10", "4")
	assert status == "OK"
	assert result == 6
	assert error_code == ""


def test_add():
	status, result, error_code = process_calculation("add", "10", "4")
	assert status == "OK"
	assert result == 14
	assert error_code == ""


def test_multiply():
	status, result, error_code = process_calculation("multiply", "10", "4")
	assert status == "OK"
	assert result == 40
	assert error_code == ""


def test_divide():
	status, result, error_code = process_calculation("divide", "10", "4")
	assert status == "OK"
	assert result == 2.5
	assert error_code == ""


def test_subtract_negative():
	status, result, error_code = process_calculation("subtract", "-10", "4")
	assert status == "OK"
	assert result == -14
	assert error_code == ""

def test_add_negative():
	status, result, error_code = process_calculation("add", "-5", "4")
	assert status == "OK"
	assert result == -1
	assert error_code == ""


def test_multiply_negative():
	status, result, error_code = process_calculation("multiply", "-3", "4")
	assert status == "OK"
	assert result == -12
	assert error_code == ""

def test_divide_negative():
	status, result, error_code = process_calculation("divide", "10", "-2")
	assert status == "OK"
	assert result == -5
	assert error_code == ""

def test_divide_zero_invalid():
	status, result, error_code = process_calculation("divide", "10", "0")
	assert status == "ERROR"
	assert result == ""
	assert error_code == "DIVISION_BY_ZERO"

def test_divide_zero():
	status, result, error_code = process_calculation("divide", "0", "5")
	assert status == "OK"
	assert result == 0
	assert error_code == ""

def test_invalid_operation():
	status, result, error_code = process_calculation("quantuple quadrant or something", "5", "5")
	assert status == "ERROR"
	assert result == ""
	assert error_code == "UNKNOWN_OPERATION"

def test_multiply_whitespace():
	status, result, error_code = process_calculation("  multiply      ", "5", "5")
	assert status == "OK"
	assert result == 25
	assert error_code == ""


def test_invalid_number():
	status, result, error_code = process_calculation("multiply", "five", "5")
	assert status == "ERROR"
	assert result == ""
	assert error_code == "INVALID_NUMBER"

def test_error_priority():
	status, result, error_code = process_calculation("multiplicationstility", "five", "5")
	assert status == "ERROR"
	assert result == ""
	assert error_code == "UNKNOWN_OPERATION"


def test_add_decimal():
	status, result, error_code = process_calculation("add", "5.2", "4.5")
	assert status == "OK"
	assert result == 9.7
	assert error_code == ""

def test_subtract_decimal():
	status, result, error_code = process_calculation("subtract", "5.5", "4.5")
	assert status == "OK"
	assert result == 1.0
	assert error_code == ""

def test_multiply_decimal():
	status, result, error_code = process_calculation("multiply", "5.5", "2")
	assert status == "OK"
	assert result == 11
	assert error_code == ""

def test_divide_decimal():
	status, result, error_code = process_calculation("divide", "14.4", "2")
	assert status == "OK"
	assert result == 7.2
	assert error_code == ""




