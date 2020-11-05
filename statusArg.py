import requests
import socket
import string
import os
import colour as cms
import delete

def control_status(r,url):	#funzione per descrizione dettagliata degli status
	print ('Url required:'), url
	print ('Status:'),r.status_code
	if (r.status_code >= 200) and (r.status_code <300):
		print 'Description: Succesful site response.',    #descrizione dello stato
		if r.status_code == 200:
			print 'OK'
			print '--------------------------------------------------','\n'
		elif r.status_code == 201:
			print 'Created'
			print '--------------------------------------------------','\n'
		elif r.status_code == 202:
			print 'Accepted'
			print '--------------------------------------------------','\n'
		elif r.status_code == 203:
			print 'Non-Authoritative Information'
			print '--------------------------------------------------','\n'
		elif r.status_code == 204:
			print 'No content'
			print '--------------------------------------------------','\n'
		elif r.status_code == 205:
			print 'Reset content'
			print '--------------------------------------------------','\n'
		elif r.status_code == 206:
			print 'Partial content'
			print '--------------------------------------------------','\n'
		elif r.status_code == 207:
			print 'Multi-Status'
			print '--------------------------------------------------','\n'
	elif (r.status_code >= 300) and (r.status_code <400):
		print 'Description: Site redirection',
		if r.status_code == 300:
			print 'Multiple Choices'
			print '--------------------------------------------------','\n'
		elif r.status_code == 301:
			print 'Url moved permanently'
			print '--------------------------------------------------','\n'
		elif r.status_code == 302:
			print 'Found'
			print '--------------------------------------------------','\n'
		elif r.status_code == 303:
			print 'See other'
			print '--------------------------------------------------','\n'
		elif r.status_code == 304:
			print 'Not modified'
			print '--------------------------------------------------','\n'
		elif r.status_code == 305:
			print 'Use proxy'
			print '--------------------------------------------------','\n'
		elif r.status_code == 306:
			print 'Switch proxy'
			print '--------------------------------------------------','\n'
		elif r.status_code == 307:
			print 'Temporary ridirect'
			print '--------------------------------------------------','\n'
		elif r.status_code == 308:
			print 'Permanet redirect'
			print '--------------------------------------------------','\n'
	elif (r.status_code >= 400) and (r.status_code <500):
		print 'Description: Client Error!',
		if r.status_code == 400:
			print 'Bad request'
			print '--------------------------------------------------','\n'
		elif r.status_code == 401:
			print 'Unauthorized'
			print '--------------------------------------------------','\n'
		elif r.status_code == 402:
			print 'Payment required'
			print '--------------------------------------------------','\n'
		elif r.status_code == 403:
			print 'Forbidden'
			print '--------------------------------------------------','\n'
		elif r.status_code == 404:
			print 'Not found'
			print '--------------------------------------------------','\n'
		elif r.status_code == 405:
			print 'Method not allowed'
			print '--------------------------------------------------','\n'
		elif r.status_code == 406:
			print 'Not acceptable'
			print '--------------------------------------------------','\n'
		elif r.status_code == 407:
			print 'Proxy autentication required'
			print '--------------------------------------------------','\n'
		elif r.status_code == 408:
			print 'Request timeout'
			print '--------------------------------------------------','\n'
		elif r.status_code == 409:
			print 'Conflict'
			print '--------------------------------------------------','\n'
		elif r.status_code == 410:
			print 'Gone'
			print '--------------------------------------------------','\n'
		elif r.status_code == 411:
			print 'Lenght required'
			print '--------------------------------------------------','\n'
		elif r.status_code == 412:
			print 'Precondition failed'
			print '--------------------------------------------------','\n'
		elif r.status_code == 413:
			print 'Request entity too large'
			print '--------------------------------------------------','\n'
		elif r.status_code == 414:
			print 'Request-URI too long'
			print '--------------------------------------------------','\n'
		elif r.status_code == 415:
			print 'Unsupported media type'
			print '--------------------------------------------------','\n'
		elif r.status_code == 416:
			print 'Requested Range Not Satisfiable'
			print '--------------------------------------------------','\n'
		elif r.status_code == 417:
			print 'Expectation failed'
			print '--------------------------------------------------','\n'
		elif r.status_code == 418:
			print 'I am a teapot --> April Fool'
			print '--------------------------------------------------','\n'
		elif r.status_code == 422:
			print 'Unprocessable entity'
			print '--------------------------------------------------','\n'
		elif r.status_code == 426:
			print 'Upgrade required'
			print '--------------------------------------------------','\n'
		elif r.status_code == 449:
			print 'Retry with'
			print '--------------------------------------------------','\n'
		elif r.status_code == 451:
			print 'Unavailable For Legal Reasons (Approved by Internet Engineering Steering Group IESG)'
			print '--------------------------------------------------','\n'
	elif (r.status_code >= 500) and (r.status_code <600):
		print 'Description: Server error!',
		if r.status_code == 500:
			print 'Internal server error'
			print '--------------------------------------------------','\n'
		elif r.status_code == 501:
			print 'Not implemented'
			print '--------------------------------------------------','\n'
		elif r.status_code == 502:
			print 'Bad gateway',
			print '--------------------------------------------------','\n'
		elif r.status_code == 503:
			print 'Service unavailable'
			print '--------------------------------------------------','\n'
		elif r.status_code == 504:
			print 'Gateway timeout'
			print '--------------------------------------------------','\n'
		elif r.status_code == 505:
			print 'HTTP version not supported'
			print '--------------------------------------------------','\n'
		elif r.status_code == 509:
			print 'Bandwidth Limit Exceeded'
			print '--------------------------------------------------','\n'

#funzione di redirizzamento dell'url
def redirect(r,url):
	print ('Url richiesto:'), url
	print ('Status:'),r.status_code
	if (r.status_code >= 200) and (r.status_code < 300):
		print 'Description: Succesful site response.'
		print '--------------------------------------------------','\n'
	elif (r.status_code >= 300) and (r.status_code < 400):
		try:
			r = requests.head(url, allow_redirects=True)
			print 'Description: Site redirection'
			print '	Redirect -->',r.url
		except:
			print '	No redirect data'
		print '--------------------------------------------------','\n'
	elif (r.status_code >= 400) and (r.status_code < 500):
		print 'Description: Client Error!'
		print '--------------------------------------------------','\n'
	elif (r.status_code >= 500) and (r.status_code < 600):
		print 'Description: Server error!'
		print '--------------------------------------------------','\n'


#funzione di calcolo IP dell'url
def resolve_dns(url):
	link = string.split(url,"/")
	print link[2]
	try:
 		host = socket.gethostbyname(link[2])
		ip = socket.gethostbyname(host)
		return ip
	except:
		return ' '
#funzione per scoprire neameserver (forse)
def nameserver(url):
	link = string.split(url,'/')
	host = link[2]		
	buff = string.split(host,'.')
	if buff[0]!= 'www':
		buff = string.split(host,'.')
		dominio = '.'.join([buff[0],buff[1]])
	else:
		buff = string.split(host,'.')
		dominio = '.'.join([buff[1],buff[2]])
		dominio = '.'.join(dominio,buff[3])
	print dominio
	x = "dig " + dominio + " NS +short"
	os.system(x)
