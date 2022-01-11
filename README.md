# automatic_mail_deletion


## Description :
Python script that deletes all emails with specified criteria.
- A specific sender email sent after a certain date

## Requirements :
For this script to work, you have to :
1. Make sure imap is enabled in your account settings. For google, the provider I'll be using, here's how to [enable imap](https://support.google.com/mail/answer/7126229?hl=en) if it isn't.
2. Allow less secure apps such as this one to be have access to your mail account. To do so, [generate a specific password for this app](https://myaccount.google.com/security). when asked for the name of the app, copy paste: automatic_mail_deletion


## Test :
- To test if this works on gmail, write the following on the search bar:
`in:{folder you chose to delete from} from:{email of the sender} after:{first date to start deleting from}`
- example:
`in:inbox from:info@meetup.com after:01/04/2022`
- launch the script :
python automate_mail_deletion.py

## Further use :
- If you want to change the folder you're selecting:
`imap.select('"folder of your choice"')`
- You can list all the folders using  `imap.list()` before the select
- If you want to change the criteria, change the second parameter of this instruction:
`imap.search(None, "FROM 'info@meetup.com' SINCE '02-Jan-2022'")`
- You can look up the criteria on the [imap library manual](https://docs.python.org/3/library/imaplib.html)
- You can look up the gmail search operators [here.](https://support.google.com/mail/answer/7190?hl=en)


Let's do this !
