# import os
# import base64
# from email.message import EmailMessage

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build

# SCOPES = ['https://www.googleapis.com/auth/gmail.send']


# def gmail_authenticate():
#     creds = None

#     if os.path.exists("token.json"):
#         creds = Credentials.from_authorized_user_file(
#             "token.json",
#             SCOPES
#         )

#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())

#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 "credentials.json",
#                 SCOPES
#             )

#             creds = flow.run_local_server(port=0)

#         with open("token.json", "w") as token:
#             token.write(creds.to_json())

#     service = build("gmail", "v1", credentials=creds)

#     return service


# def send_email():
#     service = gmail_authenticate()

#     message = EmailMessage()

#     # message.set_content(
#     #     "Hello!\n\nThis is an automated email from Python."
#     # )
#     designation = "Python Developer"

#     message.set_content(f"""
#     Dear Hiring Manager,

#     I hope you are doing well.

#     I am writing to express my interest in the {designation} position.

#     I have experience in:
#     - Python Development
#     - AI Engineering
#     - Web Development
#     - API Integration
#     - Automation Projects

#     I am attaching my CV for your consideration.

#     I would welcome the opportunity to discuss how my skills and experience can contribute to your team.

#     Thank you for your time and consideration.

#     Best Regards,
#     Sehrish Shafiq
#     LinkedIn:
#     https://www.linkedin.com/in/sehrish-shafiq
#     """)

#     message["To"] = "sehr.shafiq345@gmail.com"
#     message["From"] = "me"
#     message["Subject"] = f"Application for {designation}"

#     with open("Sehrish_Shafiq_CV.pdf", "rb") as f:
#         file_data = f.read()

#     message.add_attachment(
#         file_data,
#         maintype="application",
#         subtype="pdf",
#         filename="Sehrish_Shafiq_CV.pdf"
#     )

#     encoded_message = base64.urlsafe_b64encode(
#         message.as_bytes()
#     ).decode()

#     create_message = {
#         'raw': encoded_message
#     }

#     send_message = service.users().messages().send(
#         userId="me",
#         body=create_message
#     ).execute()

#     print("Email Sent Successfully!")
#     print("Message Id:", send_message['id'])


# if __name__ == "__main__":
#     send_email()

import os
import base64
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def gmail_authenticate():
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


def send_email(to_email, designation, cv_path):
    service = gmail_authenticate()

    message = EmailMessage()

    message.set_content(f"""
Dear Hiring Manager,

I am applying for the {designation} position.

Please find my CV attached.

Best Regards,
Sehrish Shafiq
LinkedIn: https://www.linkedin.com/in/sehrish-shafiq
""")

    message["To"] = to_email
    message["From"] = "me"
    message["Subject"] = f"Application for {designation}"

    # Attach CV
    with open(cv_path, "rb") as f:
        file_data = f.read()

    message.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename="CV.pdf"
    )

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    service.users().messages().send(
        userId="me",
        body={"raw": encoded_message}
    ).execute()

    return "Email Sent Successfully!"