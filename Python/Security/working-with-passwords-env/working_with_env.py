
from dotenv import load_dotenv # pip install python-dotenv
import os

# Load environment variables from the .env file into the environment
load_dotenv()

# Retrieve the values of the environment variables from the .env file
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
tenant_id = os.getenv('TENANT_ID')
scope = os.getenv('SCOPE')
token_url = os.getenv('TOKEN_URL')


print(f"Client ID: {client_id}")
print(f"Client Secret: {client_secret}")
print(f"Tenant ID: {tenant_id}")
print(f"Scope: {scope}")
print(f"Token URL: {token_url}")


if client_id and client_secret and tenant_id and scope and token_url:
    print("All variables were correctly captured.")
else:
    print("Some variables are missing.")
