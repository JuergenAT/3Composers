import time
import mido
from mido import MidiFile, MidiTrack
from pynput import keyboard
from pythonosc.udp_client import SimpleUDPClient
#import datetime  #for use in MIDI file name generation



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
#MIDI_filename = 'MIDI-B3-' + str(datetime.datetime.now().date()) + '-' + str(datetime.datetime.now().time()).replace(':', '')
#MIDI_filename = MIDI_filename.replace('.','')


print("55555555555555")

# функции обработки вторично активных миди-клавиш

def f_Bef15101():
	Bef_Key  -= {81}
	Bef_Key  |= {31}
	print("AktNr =",Akt_Num, ' passed',end='')
	Akt_Num = 15102
	print(", New AktNr =",Akt_Num)

def f_Bef15102():
	Bef_Key  -= {31}
	Bef_Key  |= {81}
	print("AktNr =",Akt_Num, ' passed',end='')
	Akt_Num = 15103
	print(", New AktNr =",Akt_Num)

def f_Bef15103():
	Bef_Key -= {81}
	Bef_Key |= {90}
	print("AktNr =",Akt_Num, ' passed',end='')
	Akt_Num = 152
	print(", New AktNr =",Akt_Num)

def f_Bef152():
	global mn, Akt_Num, Bef_Key
	Bef_Key -= {90}
	Bef_Key |= {81}
	mn = 77
	msg = "/action/launchColumn"
	#SENDING OSC MESSAGES
	client.send_message(msg, mn) 
	print("msg=",msg,"n=",mn)
	print("AktNr =",Akt_Num, ' passed',end='')
	Akt_Num = 153
	print(", New AktNr =",Akt_Num)




