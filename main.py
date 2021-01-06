import imaplib
import email


host = 'imap.gmail.com'
username = 'onietest1@gmail.com'
password = 'P@$$w0rd#onietest'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select('inbox')

_, search_data = mail.search(None, 'UNSEEN')
for num in search_data[0].split():
    _, data = mail.fetch(num, 'RFC822')
    _, b = data[0]
    email_msg = email.message_from_bytes(b)

    # for header in ['subject', 'to', 'from', 'date']:
    #     print('{}: {}'.format(header, email_msg[header]))
    print('SUBJECT:', email_msg['subject'])
    print('FROM:', email_msg['from'])
    print('DATE:', email_msg['date'])

    for part in email_msg.walk():
        if part.get_content_type() == 'text/plain':
            body_text = part.get_payload(decode=True)
            print(body_text.decode())
        # elif part.get_content_type() == 'text/html':
        #     body_html = part.get_payload(decode=True)
        #     print(body_html.decode())

