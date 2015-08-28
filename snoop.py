from scapy.all import *

word = str('rtmp')
word.encode('hex')

def data(packet):
	try:
		if word in packet.getlayer(Raw).load:
			return str(packet[Raw].load.encode('hex')
	except:
		pass

sniff(prn=data, filter='dst port 1935', count=0, store=0)
