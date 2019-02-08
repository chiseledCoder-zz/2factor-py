class 2FactorConfig(object):
	def __init__(self, api_key):
		self.api_key = api_key

	def get_api_key():
		return self.api_key

	def set_api_key(api_key):
		self.api_key = api_key
		assert self.api_key!=None
		return str(self.api_key) + " set successfully as API Key"