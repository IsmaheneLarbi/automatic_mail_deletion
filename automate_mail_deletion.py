import imaplib

provider = "gmail"
username = f"youraddress@{provider}.com"
password = "your password"
imap = imaplib.IMAP4_SSL(f"imap.{provider}.com")
imap.login(username, password)
imap.select('"INBOX"')
imap.search(None, "FROM 'info@meetup.com' SINCE '02-Jan-2022'")
mails = mails[0].split(b' ')
for mail in mails:
    imap.store(mail, '+FLAGS', '\\Deleted')
imap.expunge()
imap.close()
imap.logout()
