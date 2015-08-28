from scapy.all import *

word = 'rtmp'
word.encode('hex')

def data(packet):
	try:
		# Regular expressions will be added to
		# validate the packet's content
		if word in packet[Raw].load:
			return packet[Raw].load #.encode('hex')
	except:
		pass # fix this :)

sniff(prn=data, filter='dst port 1935', count=0, store=0)
