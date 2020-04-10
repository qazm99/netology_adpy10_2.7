import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.MIMEText import MIMEText
# from email.MIMEMultipart import MIMEMultipart


class EmailSession:
    def __init__(self, login_email, password_email):
        self.connect = {'login': login_email, 'password': password_email}

    def send_mail(self, server_smtp, port, subject, recipients, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.connect['login']
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            msg.attach(MIMEText(message))
            ms = smtplib.SMTP(server_smtp, port)
            # identify ourselves to smtp gmail client
            ms.ehlo()
            # secure our email with tls encryption
            ms.starttls()
            # re-identify ourselves as an encrypted connection
            ms.ehlo()
            ms.login(self.connect['login'], self.connect['password'])
            ms.sendmail(self.connect['login'], ms, msg.as_string())
            ms.quit()

        except Exception as e:
            print(f'send mail is fail:{e}')

    def receive_mail(self, server_imap, box_mail, header_mail=None):
        mail = imaplib.IMAP4_SSL(server_imap)
        try:
            mail.login(self.connect['login'], self.connect['password'])
            mail.list()
            mail.select(box_mail)
            criterion = '(HEADER Subject "%s")' % header_mail if header_mail else 'ALL'
            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_result_receive = email.message_from_string(raw_email)
            mail.logout()
            return email_result_receive
        except Exception as e:
            print(f'receive mail is fail:{e}')
        return False


if __name__ == '__main__':
    gmail_session = EmailSession('login@gmail.com', 'qwerty')

    gmail_session.send_mail('smtp.gmail.com', 587, 'Subject',
                            ['vasya@email.com', 'petya@email.com'], 'Message')

    email_message = gmail_session.receive_mail('imap.gmail.com', 'inbox')









