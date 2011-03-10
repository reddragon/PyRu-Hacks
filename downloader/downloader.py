# I saw the long list of pdfs that I had to download to
# get the Advanced Linux Programming book. So I decided
# to write a Python script.

# Released under GNU GPL v3
# http://www.gnu.org/licenses/gpl.html

# Author: Gaurav Menghani
# Date: 10th March, 2011

import urllib
import urllib2
import sys
import re

def download_file(url, local_addr):
    web_file = urllib.urlopen(url)
    local_file = open(local_addr, 'w')
    local_file.write(web_file.read())
    web_file.close()
    local_file.close()

# Change this URI 
fetching_uri = "http://www.advancedlinuxprogramming.com/alp-folder"
request = urllib2.Request(fetching_uri)
response = urllib2.urlopen(request)
response_str = response.read()

# Might need to heavily customize this regex
pdf_link_pattern = re.compile(r'<a href=".*">pdf</a>')
links = pdf_link_pattern.findall(response_str)
for link in links:
   start_i = link.find('href="')
   end_i = link.find('">')
   file_name = link[start_i + 6 : end_i]
   print "Downloading " + file_name + " now "
   download_file(fetching_uri + "/" + file_name, file_name)
   print "Downloaded " + file_name


