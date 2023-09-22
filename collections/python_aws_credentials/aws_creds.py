import os
from configparser import ConfigParser

current_user = os.getenv("USER")
CRED_FILE_PATH = f"{os.path.expanduser('~')}/.aws/credentials"


def load_creds_file(file_path):
    config_data = {}
    aws_config = ConfigParser()
    aws_config.read(file_path)
    for section in aws_config.sections():
        section_data = aws_config[section]
        access_key = section_data["aws_access_key_id"]
        secret_key = section_data["aws_secret_access_key"]
        session_token = aws_config[section]["aws_session_token"]
        config_data[section] = {
            "access_key": access_key,
            "secret_key": secret_key,
            "session_token": session_token
        }
    return config_data


if __name__ == '__main__':
    results = load_creds_file(CRED_FILE_PATH)
    print(results)

