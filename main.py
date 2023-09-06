import imaplib
import email
from email.header import decode_header
import bleach
from bs4 import BeautifulSoup
import re


mail_pass = "Den-4242"
username = "mail@z3x.ru"
imap_server = "imap.beget.com"

imap = imaplib.IMAP4_SSL(imap_server,993)
imap.login(username, mail_pass)
imap.select("INBOX")
#allm = imap.search(None, 'ALL')

m = imap.uid('search', "UNSEEN", "ALL")
#res, msg = imap.uid('fetch', b'28', '(RFC822)') 


result, data = imap.search(None, "ALL")

ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

result, data = imap.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]
raw_email_string = raw_email.decode('utf-8')


email_message = email.message_from_string(raw_email_string)
 
# print(email_message['To'])
# print(email.utils.parseaddr(email_message['From']))
# print(email_message['Date'])
# print(email_message['Subject'])
# print(email_message['Message-Id'])

email_message = email.message_from_string(raw_email_string)
 
if email_message.is_multipart():
    for payload in email_message.get_payload():
        body = payload.get_payload(decode=True).decode('utf-8')
        print("-------------------------------------")
        print(bleach.clean(body, tags=[], strip=True))
else:    
    body = email_message.get_payload(decode=True).decode('utf-8')
    #print(body)
    print(bleach.clean(body, tags=[], strip=True))