# Функция для обработки MIDI-сообщений
def process_midi_message(message):
	global mn, Akt_Num, Bef_Key, BExit
	if message.type == 'note_on':
		print(f">>>>>>>>>>>>>>>>>>>>>>>>>>MIDI Note On: {message.note}")
		if Akt_Num == 123:          # ===============================================   123
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key -= {81}
				Bef_Key |= {50}
				mn = 51
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 124
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 124:        # ===============================================   124
			print("AktionsNr =",Akt_Num)
			if message.note == 50:
				Bef_Key -= {50}
				Bef_Key |= {54}
				mn = 52
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 125
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 125:        # ===============================================   125
			print("AktionsNr =",Akt_Num)
			if message.note == 54:
				Bef_Key -= {54}
				Bef_Key |= {55}
				mn = 53
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 126
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 126:        # ===============================================   126
			print("AktionsNr =",Akt_Num)
			if message.note == 55:
				Bef_Key -= {55}
				Bef_Key |= {57}
				mn = 54
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 127
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 127:        # ===============================================   127
			print("AktionsNr =",Akt_Num)
			if message.note == 57:
				Bef_Key -= {57}
				Bef_Key |= {59}
				mn = 55
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 128
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 128:        # ===============================================   128
			print("AktionsNr =",Akt_Num)
			if message.note == 59:
				Bef_Key -= {59}
				Bef_Key |= {61}
				mn = 56
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 129
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 129:        # ===============================================   129
			print("AktionsNr =",Akt_Num)
			if message.note == 61:
				Bef_Key -= {61}
				Bef_Key |= {62}
				mn = 57
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 130
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 130:        # ===============================================   130
			print("AktionsNr =",Akt_Num)
			if message.note == 62:
				Bef_Key -= {62}
				Bef_Key |= {64}
				mn = 58
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 131
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 131:        # ===============================================   131
			print("AktionsNr =",Akt_Num)
			if message.note == 64:
				Bef_Key -= {64}
				Bef_Key |= {66}
				mn = 59
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 132
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 132:       # ===============================================   132
			print("AktionsNr =",Akt_Num)
			if message.note == 66:
				Bef_Key -= {66}
				Bef_Key |= {56}
				mn = 60
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 133
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 133:       # ===============================================   133
			print("AktionsNr =",Akt_Num)
			if message.note == 56:
				Bef_Key -= {56}
				Bef_Key |= {57}
				mn = 61
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 134
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 134:       # ===============================================   134
			print("AktionsNr =",Akt_Num)
			if message.note == 57:
				Bef_Key -= {57}
				Bef_Key |= {62}
				mn = 62
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 135
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 135:       # ===============================================   135
			print("AktionsNr =",Akt_Num)
			if message.note == 62:
				Bef_Key -= {62}
				Bef_Key |= {61}
				mn = 63
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 136
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 136:       # ===============================================   136
			print("AktionsNr =",Akt_Num)
			if message.note == 61:
				Bef_Key -= {61}
				Bef_Key |= {59}
				mn = 64
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 137
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 137:       # ===============================================   137
			print("AktionsNr =",Akt_Num)
			if message.note == 59:
				Bef_Key -= {59}
				Bef_Key |= {64}
				mn = 65
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 138
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 138:       # ===============================================   138
			print("AktionsNr =",Akt_Num)
			if message.note == 64:
				Bef_Key -= {64}
				Bef_Key |= {61}
				mn = 66
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 139
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 139:       # ===============================================   139
			print("AktionsNr =",Akt_Num)
			if message.note == 61:
				Bef_Key -= {61}
				Bef_Key |= {59}
				mn = 67
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 140
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 140:       # ===============================================   140
			print("AktionsNr =",Akt_Num)
			if message.note == 59:
				Bef_Key -= {59}
				Bef_Key |= {57}
				mn = 68
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 141
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 141:       # ===============================================   141
			print("AktionsNr =",Akt_Num)
			if message.note == 57:
				Bef_Key -= {57}
				Bef_Key |= {64}
				mn = 69
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 142
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 142:       # ===============================================   142
			print("AktionsNr =",Akt_Num)
			if message.note == 64:
				Bef_Key -= {64}
				Bef_Key |= {62}
				mn = 70
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 143
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 143:       # ===============================================   143
			print("AktionsNr =",Akt_Num)
			if message.note == 62:
				Bef_Key -= {62}
				Bef_Key |= {61}
				mn = 71
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 144
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 144:       # ===============================================   144
			print("AktionsNr =",Akt_Num)
			if message.note == 61:
				Bef_Key -= {61}
				Bef_Key |= {59}
				mn = 72
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 145
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 145:       # ===============================================   145
			print("AktionsNr =",Akt_Num)
			if message.note == 59:
				Bef_Key -= {59}
				Bef_Key |= {69}
				mn = 73
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 146
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 146:       # ===============================================   146
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key -= {69}
				Bef_Key |= {30}
				mn = 74
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 147
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 147:       # ===============================================   147
			print("AktionsNr =",Akt_Num)
			if message.note == 30:
				Bef_Key -= {30}
				Bef_Key |= {54}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 148
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 148:       # ===============================================   148
			print("AktionsNr =",Akt_Num)
			if message.note == 54:
				Bef_Key -= {54}
				Bef_Key |= {47}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 149
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 149:       # ===============================================   149
			print("AktionsNr =",Akt_Num)
			if message.note == 47:
				Bef_Key -= {47}
				Bef_Key |= {79}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 150
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 150:       # ===============================================   150
			print("AktionsNr =",Akt_Num)
			if message.note not in Bef_Key: # 79
				return
			if message.note == 79:
				Bef_Key -= {79}
				Bef_Key |= {38, 90}
				mn = 75
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 151
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 151:       # ===============================================   151
			print("AktionsNr =",Akt_Num)
			if message.note not in Bef_Key: # 38, 90
				return
			if message.note == 38:
				Bef_Key -= {38}
				Bef_Key |= {81}
				mn = 76
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 15101
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 15101:       # ===============================================   15101
			print("AktionsNr =",Akt_Num)
			if message.note not in Bef_Key: # 81, 90
				return
			if message.note == 81:
				f_Bef15101()
			elif message.note == 90:
				f_Bef152()
		elif Akt_Num == 15102:       # ===============================================   15102
			print("AktionsNr =",Akt_Num)
			if message.note not in Bef_Key: # 31, 90
				return
			if message.note == 31:     
				f_Bef15102()
			elif message.note == 90:
				f_Bef152()
		elif Akt_Num == 15103:       # ===============================================   15103
			print("AktionsNr =",Akt_Num)
			if message.note not in Bef_Key: # 81, 90
				return
			if message.note == 81:
				f_Bef15103()
			elif message.note == 90:
				f_Bef152()
		elif Akt_Num == 152:       # ===============================================   152
			print("AktionsNr =",Akt_Num)
			if message.note not in Bef_Key: # 90
				return
			if message.note == 90:
				f_Bef152()
		elif Akt_Num == 153:       # ===============================================   153
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key -= {81}
				Bef_Key |= {88}
				mn = 78
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 154
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 154:       # ===============================================   154
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key -= {88}
				Bef_Key |= {81}
				mn = 79
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 155
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 155:       # ===============================================   155
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key -= {81}
				Bef_Key |= {88}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 156
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 156:       # ===============================================   156
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key -= {88}
				Bef_Key |= {83}
				mn = 80
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 157
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 157:       # ===============================================   157
			print("AktionsNr =",Akt_Num)
			if message.note == 83:
				Bef_Key -= {83}
				Bef_Key |= {88}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 158
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 158:       # ===============================================   158
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key -= {88}
				Bef_Key |= {33}
				mn = 81
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 159
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 159:       # ===============================================   159
			print("AktionsNr =",Akt_Num)
			if message.note == 33:
				Bef_Key -= {33}
				Bef_Key |= {47}
				mn = 82
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 160
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 160:       # ===============================================   160
			print("AktionsNr =",Akt_Num)
			if message.note == 47:
				Bef_Key -= {47}
				Bef_Key |= {38}
				mn = 83
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 161
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 161:       # ===============================================   161
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key -= {38}
				Bef_Key |= {42}
				mn = 84
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 162
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 162:       # ===============================================   162
			print("AktionsNr =",Akt_Num)
			if message.note == 42:
				Bef_Key -= {42}
				Bef_Key |= {40}
				mn = 85
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 163
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 163:       # ===============================================   163
			print("AktionsNr =",Akt_Num)
			if message.note == 40:
				Bef_Key -= {40}
				Bef_Key |= {48}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 164
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 164:       # ===============================================   164
			print("AktionsNr =",Akt_Num)
			if message.note == 48:
				Bef_Key -= {48}
				Bef_Key |= {81}
				mn = 86
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 165
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 165:       # ===============================================   165
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key -= {81}
				Bef_Key |= {54}
				mn = 87
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 166
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 166:       # ===============================================   166
			print("AktionsNr =",Akt_Num)
			if message.note == 54:
				Bef_Key -= {54}
				Bef_Key |= {78}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 167
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 167:       # ===============================================   167
			print("AktionsNr =",Akt_Num)
			if message.note == 78:
				Bef_Key -= {78}
				Bef_Key |= {57}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 168
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 168:       # ===============================================   168
			print("AktionsNr =",Akt_Num)
			if message.note == 57:
				Bef_Key -= {57}
				Bef_Key |= {55}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 169
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 169:       # ===============================================   169
			print("AktionsNr =",Akt_Num)
			if message.note == 55:
				Bef_Key -= {55}
				Bef_Key |= {66}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 170
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 170:       # ===============================================   170
			print("AktionsNr =",Akt_Num)
			if message.note == 66:
				Bef_Key -= {66}
				Bef_Key |= {67}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 171
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 171:       # ===============================================   171
			print("AktionsNr =",Akt_Num)
			if message.note == 67:
				Bef_Key -= {67}
				Bef_Key |= {47}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 172
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 172:       # ===============================================   172
			print("AktionsNr =",Akt_Num)
			if message.note == 47:
				Bef_Key -= {47}
				Bef_Key |= {71}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 173
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 173:       # ===============================================   173
			print("AktionsNr =",Akt_Num)
			if message.note == 71:
				Bef_Key -= {71}
				Bef_Key |= {55}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 17301
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 17301:       # ===============================================   17301
			print("AktionsNr =",Akt_Num)
			if message.note == 55:
				Bef_Key -= {55}
				Bef_Key |= {79}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 17302
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 17302:       # ===============================================   17302
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key -= {79}
				Bef_Key |= {59}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 17303
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 17303:       # ===============================================   17303
			print("AktionsNr =",Akt_Num)
			if message.note == 59:
				Bef_Key -= {59}
				Bef_Key |= {71}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 17304
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 17304:       # ===============================================   17304
			print("AktionsNr =",Akt_Num)
			if message.note == 71:
				Bef_Key -= {71}
				Bef_Key |= {88}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 174
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 174:       # ===============================================   174
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key -= {88}
				Bef_Key |= {84}
				mn = 88
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 175
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 175:       # ===============================================   175
			print("AktionsNr =",Akt_Num)
			if message.note == 84:
				Bef_Key -= {84}
				Bef_Key |= {76}
				mn = 89
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 176
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 176:       # ===============================================   176
			print("AktionsNr =",Akt_Num)
			if message.note == 76:
				Bef_Key -= {76}
				Bef_Key |= {48}
				Bef_Key |= {88}
				mn = 90
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 177
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 177:       # ===============================================   177
			print("AktionsNr =",Akt_Num)
			if message.note not in Bef_Key: # 48, 88
				return
			if message.note == 48:
				mn = 91
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 178
				print(", New AktNr =",Akt_Num)
			elif message.note == 88:
				Bef_Key -= {88}
				Bef_Key -= {48}
				Bef_Key |= {30}
				mn = 92
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 179
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 178:       # ===============================================   178
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key -= {88}
				Bef_Key -= {48}
				Bef_Key |= {30}
				mn = 92
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 179
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 179:       # ===============================================   179
			print("AktionsNr =",Akt_Num)
			if message.note == 30:
				Bef_Key -= {30}
				Bef_Key |= {34}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 180
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 180:       # ===============================================   180
			print("AktionsNr =",Akt_Num)
			if message.note == 34:
				Bef_Key -= {34}
				Bef_Key |= {33}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 181
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 181:       # ===============================================   181
			print("AktionsNr =",Akt_Num)
			if message.note == 33:
				Bef_Key -= {33}
				Bef_Key |= {31}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 182
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 182:       # ===============================================   182
			print("AktionsNr =",Akt_Num)
			if message.note == 31:
				Bef_Key -= {31}
				Bef_Key |= {88}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 183
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 183:       # ===============================================   183
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key -= {88}
				Bef_Key |= {64}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 18301
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 18301:       # ===============================================   18301
			print("AktionsNr =",Akt_Num)
			if message.note == 64:
				Bef_Key -= {64}
				Bef_Key |= {71}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 184
				print(", New AktNr =",Akt_Num)
			pass	
		elif Akt_Num == 184:       # ===============================================   184
			print("AktionsNr =",Akt_Num)
			if message.note == 71:
				Bef_Key -= {71}
				Bef_Key |= {35}
				mn = 93
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 185
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 185:       # ===============================================   185
			print("AktionsNr =",Akt_Num)
			if message.note == 35:
				Bef_Key -= {35}
				Bef_Key |= {84}
				mn = 94
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 186
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 186:       # ===============================================   186
			print("AktionsNr =",Akt_Num)
			if message.note == 84:
				Bef_Key -= {84}
				Bef_Key |= {35}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 187
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 187:       # ===============================================   187
			print("AktionsNr =",Akt_Num)
			if message.note == 35:
				Bef_Key -= {35}
				Bef_Key |= {88}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 188
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 188:       # ===============================================   188
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key -= {88}
				Bef_Key |= {32}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 189
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 189:       # ===============================================   189
			print("AktionsNr =",Akt_Num)
			if message.note == 32:
				Bef_Key -= {32}
				Bef_Key |= {88}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 190
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 190:       # ===============================================   190
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key -= {88}
				Bef_Key |= {30}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 191
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 191:       # ===============================================   191
			print("AktionsNr =",Akt_Num)
			if message.note == 30:
				Bef_Key -= {30}
				Bef_Key |= {88}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 192
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 192:       # ===============================================   192
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key -= {88}
				Bef_Key |= {30}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 193
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 193:       # ===============================================   193
			print("AktionsNr =",Akt_Num)
			if message.note == 30:
				Bef_Key -= {30}
				Bef_Key |= {76}
				mn = 95
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 194
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 194:       # ===============================================   194
			print("AktionsNr =",Akt_Num)
			if message.note == 76:
				Bef_Key -= {76}
				Bef_Key |= {93}
				mn = 96
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 195
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 195:       # ===============================================   195
			print("AktionsNr =",Akt_Num)
			if message.note == 93:
				Bef_Key -= {93}
				Bef_Key |= {30}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 196
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 196:       # ===============================================   196
			print("AktionsNr =",Akt_Num)
			if message.note == 30:
				Bef_Key -= {30}
				Bef_Key |= {93}
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 197
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 197:       # ===============================================   197
			print("AktionsNr =",Akt_Num)
			if message.note == 93:
				Bef_Key -= {93}
				Bef_Key |= {45}
				mn = 97
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
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
#mid = MidiFile()
#track = MidiTrack()
#mid.tracks.append(track)




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
		Akt_Num = 122
		print("AktionsNr =",Akt_Num)

		#initializing midi-key flags - list of 100 Befel Keys
		Bef_Key = {}

		#number of Milumin Column
		mn = 51
	
		Bef_Key |= {81}
		#msg = "/action/launchColumn"
		#SENDING OSC MESSAGES
		#client.send_message(msg, mn) 
		#print("msg=",msg,"n=",mn)
		#print("AktNr =",Akt_Num, ' passed',end='')
		Akt_Num = 123
		print(", New AktNr =",Akt_Num)

		BReRun = False
		# Запускаем цикл для обработки онлайн MIDI-сообщений
		while True:
			message = input_port.poll()
			if message:
				process_midi_message(message)
				#if message.type == 'note_on' or message.type == 'note_off':
					#print("message=", message)
					#track.append(mido.Message('note_on', note = message.note, velocity=64, time=64))
					#track.append(mido.Message('note_off', note = message.note, velocity=64, time=128))
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
#mid.save(MIDI_filename+'.mid')
#print("MIDI-file is saved")
#print("E-444444444444444444")


