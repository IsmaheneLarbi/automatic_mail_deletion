import imaplib


from datetime import datetime, timedelta

provider = "gmail"
username = f"yourusername@{provider}.com"
password = "your password for this app"
imap = imaplib.IMAP4_SSL(f"imap.{provider}.com")
imap.login(username, password)
imap.select('"INBOX"')
today = datetime.today()
yesterday = today - timedelta(days=1)
yesterday = yesterday.strftime("%d-%b-%Y")
status, mails = imap.search(None, f'FROM "info@meetup.com" SINCE "{yesterday}"')
mails = mails[0].split(b' ')
for mail in mails:
    imap.store(mail, '+FLAGS', '\\Deleted')
imap.expunge()
imap.close()
imap.logout()
