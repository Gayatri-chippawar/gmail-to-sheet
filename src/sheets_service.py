from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import pickle
import os

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_sheets_service():
    if not os.path.exists('token.json'):
        raise Exception("token.json not found. Run Gmail auth first.")

    with open('token.json', 'rb') as token:
        creds = pickle.load(token)

    return build('sheets', 'v4', credentials=creds)


def append_row(spreadsheet_id, values):
    service = get_sheets_service()

    body = {
        'values': [values]
    }

    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range='Sheet1!A:D',
        valueInputOption='RAW',
        insertDataOption='INSERT_ROWS',
        body=body
    ).execute()
