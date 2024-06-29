import jwt
import os
import requests
import uuid
from dotenv import load_dotenv

load_dotenv()
access_key = os.getenv('UPBIT_OPEN_API_ACCESS_KEY')
secret_key = os.getenv('UPBIT_OPEN_API_SECRET_KEY')
if not access_key or not secret_key:
    raise ValueError('API key and secret key are not found.')

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)

url = 'https://api.upbit.com/v1/accounts'

headers = {
  'Authorization': authorization,
}

res = requests.get(url, headers=headers)

print(res.json())