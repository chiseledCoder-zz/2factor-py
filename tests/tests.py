from _2factor_wrapper import _2Factor


def verify_api():
	"""Test the api by verifying the API"""
	instance = _2Factor(api_key='293832-67745-11e5-88de-5600000c6b13')
	response = instance.verify()

	assert isinstance(response, dict)
	assert response['status'] == "True"
