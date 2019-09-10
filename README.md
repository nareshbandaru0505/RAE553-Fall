###################### Downloading html file #########################################

# importing FTP class from ftplib module
from ftplib import FTP

# connect the destination ftp server according to given instructions
ftp = FTP('ftp.lt.debian.org')

# login in connected ftp server with anonymous user name and password
ftp.login(); 

# retrlines display the files in current directory
ftp.retrlines('LIST')

# change the directory to debian
ftp.cwd('debian')

#define download with exact location in local file system and its location
download = '/Users/naresh0505/Downloads/Download_html.html'

# open the file download with writting in binary mode as name file
#retrive the file as binary code and file name in ftp server is README.html
with open(download, 'wb') as file:
 ftp.retrbinary('RETR ' + 'README.html', file.write)
 

#verify the file by "cat /Users/naresh0505/Downloads/Download_html.html"


###################### Downloading text file #########################################

# importing FTP class from ftplib module
from ftplib import FTP

# connect the destination ftp server according to given instructions
ftp = FTP('ftp.lt.debian.org')

# login in connected ftp server with anonymous user name and password
ftp.login(); 

# retrlines display the files in current directory
ftp.retrlines('LIST')

# change the directory to debian
ftp.cwd('debian')

#define download.txt with exact location in local file system and its location
download_text = '/Users/naresh0505/Downloads/Download.txt'

# open the file download_text.txt with writting in text mode as name file
#retrive the file as binary code and file name in ftp server is README.mirrors.txt
with open(download_text, 'w') as f:
  ftp.retrlines('RETR ' + 'README.mirrors.txt', f.write)


############### Replacing the html codes ##########################

sed 's/<[^>]*>//g' Download_html.html > README2.txt

#though i can replace all the html tags by sed 's/<test>//g', prepared to do it by taken help from google
#here is the explainations about it.
# [^>] is a regex which display everything expect >
# * indicates that zero or more repeatations
#together, [^>]* displays all the characters doesnt match >
#by placing search option as <[^>]*>, we filter all the words which starts with <, infinite number of words in between and ends with >
# as format of search and replace a word globally, i have used sed as sed 's/searchword/replaceword/g'
#write in to another file called README2.txt


################# uploading README2.txt to FTPSERVER ###################
# importing FTP class from ftplib module
from ftplib import FTP

# connect the destination ftp server according to given instructions
ftp = FTP('ftp.lt.debian.org')

# login in connected ftp server with anonymous user name and password
ftp.login(); 

# retrlines display the files in current directory
ftp.retrlines('LIST')

# change the directory to debian
ftp.cwd('debian')

#define upload with exact location in local file system and its location
upload = '/Users/naresh0505/Downloads/README2.txt'

# copy the file README2.txt with writting in text mode as name file
#retrive the file as binary code and file name in ftp server is README.mirrors.txt
with open(upload, 'r') as f:
 ftp.storlines("STOR " + 'upload', f) 
 
 
 
