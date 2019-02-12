class Configure2Factor(object):
    """ This module configures the environment and setup required for 2Factor.in """

    api_key = None  # Static variable

    @staticmethod
    def get_api_key():
        assert  Configure2Factor.api_key is not None, "API Key should not be Null"
        return str(Configure2Factor.api_key)

    @staticmethod
    def set_api_key(api_key):
        Configure2Factor.api_key = api_key
        return str(Configure2Factor.api_key)
