#-*-coding:utf8-*-

import urllib2

url = ""
res = urllib2.urlopen("http://103.235.253.172:8666/data/mi/info_artist/2018091814_artist/artist_full_2018091814_110.json")
print(res.read())