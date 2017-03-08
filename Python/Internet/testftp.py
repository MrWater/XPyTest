# !/user/bin/env python

import ftplib


with ftplib.FTP('localhost') as f:
	f.login('wx', '1aA')

	file = 'test.txt'
	f.retrbinary('RETR %s' % file, open('C:\\Users\\WX\\Desktop\\%s' % file, 'wb').write)

	fs = open(r'C:\Users\WX\Desktop\test.py', 'rb')
	f.storbinary('STOR test.py', fs, 1024)
	fs.close()

	f.quit()