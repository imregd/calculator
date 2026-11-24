from batch_calculator import process_calculation


def test_process_calculation():
	status, result, error_code = process_calculation("add", "2", "3")
	assert status == "OK"
	assert result == 5
	assert error_code == ""