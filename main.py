import requests
import statusArg
import sys
import colour as cms
import string
import delete

c=0	#contatore righe per scruittura intetsazione

if len(sys.argv)!= 3:
	print cms.color('<red>ERROR: Bad parameters</red>')	#controllo argc
	print 'Visita il manuale scrivendo --help come opzione!'
	sys.exit()

f = open(sys.argv[1], "r+")	#apertura file .zona

if sys.argv[1]==None:
	print cms.color('<red>File has not been opened</red>')	#controllo file
	print 'Visita il manuale scrivendo --help come opzione!'
	sys.exit()

while c<20:
	st=f.readline()		#scrittura intestazione del file .zona
	c = c+1

if sys.argv[2]=='--help':	#pannello di aiuto
	print '-----------------------------------------------------------------------'
	print 'PROGRAM MANUAL\nProgramming language used: Python v3.x'
	print 'Selezionare UNA delle seguenti opzioni:'
	print 'USABLE OPTIONS:'
	print '-s : Shows the detailed status of the site content with code;'
	print '-r : Show, on sites with 3xx status, the redirect link;'
	print '-ip : Show url IP addresses;'
	print 'Syntax: python [prog_name] [zone_file] [-option]'
	print '-----------------------------------------------------------------------'

if sys.argv[2]==None:
	if stm[0]=='@':
		url = '<your url>'
	else:
		url = 'http://' + stm[0] + '.<your_subdomain.it>'
	r = requests.head(url, allow_redirects=False, timeout=15)
	delete.elimina(sys.argv[2])


stm = string.split(st,'   ')		#stm = stringa modificata

#inizializzazione delle opzioni

if sys.argv[2]=='-s':			
	if stm[0]=='@':
		url = '<your url>'
	else:
		url = 'http://' + stm[0] + '.<your_subdomain.it>'
	#r = requests.head(url, allow_redirects=False, timeout=15)
	delete.elimina(sys.argv[2])

elif sys.argv[2]=='-r':
	if stm[0]=='@':
		url = '<your url>'
	else:
		url = 'http://' + stm[0] + '.<your_subdomain.it>'
	#r = requests.head(url, allow_redirects=False, timeout=15)
	delete.elimina(sys.argv[2])

elif sys.argv[2]=='-NS':
	if stm[0]=='@':
		url = '<your url>'
	else:
		url = 'http://' + stm[0] + '.<your_subdomain.it>'
	try:
		r = requests.head(url, allow_redirects=False, timeout=15)
		pass
	except:
		print cms.color('<red>Timeout - seconds=15</red>')

	delete.elimina(sys.argv[2])
		
elif sys.argv[2]=='-ip':
	if stm[0]=='@':
		url = '<your url>'
	else:
		url = 'http://' + stm[0] + '.<your_subdomain.it>'
	#	r = requests.head(url, allow_redirects=False, timeout=15)

	delete.elimina(sys.argv[2])

print cms.color('<green> Operation successully complite</green>')
f.close()
