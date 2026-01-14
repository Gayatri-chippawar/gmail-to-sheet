Gmail to Google Sheets Automation
📌 Overview

This project is a Python automation script that reads unread emails from a Gmail inbox and logs them into a Google Sheet using Google APIs.

Each email is added as a new row containing sender, subject, date, and plain-text content.
The system prevents duplicates and marks emails as read after processing.

🎯 Objective

Log each unread Gmail message into Google Sheets with the following fields:

Column	Description
From	Sender email address
Subject	Email subject
Date	Date & time received
Content	Email body (plain text)
🏗️ Architecture
Gmail (Unread)
     ↓
Python Script (OAuth + Parsing + Deduplication)
     ↓
Google Sheets (Append Rows)

📂 Project Structure
gmail-to-sheets/
├── src/
│   ├── gmail_service.py
│   ├── sheets_service.py
│   ├── email_parser.py
│   ├── state_manager.py
│   ├── config.py
│   └── main.py
├── credentials/credentials.json
├── state.json
├── token.json
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Setup & Run

Create virtual environment and install dependencies:

pip install -r requirements.txt


Enable Gmail API and Google Sheets API in Google Cloud.

Create OAuth Client ID (Desktop App) and place:

credentials/credentials.json


Create a Google Sheet with headers:

From | Subject | Date | Content


Add Spreadsheet ID to config.py.

Run the script:

python src/main.py

🔐 OAuth Flow

OAuth 2.0 Desktop authentication is used.
On first run, the user grants Gmail and Sheets access.
OAuth token is stored locally and reused on subsequent runs.

🔁 Duplicate Prevention & State

Processed Gmail message IDs are stored in state.json.
Before processing, the script checks this state to avoid duplicate entries.

📬 Mark as Read

After successful logging to Google Sheets, emails are marked as read by removing the UNREAD label.

⚠️ Challenge Faced

OAuth scope errors occurred when adding Google Sheets access after initial authentication.
Resolved by deleting the old token and re-authenticating with combined scopes.

🚧 Limitations

Only unread inbox emails are processed

Plain text content only

State stored locally

👩‍💻 Author

Gayatri Chippawar