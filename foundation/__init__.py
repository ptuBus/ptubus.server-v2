import os


def get_api_key():
    api_key = os.getenv("ODSAY_API_KEY")
    try:
        return api_key
    except ValueError:
        raise ValueError("Did you enter API KEY at '.env file'?")
