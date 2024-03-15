import time
import mido
from mido import MidiFile, MidiTrack
from pynput import keyboard
from pythonosc.udp_client import SimpleUDPClient
import datetime  #for use in MIDI file name generation



'''
Code for online receiving and processing of MIDI signals and computer keyboard events. 
According to the specified algorithm, OSC messages are generated based on MIDI signals 
to control external audio-visual equipment/interactive shows.

tested for MacOS Ventura 13.6.3
MacBook Pro 13" 2020 M1

Keyboard buttons:
'Q', 'q' - quit/exit
'R', 'r' - re run from the beginning
'B', 'b' - block/unblock MIDI processing

'''

#initializing ip, port for OSC-commands
ip = "127.0.0.1"
port = 5000

print("44444444444444")

client = SimpleUDPClient(ip, port)  # Create client

#generate MIDI-file name to write
MIDI_filename = 'MIDI-B2-' + str(datetime.datetime.now().date()) + '-' + str(datetime.datetime.now().time()).replace(':', '')
MIDI_filename = MIDI_filename.replace('.','')


print("55555555555555")


# Функция для обработки MIDI-сообщений
def process_midi_message(message):
	global mn, Akt_Num, Bef_Key, BExit
	if message.type == 'note_on':
		print(f"MIDI Note On: {message.note}")
		if Akt_Num == 61:          # ===============================================   061
			print("AktionsNr =",Akt_Num)
			Bef_Key[45] = True
			mn = 23
			msg = "/action/launchColumn"
			#SENDING OSC MESSAGES
			client.send_message(msg, mn) 
			print("msg=",msg,"n=",mn)
			print("AktNr =",Akt_Num, ' passed',end='')
			Akt_Num = 62
			print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 62:        # ===============================================   062
			print("AktionsNr =",Akt_Num)
			if message.note == 45:
				Bef_Key[45]=False
				Bef_Key[49]=True
				mn = 24
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 63
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 63:        # ===============================================   063
			print("AktionsNr =",Akt_Num)
			if message.note == 49:
				Bef_Key[49]=False
				Bef_Key[50]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 64
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 64:        # ===============================================   064
			print("AktionsNr =",Akt_Num)
			if message.note == 50:
				Bef_Key[50]=False
				Bef_Key[49]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 65
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 65:        # ===============================================   065
			print("AktionsNr =",Akt_Num)
			if message.note == 49:
				Bef_Key[49]=False
				Bef_Key[41]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 66
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 66:        # ===============================================   066
			print("AktionsNr =",Akt_Num)
			if message.note == 41:
				Bef_Key[41]=False
				Bef_Key[43]=True
				mn = 25
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 67
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 67:        # ===============================================   067
			print("AktionsNr =",Akt_Num)
			if message.note == 43:
				Bef_Key[43]=False
				Bef_Key[40]=True
				mn = 26
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 68
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 68:        # ===============================================   068
			print("AktionsNr =",Akt_Num)
			if message.note == 40:
				Bef_Key[40]=False
				Bef_Key[38]=True
				mn = 27
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 69
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 69:        # ===============================================   069
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key[38]=False
				Bef_Key[43]=True
				mn = 28
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 70
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 70:       # ===============================================   070
			print("AktionsNr =",Akt_Num)
			if message.note == 43:
				Bef_Key[43]=False
				Bef_Key[36]=True
				mn = 29
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 71
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 71:       # ===============================================   071
			print("AktionsNr =",Akt_Num)
			if message.note == 36:
				Bef_Key[36]=False
				Bef_Key[41]=True
				mn = 30
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 72
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 72:       # ===============================================   072
			print("AktionsNr =",Akt_Num)
			if message.note == 41:
				Bef_Key[41]=False
				Bef_Key[40]=True
				mn = 31
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 73
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 73:       # ===============================================   073
			print("AktionsNr =",Akt_Num)
			if message.note == 40:
				Bef_Key[40]=False
				Bef_Key[52]=True
				mn = 32
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 74
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 74:       # ===============================================   074
			print("AktionsNr =",Akt_Num)
			if message.note == 52:
				Bef_Key[52]=False
				Bef_Key[76]=True
				mn = 33
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 75
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 75:       # ===============================================   075
			print("AktionsNr =",Akt_Num)
			if message.note == 76:
				Bef_Key[76]=False
				Bef_Key[69]=True
				mn = 34
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 76
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 76:       # ===============================================   076
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[64]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 77
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 77:       # ===============================================   077
			print("AktionsNr =",Akt_Num)
			if message.note == 64:
				Bef_Key[64]=False
				Bef_Key[77]=True
				mn = 35
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 78
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 78:       # ===============================================   078
			print("AktionsNr =",Akt_Num)
			if message.note == 77:
				Bef_Key[77]=False
				Bef_Key[57]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 79
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 79:       # ===============================================   079
			print("AktionsNr =",Akt_Num)
			if message.note == 57:
				Bef_Key[57]=False
				Bef_Key[77]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 80
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 80:       # ===============================================   080
			print("AktionsNr =",Akt_Num)
			if message.note == 77:
				Bef_Key[77]=False
				Bef_Key[37]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 81
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 81:       # ===============================================   081
			print("AktionsNr =",Akt_Num)
			if message.note == 37:
				Bef_Key[37]=False
				Bef_Key[77]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 82
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 82:       # ===============================================   082
			print("AktionsNr =",Akt_Num)
			if message.note == 77:
				Bef_Key[77]=False
				Bef_Key[69]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 83
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 83:       # ===============================================   083
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[86]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 84
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 84:       # ===============================================   084
			print("AktionsNr =",Akt_Num)
			if message.note == 86:
				Bef_Key[86]=False
				Bef_Key[83]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 85
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 85:       # ===============================================   085
			print("AktionsNr =",Akt_Num)
			if message.note == 83:
				Bef_Key[83]=False
				Bef_Key[79]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 86
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 86:       # ===============================================   086
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[67]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 87
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 87:       # ===============================================   087
			print("AktionsNr =",Akt_Num)
			if message.note == 67:
				Bef_Key[67]=False
				Bef_Key[79]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 88
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 88:       # ===============================================   088
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[67]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 89
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 89:       # ===============================================   089
			print("AktionsNr =",Akt_Num)
			if message.note == 67:
				Bef_Key[67]=False
				Bef_Key[79]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 90
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 90:       # ===============================================   090
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[38]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 91
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 91:       # ===============================================   091
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key[38]=False
				Bef_Key[52]=True
				mn = 36
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 92
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 92:       # ===============================================   092
			print("AktionsNr =",Akt_Num)
			if message.note == 52:
				Bef_Key[52]=False
				Bef_Key[29]=True
				mn = 37
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 93
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 93:       # ===============================================   093
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				Bef_Key[29]=False
				Bef_Key[52]=True
				mn = 38
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 94
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 94:       # ===============================================   094
			print("AktionsNr =",Akt_Num)
			if message.note == 52:
				Bef_Key[52]=False
				Bef_Key[60]=True
				mn = 39
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 95
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 95:       # ===============================================   095
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				Bef_Key[60]=False
				Bef_Key[52]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 96
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 96:       # ===============================================   096
			print("AktionsNr =",Akt_Num)
			if message.note == 52:
				Bef_Key[52]=False
				Bef_Key[41]=True
				mn = 40
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 97
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 97:       # ===============================================   097
			print("AktionsNr =",Akt_Num)
			if message.note == 41:
				Bef_Key[41]=False
				Bef_Key[60]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 98
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 98:       # ===============================================   098
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				Bef_Key[60]=False
				Bef_Key[33]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 99
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 99:       # ===============================================   099
			print("AktionsNr =",Akt_Num)
			if message.note == 33:
				Bef_Key[33]=False
				Bef_Key[83]=True
				mn = 41
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 100
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 100:       # ===============================================   100
			print("AktionsNr =",Akt_Num)
			if message.note == 83:
				Bef_Key[83]=False
				Bef_Key[31]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 101
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 101:       # ===============================================   101
			print("AktionsNr =",Akt_Num)
			if message.note == 31:
				Bef_Key[31]=False
				Bef_Key[81]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 102
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 102:       # ===============================================   102
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key[81]=False
				Bef_Key[40]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 103
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 103:       # ===============================================   103
			print("AktionsNr =",Akt_Num)
			if message.note == 40:
				Bef_Key[40]=False
				Bef_Key[38]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 104
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 104:       # ===============================================   104
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key[38]=False
				Bef_Key[35]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 105
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 105:       # ===============================================   105
			print("AktionsNr =",Akt_Num)
			if message.note == 35:
				Bef_Key[35]=False
				Bef_Key[33]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 106
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 106:       # ===============================================   106
			print("AktionsNr =",Akt_Num)
			if message.note == 33:
				Bef_Key[33]=False
				Bef_Key[35]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 107
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 107:       # ===============================================   107
			print("AktionsNr =",Akt_Num)
			if message.note == 35:
				Bef_Key[35]=False
				Bef_Key[81]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 108
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 108:       # ===============================================   108
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key[81]=False
				Bef_Key[31]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 109
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 109:       # ===============================================   109
			print("AktionsNr =",Akt_Num)
			if message.note == 31:
				Bef_Key[31]=False
				Bef_Key[32]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 110
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 110:       # ===============================================   110
			print("AktionsNr =",Akt_Num)
			if message.note == 32:
				Bef_Key[32]=False
				Bef_Key[67]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 111
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 111:       # ===============================================   111
			print("AktionsNr =",Akt_Num)
			if message.note == 67:
				Bef_Key[67]=False
				Bef_Key[68]=True
				mn = 42
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 112
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 112:       # ===============================================   112
			print("AktionsNr =",Akt_Num)
			if message.note == 68:
				Bef_Key[68]=False
				Bef_Key[37]=True
				mn = 43
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 113
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 113:       # ===============================================   113
			print("AktionsNr =",Akt_Num)
			if message.note == 37:
				Bef_Key[37]=False
				Bef_Key[69]=True
				mn = 44
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 114
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 114:       # ===============================================   114
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[67]=True
				mn = 45
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 115
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 115:       # ===============================================   115
			print("AktionsNr =",Akt_Num)
			if message.note == 67:
				Bef_Key[67]=False
				Bef_Key[76]=True
				mn = 46
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 116
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 116:       # ===============================================   116
			print("AktionsNr =",Akt_Num)
			if message.note == 76:
				Bef_Key[76]=False
				Bef_Key[78]=True
				mn = 47
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 117
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 117:       # ===============================================   117
			print("AktionsNr =",Akt_Num)
			if message.note == 78:
				Bef_Key[78]=False
				Bef_Key[33]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 118
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 118:       # ===============================================   118
			print("AktionsNr =",Akt_Num)
			if message.note == 33:
				Bef_Key[33]=False
				Bef_Key[73]=True
				mn = 48
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 119
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 119:       # ===============================================   119
			print("AktionsNr =",Akt_Num)
			if message.note == 73:
				Bef_Key[73]=False
				Bef_Key[67]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 120
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 120:       # ===============================================   120
			print("AktionsNr =",Akt_Num)
			if message.note == 67:
				Bef_Key[67]=False
				Bef_Key[33]=True
				mn = 49
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 121
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 121:       # ===============================================   121
			print("AktionsNr =",Akt_Num)
			if message.note == 33:
				Bef_Key[33]=False
				mn = 50
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 121
				print(", New AktNr =",Akt_Num)
				BExit = True
			pass
		
	#elif message.type == 'note_off' and message.channel == TARGET_INSTRUMENT:
		#print(f"MIDI Note Off: {message.note}")
    # Другие проверки, если необходимо




