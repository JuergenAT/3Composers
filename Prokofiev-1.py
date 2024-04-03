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
MIDI_filename = 'MIDI-P1-' + str(datetime.datetime.now().date()) + '-' + str(datetime.datetime.now().time()).replace(':', '')
MIDI_filename = MIDI_filename.replace('.','')


print("55555555555555")


# Функция для обработки MIDI-сообщений
def process_midi_message(message):
	global mn, Akt_Num, Bef_Key, BExit
	if message.type == 'note_on':
		print(f">>>>>>>>>>>>>>>>>>>>>>>>>>MIDI Note On: {message.note}")
		if Akt_Num == 198:          # ===============================================   198
			print("AktionsNr =",Akt_Num)
			if message.note == 45:
				Bef_Key[45]=False
				Bef_Key[38]=True
				mn = 99
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 199
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 199:        # ===============================================   199
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key[38]=False
				Bef_Key[45]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 200
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 200:        # ===============================================   200
			print("AktionsNr =",Akt_Num)
			if message.note == 45:
				Bef_Key[45]=False
				Bef_Key[38]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 201
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 201:        # ===============================================   201
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key[38]=False
				Bef_Key[45]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 202
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 202:        # ===============================================   202
			print("AktionsNr =",Akt_Num)
			if message.note == 45:
				Bef_Key[45]=False
				Bef_Key[38]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 203
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 203:        # ===============================================   203
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key[38]=False
				Bef_Key[45]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 204
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 204:        # ===============================================   204
			print("AktionsNr =",Akt_Num)
			if message.note == 45:
				Bef_Key[45]=False
				Bef_Key[38]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 205
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 205:        # ===============================================   205
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key[38]=False
				Bef_Key[76]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 206
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 206:        # ===============================================   206
			print("AktionsNr =",Akt_Num)
			if message.note == 76:
				Bef_Key[76]=False
				Bef_Key[81]=True
				mn = 100
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 207
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 207:       # ===============================================   207
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key[81]=False
				Bef_Key[76]=True
				mn = 101
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 208
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 208:       # ===============================================   208
			print("AktionsNr =",Akt_Num)
			if message.note == 76:
				Bef_Key[76]=False
				Bef_Key[69]=True
				mn = 102
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 209
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 209:       # ===============================================   209
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[79]=True
				mn = 103
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 210
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 210:       # ===============================================   210
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[60]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 211
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 211:       # ===============================================   211
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				#Bef_Key[60]=False
				Bef_Key[71]=True
				mn = 104
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 21101
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 21101:       # ===============================================   21101
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				#Bef_Key[60]=False
				#Bef_Key[71]=True
				mn = 105
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 21102
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 21102:       # ===============================================   21102
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				#Bef_Key[60]=False
				#Bef_Key[71]=True
				mn = 106
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 21103
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 21103:       # ===============================================   21103
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				#Bef_Key[60]=False
				#Bef_Key[71]=True
				mn = 107
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 21104
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 21104:       # ===============================================   21104
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				#Bef_Key[60]=False
				#Bef_Key[71]=True
				mn = 108
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 21105
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 21105:       # ===============================================   21105
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				#Bef_Key[60]=False
				#Bef_Key[71]=True
				mn = 109
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 21106
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 21106:       # ===============================================   21106
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				#Bef_Key[60]=False
				#Bef_Key[71]=True
				mn = 110
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 21107
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 21107:       # ===============================================   21107
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				#Bef_Key[60]=False
				#Bef_Key[71]=True
				mn = 111
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 21108
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 21108:       # ===============================================   21108
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				#Bef_Key[60]=False
				#Bef_Key[71]=True
				mn = 112
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 212
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 212:       # ===============================================   212
			print("AktionsNr =",Akt_Num)
			if message.note == 71:
				Bef_Key[71]=False
				Bef_Key[60]=False
				Bef_Key[73]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 213
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 213:       # ===============================================   213
			print("AktionsNr =",Akt_Num)
			if message.note == 73:
				Bef_Key[73]=False
				Bef_Key[90]=True
				mn = 113
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 214
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 214:       # ===============================================   214
			print("AktionsNr =",Akt_Num)
			if message.note == 90:
				Bef_Key[90]=False
				Bef_Key[79]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 215
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 215:       # ===============================================   215
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[55]=True
				mn = 114
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 216
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 216:       # ===============================================   216
			print("AktionsNr =",Akt_Num)
			if message.note == 55:
				Bef_Key[55]=False
				Bef_Key[64]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 217
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 217:       # ===============================================   217
			print("AktionsNr =",Akt_Num)
			if message.note == 64:
				Bef_Key[64]=False
				Bef_Key[31]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 218
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 218:       # ===============================================   218
			print("AktionsNr =",Akt_Num)
			if message.note == 31:
				Bef_Key[31]=False
				Bef_Key[64]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 219
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 219:       # ===============================================   219
			print("AktionsNr =",Akt_Num)
			if message.note == 64:
				Bef_Key[64]=False
				Bef_Key[31]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 220
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 220:       # ===============================================   220
			print("AktionsNr =",Akt_Num)
			if message.note == 31:
				Bef_Key[31]=False
				Bef_Key[55]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 221
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 221:       # ===============================================   221
			print("AktionsNr =",Akt_Num)
			if message.note == 55:
				Bef_Key[55]=False
				Bef_Key[36]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 222
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 222:       # ===============================================   222
			print("AktionsNr =",Akt_Num)
			if message.note == 36:
				Bef_Key[36]=False
				Bef_Key[81]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 223
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 223:       # ===============================================   223
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key[81]=False
				Bef_Key[40]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 224
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 224:       # ===============================================   224
			print("AktionsNr =",Akt_Num)
			if message.note == 40:
				Bef_Key[40]=False
				Bef_Key[81]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 225
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 225:       # ===============================================   225
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key[81]=False
				Bef_Key[37]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 226
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 226:       # ===============================================   226
			print("AktionsNr =",Akt_Num)
			if message.note == 37:
				Bef_Key[37]=False
				Bef_Key[46]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 227
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 227:       # ===============================================   227
			print("AktionsNr =",Akt_Num)
			if message.note == 46:
				Bef_Key[46]=False
				Bef_Key[28]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 228
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 228:       # ===============================================   228
			print("AktionsNr =",Akt_Num)
			if message.note == 28:
				Bef_Key[28]=False
				Bef_Key[71]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 229
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 229:       # ===============================================   229
			print("AktionsNr =",Akt_Num)
			if message.note == 71:
				Bef_Key[71]=False
				Bef_Key[81]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 230
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 230:       # ===============================================   230
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key[81]=False
				Bef_Key[31]=True
				mn = 115
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 231
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 231:       # ===============================================   231
			print("AktionsNr =",Akt_Num)
			if message.note == 31:
				Bef_Key[31]=False
				Bef_Key[68]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 232
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 232:       # ===============================================   232
			print("AktionsNr =",Akt_Num)
			if message.note == 68:
				Bef_Key[68]=False
				Bef_Key[91]=True
				mn = 116
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 233
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 233:       # ===============================================   233
			print("AktionsNr =",Akt_Num)
			if message.note == 91:
				Bef_Key[91]=False
				Bef_Key[39]=True
				mn = 117
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 234
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 234:       # ===============================================   234
			print("AktionsNr =",Akt_Num)
			if message.note == 39:
				Bef_Key[39]=False
				Bef_Key[67]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 235
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 235:       # ===============================================   235
			print("AktionsNr =",Akt_Num)
			if message.note == 67:
				Bef_Key[67]=False
				Bef_Key[28]=True
				mn = 118
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 236
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 236:       # ===============================================   236
			print("AktionsNr =",Akt_Num)
			if message.note == 28:
				Bef_Key[28]=False
				Bef_Key[79]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 237
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 237:       # ===============================================   237
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[80]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 238
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 238:       # ===============================================   238
			print("AktionsNr =",Akt_Num)
			if message.note == 80:
				Bef_Key[80]=False
				Bef_Key[88]=True
				mn = 119
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 239
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 239:       # ===============================================   239
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key[88]=False
				Bef_Key[24]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 240
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 240:       # ===============================================   240
			print("AktionsNr =",Akt_Num)
			if message.note == 24:
				Bef_Key[24]=False
				Bef_Key[31]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 241
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 241:       # ===============================================   241
			print("AktionsNr =",Akt_Num)
			if message.note == 31:
				Bef_Key[31]=False
				Bef_Key[24]=True
				mn = 120
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 242
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 242:       # ===============================================   242
			print("AktionsNr =",Akt_Num)
			if message.note == 24:
				Bef_Key[24]=False
				Bef_Key[87]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 243
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 243:       # ===============================================   243
			print("AktionsNr =",Akt_Num)
			if message.note == 87:
				Bef_Key[87]=False
				Bef_Key[30]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 244
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 244:       # ===============================================   244
			print("AktionsNr =",Akt_Num)
			if message.note == 30:
				Bef_Key[30]=False
				Bef_Key[86]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 245
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 245:       # ===============================================   245
			print("AktionsNr =",Akt_Num)
			if message.note == 86:
				Bef_Key[86]=False
				Bef_Key[82]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 246
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 246:       # ===============================================   246
			print("AktionsNr =",Akt_Num)
			if message.note == 82:
				Bef_Key[82]=False
				Bef_Key[39]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 247
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 247:       # ===============================================   247
			print("AktionsNr =",Akt_Num)
			if message.note == 39:
				Bef_Key[39]=False
				Bef_Key[53]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 248
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 248:       # ===============================================   248
			print("AktionsNr =",Akt_Num)
			if message.note == 53:
				Bef_Key[53]=False
				Bef_Key[60]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 249
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 249:       # ===============================================   249
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				Bef_Key[60]=False
				Bef_Key[30]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 250
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 250:       # ===============================================   250
			print("AktionsNr =",Akt_Num)
			if message.note == 30:
				Bef_Key[30]=False
				Bef_Key[90]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 251
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 251:       # ===============================================   251
			print("AktionsNr =",Akt_Num)
			if message.note == 90:
				Bef_Key[90]=False
				Bef_Key[26]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 252
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 252:       # ===============================================   252
			print("AktionsNr =",Akt_Num)
			if message.note == 26:
				Bef_Key[26]=False
				Bef_Key[75]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 253
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 253:       # ===============================================   253
			print("AktionsNr =",Akt_Num)
			if message.note == 75:
				Bef_Key[75]=False
				Bef_Key[32]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 254
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 254:       # ===============================================   254
			print("AktionsNr =",Akt_Num)
			if message.note == 32:
				#Bef_Key[86]=False
				#Bef_Key[32]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 255
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 255:       # ===============================================   255
			print("AktionsNr =",Akt_Num)
			if message.note == 32:
				Bef_Key[32]=False
				Bef_Key[83]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 256
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 256:       # ===============================================   256
			print("AktionsNr =",Akt_Num)
			if message.note == 83:
				Bef_Key[83]=False
				Bef_Key[69]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 257
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 257:       # ===============================================   257
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[71]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 258
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 258:       # ===============================================   258
			print("AktionsNr =",Akt_Num)
			if message.note == 71:
				Bef_Key[71]=False
				Bef_Key[96]=True
				mn = 121
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 258
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
		#Akt_Num = 197
		#print("AktionsNr =",Akt_Num)

		#initializing midi-key flags - list of 100 Befel Keys
		Bef_Key = [False]*100

		#number of Milumin Column
		mn = 98
	
		Bef_Key[45] = True
		msg = "/action/launchColumn"
		#SENDING OSC MESSAGES
		client.send_message(msg, mn) 
		print("msg=",msg,"n=",mn)
		#print("AktNr =",Akt_Num, ' passed',end='')
		Akt_Num = 198
		print(", New AktNr =",Akt_Num)

		BReRun = False
		# Запускаем цикл для обработки онлайн MIDI-сообщений
		while True:
			message = input_port.poll()
			if message:
				track.append(message)
				process_midi_message(message)
				if message.type == 'note_on' or message.type == 'note_off':
					#print("message=", message)
					#track.append(mido.Message('note_on', note = message.note, velocity=64, time=64))
					#track.append(mido.Message('note_off', note = message.note, velocity=64, time=128))
					pass
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


