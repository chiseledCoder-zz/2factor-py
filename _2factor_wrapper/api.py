import os
import requests


class _2Factor(object):

	def __init__(self, api_key=None, endpoint=None):
		self.api_key = api_key
		self.endpoint = endpoint

	def check_sms_otp_balance(self):
		response = call_api(method='get', )

	def request(self, method, data, **options):