# Функция для обработки событий клавиатуры
def on_key_press(key):
	global BExit, BReRun, BBlock
	try:
		print(f"Key {key.char} pressed")
		if key.char == 'Q' or key.char == 'q':
			BExit = True
		if key.char == 'R' or key.char == 'r':
			BReRun = True
		if key.char == 'B' or key.char == 'b':
			BBlock = not BBlock
	except AttributeError:
		print(f"Special key {key} pressed")


print("6666666666666666")


#open MIDI-file to write msg
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)




#To get a list of available ports
port_List = mido.get_output_names()
print("MIDI-Ports available:", port_List)

print("77777777777777")


if len(port_List) > 0 and port_List[0] != 'To Millumin':
	# Открываем виртуальный MIDI-вход для чтения сообщений
	input_port = mido.open_input(port_List[0])  # Замените на имя вашего MIDI-устройства
	BReRun = True
	BExit = False
	BBlock = False
else:
	print("No any MIDI-ports are available. Program stop")
	BReRun = False
	BExit = True
	BBlock = False

print("8888888888888")



#внешний цикл для перезапуска сначала/BReRun
while BReRun and (not BExit):
	with keyboard.Listener(on_press=on_key_press) as listener:
	#try:
		print("99999999999")
		# первое событие с инициализацией без участия MIDI
		
		#initialize Aktionsnummer while MIDI message comes
		Akt_Num = 61
		print("AktionsNr =",Akt_Num)

		#initializing midi-key flags - list of 100 Befel Keys
		Bef_Key = [False]*100

		#number of Milumin Column
		mn = 23
	
		Bef_Key[45] = True
		msg = "/action/launchColumn"
		#SENDING OSC MESSAGES
		client.send_message(msg, mn) 
		print("msg=",msg,"n=",mn)
		print("AktNr =",Akt_Num, ' passed',end='')
		Akt_Num = 62
		print(", New AktNr =",Akt_Num)

		BReRun = False
		# Запускаем цикл для обработки онлайн MIDI-сообщений
		while True:
			message = input_port.poll()
			if message:
				process_midi_message(message)
				if message.type == 'note_on' or message.type == 'note_off':
					#print("message=", message)
					track.append(mido.Message('note_on', note = message.note, velocity=64, time=32))
					track.append(mido.Message('note_off', note = message.note, velocity=64, time=64))
			#else:
				#print("mn=",mn)
				
			#выход из цикла по событиям BReRun/BExit
			if BReRun or BExit:
				break

			time.sleep(0.01)
		#end of internal cycle
	#end of with
	#выход из внешнего цикла по событию BExit
	if BExit:
		break
#end of external cycle
			
'''       
except KeyboardInterrupt:
	pass    
except:
	print("Something else went wrong") 
'''

#finally:
	#print ("\nClosing OSCClient")
	#close OSC-port
	#client.close() - there is no method close()

print("E-11111111111111111")
keyboard.Listener.stop
print("E-22222222222222222")
if len(port_List) > 0:
	print ("Closing MIDI-port")
	input_port.close()  # Важно закрыть порт после использования
print("E-333333333333333333")
print ("\nMIDI-port closed")
#save MIDI-file
mid.save(MIDI_filename+'.mid')
print("MIDI-file is saved")
print("E-444444444444444444")


