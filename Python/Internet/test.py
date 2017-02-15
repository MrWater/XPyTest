import smtplib
from smtplib import SMTP
import email.message
from email.message import Message
import imaplib
from imaplib import IMAP4_SSL


fromAddress = "1733301206@qq.com"
toAddress = "1733301206@qq.com"
msg = Message()
msg["From"] = "wx@python.test.com"
msg["To"] = toAddress
msg["Subject"] = "Python Test"
msg.set_payload("This is a python test\nset_payload")

server = SMTP("smtp.qq.com", 587)
server.starttls()
server.login("1733301206@qq.com", "rcoezbcccaypcihg")
server.sendmail(fromAddress, toAddress, str(msg)) # from_addr和smtp的账号一致
server.quit()
server.close()

# print(str(msg))

try:
		print(0)
		client = IMAP4_SSL("imap.qq.com", 993)
		print(2)
		client.login("1733301206@qq.com", "rcoezbcccaypcihg")
		print(3)
		client.select("INBOX")
		print(4)
		type, data = client.select("INBOX")
		msgList = data[0].split()
		type, data = client.fetch(msgList[len(msgList)-1], "(RFC822)")
		msg = email.message_from_bytes(data[0][1])
		print(msg.get_payload(decode=True))
		# client.logout()
		# client.close()
except Exception as e:
	print("FDSF")
	raise e	
