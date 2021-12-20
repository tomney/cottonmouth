import os
from google.oauth2 import service_account

CREDENTIAL_PATH="creds/bolg-229922-eea9f44a1422.json"



def get_credentials():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cred_path = os.path.join(dir_path, CREDENTIAL_PATH)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path
    credentials = service_account.Credentials.from_service_account_file(cred_path)
    return credentials

creds = get_credentials()