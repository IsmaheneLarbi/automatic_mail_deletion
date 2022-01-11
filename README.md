# automatic_mail_deletion



Python script that deletes all emails with specified criteria.
- A specific sender email sent after a certain date

For this script to work, you have to :
1. Make sure imap is enabled in your provider, for google, the provider I'll be using, here's how to [enable imap](https://support.google.com/mail/answer/7126229?hl=en) if it isn't.
2. [Allow less secure apps] such as this one to be have access to your mail account. To do so, [generate a specific password for this app](https://myaccount.google.com/security). when asked for the name of the app, copy paste: automatic_mail_deletion


# To test if this works on gmail, write the following on the search bar:
in:inbox from:info@meetup.com after:01/04/2022
and watch them disappear!
in:{folder you chose to delete from} from:{email of the sender} after:{first date to start deleting from}
you can look up the gmail search operators [here.](https://support.google.com/mail/answer/7190?hl=en)
launch the script :
python automate_mail_deletion.py

Let's do this !
