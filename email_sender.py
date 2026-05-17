import os
import base64
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def gmail_auth():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def send_email(to_email, subject, body, cv_path):
    service = gmail_auth()

    message = EmailMessage()
    message.set_content(body)

    message["To"] = to_email
    message["From"] = "me"
    message["Subject"] = subject

    # Attach CV
    with open(cv_path, "rb") as f:
        file_data = f.read()

    message.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename="CV.pdf"
    )

    encoded = base64.urlsafe_b64encode(message.as_bytes()).decode()

    service.users().messages().send(
        userId="me",
        body={"raw": encoded}
    ).execute()

    return "Email Sent Successfully!"