import datetime
import urllib.request

#get timestamp
today = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

#get ip
with urllib.request.urlopen('https://api.ipify.org') as response:
   ip = response.read()
   
#write info to logfile
file_object = open('iplog.txt', 'a')
# Append 'ip' at the end of file
file_object.write(today + ' My external IP is:  ' + str(ip) + "\n")
# Close the file
file_object.close()
