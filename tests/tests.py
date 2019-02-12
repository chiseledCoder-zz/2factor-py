#from _2factor_wrapper import _2Factor
from _2factor_wrapper.Configure2Factor import Configure2Factor

import unittest

def verify_api():
	"""Test the api by verifying the API"""
	instance = _2Factor(api_key='293832-67745-11e5-88de-5600000c6b13')
	response = instance.verify()

	assert isinstance(response, dict)
	assert response['status'] == "True"


class Test2FactorConfiguration(unittest.TestCase):

	def test_set_api_key(self):
		self.assertEqual(Configure2Factor.set_api_key(api_key='1234'), '1234')
		self.assertNotEqual(Configure2Factor.set_api_key(api_key='1234'), '9090')

	def test_get_api_key_after_setting(self):
		self.assertIsNotNone(Configure2Factor.set_api_key(api_key='1234'))
		self.assertEqual(Configure2Factor.set_api_key(api_key='1234'), Configure2Factor.get_api_key())


if __name__ == '__main__':
	unittest.main()