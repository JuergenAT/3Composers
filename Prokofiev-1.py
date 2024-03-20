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
		if Akt_Num == 123:          # ===============================================   123
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key[81]=False
				Bef_Key[50]=True
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
			
			pass
		elif Akt_Num == 125:        # ===============================================   125
			
			pass
		elif Akt_Num == 126:        # ===============================================   126
		
			pass
		elif Akt_Num == 127:        # ===============================================   127
			
			pass
		elif Akt_Num == 128:        # ===============================================   128
		
			pass
		elif Akt_Num == 129:        # ===============================================   129
			
			pass
		elif Akt_Num == 130:        # ===============================================   130
		
			pass
		elif Akt_Num == 131:        # ===============================================   131
			
			pass
		elif Akt_Num == 132:       # ===============================================   132
		
			pass
		elif Akt_Num == 133:       # ===============================================   133
			
			pass
		elif Akt_Num == 134:       # ===============================================   134
		
			pass
		elif Akt_Num == 135:       # ===============================================   135
		
			pass
		elif Akt_Num == 136:       # ===============================================   136
			
			pass
		elif Akt_Num == 137:       # ===============================================   137
		
			pass
		elif Akt_Num == 138:       # ===============================================   138
			
			pass
		elif Akt_Num == 139:       # ===============================================   139
			
			pass
		elif Akt_Num == 140:       # ===============================================   140
		
			pass
		elif Akt_Num == 141:       # ===============================================   141
		
			pass
		elif Akt_Num == 142:       # ===============================================   142
			
			pass
		elif Akt_Num == 143:       # ===============================================   143
		
			pass
		elif Akt_Num == 144:       # ===============================================   144
		
			pass
		elif Akt_Num == 145:       # ===============================================   145
		
			pass
		elif Akt_Num == 146:       # ===============================================   146
			
			pass
		elif Akt_Num == 147:       # ===============================================   147
		
			pass
		elif Akt_Num == 148:       # ===============================================   148
		
			pass
		elif Akt_Num == 149:       # ===============================================   149
			
			pass
		elif Akt_Num == 150:       # ===============================================   150
			
			pass
		elif Akt_Num == 151:       # ===============================================   151
			
			pass
		elif Akt_Num == 15101:       # ===============================================   15101
		
			pass
		elif Akt_Num == 15102:       # ===============================================   15102
		
			pass
		elif Akt_Num == 15103:       # ===============================================   15103
		
			pass
		elif Akt_Num == 152:       # ===============================================   152
		
			pass
		elif Akt_Num == 153:       # ===============================================   153
			
			pass
		elif Akt_Num == 154:       # ===============================================   154
		
			pass
		elif Akt_Num == 155:       # ===============================================   155
			
			pass
		elif Akt_Num == 156:       # ===============================================   156
		
			pass
		elif Akt_Num == 157:       # ===============================================   157
			
			pass
		elif Akt_Num == 158:       # ===============================================   158
		
			pass
		elif Akt_Num == 159:       # ===============================================   159
			
			pass
		elif Akt_Num == 160:       # ===============================================   160
		
			pass
		elif Akt_Num == 161:       # ===============================================   161
			
			pass
		elif Akt_Num == 162:       # ===============================================   162
		
			pass
		elif Akt_Num == 163:       # ===============================================   163
		
			pass
		elif Akt_Num == 164:       # ===============================================   164
		
			pass
		elif Akt_Num == 165:       # ===============================================   165
		
			pass
		elif Akt_Num == 166:       # ===============================================   166
		
			pass
		elif Akt_Num == 167:       # ===============================================   167
			
			pass
		elif Akt_Num == 168:       # ===============================================   168
		
			pass
		elif Akt_Num == 169:       # ===============================================   169
		
			pass
		elif Akt_Num == 170:       # ===============================================   170
			
			pass
		elif Akt_Num == 171:       # ===============================================   171
		
			pass
		elif Akt_Num == 172:       # ===============================================   172
			
			pass
		elif Akt_Num == 173:       # ===============================================   173
			
			pass
		elif Akt_Num == 174:       # ===============================================   174
		
			pass
		elif Akt_Num == 175:       # ===============================================   175
		
			pass
		elif Akt_Num == 176:       # ===============================================   176
		
			pass
		elif Akt_Num == 177:       # ===============================================   177
			
			pass
		elif Akt_Num == 178:       # ===============================================   178
		
			pass
		elif Akt_Num == 179:       # ===============================================   179
			
			pass
		elif Akt_Num == 180:       # ===============================================   180
			
			pass
		elif Akt_Num == 181:       # ===============================================   181
			
			pass
		elif Akt_Num == 182:       # ===============================================   182
		
			pass
		elif Akt_Num == 183:       # ===============================================   183
			
			pass
		elif Akt_Num == 18301:       # ===============================================   18301
		
			pass	
		elif Akt_Num == 184:       # ===============================================   184
		
			pass
		elif Akt_Num == 185:       # ===============================================   185
			
			pass
		elif Akt_Num == 186:       # ===============================================   186
		
			pass
		elif Akt_Num == 187:       # ===============================================   187
		
			pass
		elif Akt_Num == 188:       # ===============================================   188
		
			pass
		elif Akt_Num == 189:       # ===============================================   189
			
			pass
		elif Akt_Num == 190:       # ===============================================   190
		
			pass
		elif Akt_Num == 191:       # ===============================================   191
			
			pass
		elif Akt_Num == 192:       # ===============================================   192
			
			pass
		elif Akt_Num == 193:       # ===============================================   193
		
			pass
		elif Akt_Num == 194:       # ===============================================   194
			
			pass
		elif Akt_Num == 195:       # ===============================================   195
			
			pass
		elif Akt_Num == 196:       # ===============================================   196
		
			pass
		elif Akt_Num == 197:       # ===============================================   197
			
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


