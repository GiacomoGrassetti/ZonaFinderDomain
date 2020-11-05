import requests
import sys
import string
import colour as cms
import statusArg
import mail

def elimina(option):	#creazione di file
	f = open(sys.argv[1],"r")
	fout = open("updated.txt", "w")
	fout2 = open("400.txt", "w")
	fout21 = open("500.txt", "w")
	fout3 = open("timeout.txt", "w")

	i=0
	c=0
	

	#scrittura intestazione su file
	while c<20:
	    st=f.readline()
		fout.write(st)
       	c = c+1

	fout.close()
	fout2.close()
	fout3.close()

	fout = open("updated.txt","a")	#apertura per scrittura sui file
	fout2 = open("400.txt","a")
	fout21 = open("500.txt","a")
	fout3 = open("timeout.txt","a")

	c=0
	#inizializzazione contatori per gli status
	ok=0
	er=0
	tm=0

	st = ''

	#scrittura url senza 400-600
	for st in f:
		stm = string.split(st,'   ')
		if stm[0]=='@':
			url = '<your url>'
		else:
			url = 'http://' + stm[0] + '.<your_subdomain.it>'
			try:
				r = requests.head(url, allow_redirects=False, timeout=90)
				if not((r.status_code>=400)and(r.status_code<600)):
					fout.write(st)
					ok = ok +1
				else: #in errore
					print r.status_code
					if(r.status_code>=400)and(r.status_code<500):
						fout2.write(st)
						er = er + 1
					elif(r.status_code>=500)and(r.status_code<600):
						fout21.write(st)
						er = er + 1
				pass
			except:
				print ('Timeout - seconds=90')
				if not((st[0]==';') or (st[0]==' ') or (st[0]=='') or (st[0]=='	')):
					print st
					fout3.write(st)
					tm = tm + 1

		#richiamo funzioni per opzioni
		if option=='-s':
			statusArg.control_status(r,url)
		elif option=='-r':
			statusArg.redirect(r,url)
		elif option=='-ip':
			ip=statusArg.resolve_dns(url)
			print ip,'\n'
			print '----------------------------------------------\n'
		elif option=='-NS':
			statusArg.nameserver(url)

	fout.close()
	fout2.close()
	fout21.close()
	fout3.close()
	mail.invia(ok,er,tm-3)
