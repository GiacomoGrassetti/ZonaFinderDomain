import smtplib
import string

def invia(ok,er,tm):
	f = open("400.txt","r") 
	f2 = open ("500.txt","r")
	f3 = open("timeout.txt","r") 

	#SETTAGGIO DATI DELLA MAIL	
	sender = '<sender email provider>'
	receivers = ['<mail@receivers.com>']
	message = """From: <sender emial provider>
MIME-Version: 1.0
Content-type: text/html
Subject: Controll domain

------------Counting record file.zona------------\f
"""+'OK:'+str(ok)+'\f'+'Errors:'+str(er)+'\f'+'Timeout:'+str(tm)+'\f'

	delimEr='--------------------------ERRORS------------------------------\f'
	delim400='-----Errors 400:-----\f'
	delim500='-----Errors 500:-----\f'
	delimTm='-------------------------TIMEOUT------------------------------\f'
	st = ' '
	st2= ' '
	st3 = ';'
	message = message+delimEr+delim400+'\f'
	while st!='':
		st = f.readline()
		message = message+ st + '\f'

	message = message + delim500 + '\f'
	while st2!='':
		st2 = f2.readline()
		message = message+ st2 + '\f'

	message = message + delimTm + '\f'
	while st3!='':
		st3 = f3.readline()
		message = message + st3 + '\f'
	#invio della mail all'host indicato
	try:
 		smtpObj = smtplib.SMTP('194.183.89.24:25')	#host
   		smtpObj.sendmail(sender, receivers, message)         
  		print "Successfully sent email"
	except:
 		print "Error: unable to send email" 
	f.close()
	f2.close()
	f3.close()
