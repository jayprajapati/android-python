import android,time,sys,os
import subprocess,pynotify

def sendmessage(message):
	subprocess.Popen(['notify-send', message])
	return

def check_device(ip):
	bashCommand = "sudo nmap "+ip+" -p 2158"
	output = subprocess.check_output(['bash','-c', bashCommand])
	if(output.find("mac_id_here")!=-1):
		jay=1
			
		return jay
	else:
		ip=0
	
ips=["192.168.0.1","192.168.0.2","192.168.0.3","192.168.0.4","192.168.0.5","192.168.0.6","192.168.0.7","192.168.0.8"]
#you can change your ips according to your gateway ip
for ip in ips:
	if(check_device(ip)==1):
		print "Your ip is " + ip
		flag=1		
		break
	else:
		flag=0
if(flag==1):
	droid=android.Android((ip,2158))
else:
	sys.exit('Device not found')	





print "Connected to zenfone"
sendmessage("Connected To ASUS ZENFONE..")
droid.startTrackingPhoneState()
sendmessage("Dont you worry, i have my eyes on your phone!")
while 1:
	yes=droid.readPhoneState().result
	if yes['state']=='ringing':
		number=yes['incomingNumber']
		msg= "Hey Jay , Incoming Call From " + number + " to ASUS Zenfone"
		sendmessage(msg)
		time.sleep(60)
	
	print "Sleeping..!"	
	print yes	
	time.sleep(5)


