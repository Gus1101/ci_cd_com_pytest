import pytest
from functions.sum import sum

@pytest.mark.unit
def test_sum():

	"""
	Functions that tests sum function from module functions
	"""

	a = 10
	b = 20

	assert sum(a,b) == 30
