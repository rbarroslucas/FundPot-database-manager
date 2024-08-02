from gspread_pandas import Client
from google.oauth2.service_account import Credentials

class GoogleClient:
    def __init__(self, cred_keys, scopes):
        """
        Initializes the GoogleClient with the provided credentials and scopes.

        :param cred_keys: Dictionary containing the Google service account credentials.
        :type cred_keys: dict
        :param scopes: List of scopes for the Google API.
        :type scopes: list
        """
        self.creds = Credentials.from_service_account_info(
            info=cred_keys,
            scopes=scopes
        )
        self.client = Client(
            scope=scopes,
            creds=self.creds
        )
