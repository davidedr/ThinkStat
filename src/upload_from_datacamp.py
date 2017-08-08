'''
Created on 04 ago 2017

@author: davide
'''

filename = "iris_data_df.csv"
local_filename = '/tmp/'+filename
remote_filename = filename

df.to_csv(local_filename)

import ftplib
s = ftplib.FTP("ftp.pollisrl.it", "pollisrl.it", "GIO1301")

print(s.pwd())
s.cwd("/www/public")
print(s.pwd())
print(ftplib.FTP.dir(s))

f = open(local_filename, 'rb')

s.storbinary('STOR '+remote_filename, f)
f.close()
s.close()