import csv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from typing import List

from dotenv import load_dotenv

load_dotenv()


def get_users_data() -> List[tuple[str, str]]:
    users_data = []
    with open("./data_contacts.csv") as raw_file:
        database = csv.reader(raw_file)

        for row in database:
            users_data.append(row)
    return users_data


class Email:
    def __init__(self, receiver_name: str, receiver_email: str, receiver_attach: str):
        self.receiver_name = receiver_name
        self.receiver_email = receiver_email
        
        #NOTE: If doesn't have attachments to send, please remove the lines related
        self.receiver_attach = receiver_attach

    def get_message(self, person_name: str):
        return MIMEText(
            f"""
<p>Hello, {person_name}! This message must be replaced.</p>
        """,
            "html",
        )

    def get_email(self):
        message = MIMEMultipart()

        sender = os.getenv("NAME") + "<"+os.getenv("EMAIL")+">"
        message["From"] = sender
        message["To"] = self.receiver_email
        # TODO: replace the email subject here!
        message["Subject"] = "Example Subject"
        message.attach(self.get_message(self.receiver_name))

        #NOTE: attachment will be iterable, so rename it from 1 to the n number
        file_path = f'attachs/{self.receiver_attach}.jpg'
        attachment = open(file_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % 'certificado.jpg')
        message.attach(part)

        return message


class EmailSender:
    def __init__(self, users_data: List[tuple[str, str]]) -> None:
        self.user_data = users_data
        self.sender = self._get_email_sender()

    def _get_email_sender(self):
        try:
            sender = smtplib.SMTP(host="smtp.gmail.com", port=587)
            sender.starttls()
            name, password = os.getenv("EMAIL"), os.getenv("PASSWORD")
            sender.login(name, password)
            return sender
        except smtplib.SMTPAuthenticationError as e:
            print(e)
            print("Seu e-mail e senha podem estar errados")
            exit(1)

    def send_emails(self):
        for index, (name, email) in enumerate(self.user_data):
            raw_email_content = Email(name, email, index+1)
            encoded_email = raw_email_content.get_email()
            self.sender.send_message(encoded_email)
            print(f'Sent e-mail to... {name}')


def main():
    users_data = get_users_data()
    email_sender = EmailSender(users_data)
    email_sender.send_emails()


if __name__ == "__main__":
    main()
