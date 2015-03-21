#!/usr/local/bin/python
import hashlib
import urllib2
import urllib
import time
import webbrowser
import time

# Variables
website = 'http://tim.stagecraft.net/neccdc/tmp/team_services.gif'
#website = ''

def getSource(web):
	response = urllib2.urlopen(web)
	html = response.read()
	return html

def compare(new_digest, old_digest):
	if old_digest == 1:
		old_digest = new_digest

	while True:
		new_digest = hashlib.md5(getSource(website)).hexdigest()
		if new_digest != old_digest:
			old_digest = new_digest
			new_digest = hashlib.md5(getSource(website)).hexdigest()
			#webbrowser.open_new(website)

			timez = time.strftime("%H:%M")
			req = urllib2.Request("http://tim.stagecraft.net/neccdc/tmp/team_services.gif")
			response = urllib2.urlopen(req)
			with open('sat_service_' + timez + '.gif','wb') as fo:
				fo.write(response.read())

			print "Change @ " + timez
			time.sleep(30)
		else:
			#new_digest = hashlib.md5(getSource(website)).hexdigest()
			timez = time.strftime("%H:%M")
			print "No change @ " + timez
			time.sleep(30)

def main():
	old_digest = 1

	timez = time.strftime("%H:%M")
	req = urllib2.Request("http://tim.stagecraft.net/neccdc/tmp/team_services.gif")
	response = urllib2.urlopen(req)

	with open('sat_service_' + timez + '.gif','wb') as fo:
		fo.write(response.read())

	new_digest = hashlib.md5(getSource(website)).hexdigest()
	change = compare(new_digest, old_digest)



main()
