from example.auth.transport.requests import Request
from example.oauth2.credentials import Credentials

# Assuming you have a token.json file with your credentials
import json

with open('token.json', 'r') as token_file:
    token_info = json.load(token_file)

# Load credentials from the token info
creds = Credentials.from_authorized_user_info(token_info)

# Check if the credentials need to be refreshed
if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())

# Now you can use creds to access example APIs
# For example, to list files in example Drive:
from googleapiclient.discovery import build

service = build('drive', 'v3', credentials=creds)
results = service.files().list(pageSize=10).execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(f"{item['name']} ({item['id']})")

# Optionally, save the refreshed credentials back to the token file
with open('token.json', 'w') as token_file:
    token_file.write(creds.to_json())
