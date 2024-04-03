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
MIDI_filename = 'MIDI-P2-' + str(datetime.datetime.now().date()) + '-' + str(datetime.datetime.now().time()).replace(':', '')
MIDI_filename = MIDI_filename.replace('.','')


print("55555555555555")


# Функция для обработки MIDI-сообщений
def process_midi_message(message):
	global mn, Akt_Num, Bef_Key, BExit
	if message.type == 'note_on':
		print(f">>>>>>>>>>>>>>>>>>>>>>>>>>MIDI Note On: {message.note}")
		if Akt_Num == 261:          # ===============================================   261
			print("AktionsNr =",Akt_Num)
			if message.note == 43:
				Bef_Key[43]=False
				Bef_Key[53]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 262
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 262:        # ===============================================   262
			print("AktionsNr =",Akt_Num)
			if message.note == 53:
				Bef_Key[53]=False
				Bef_Key[57]=True
				mn = 123
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 263
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 263:        # ===============================================   263
			print("AktionsNr =",Akt_Num)
			if message.note == 57:
				Bef_Key[57]=False
				Bef_Key[69]=True
				mn = 124
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 264
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 264:        # ===============================================   264
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[74]=True
				mn = 125
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 265
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 265:        # ===============================================   265
			print("AktionsNr =",Akt_Num)
			if message.note == 74:
				Bef_Key[74]=False
				Bef_Key[70]=True
				mn = 126
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 266
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 266:        # ===============================================   266
			print("AktionsNr =",Akt_Num)
			if message.note == 70:
				Bef_Key[70]=False
				Bef_Key[71]=True
				mn = 127
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 267
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 267:        # ===============================================   267
			print("AktionsNr =",Akt_Num)
			if message.note == 71:
				Bef_Key[71]=False
				Bef_Key[76]=True
				mn = 128
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 268
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 268:        # ===============================================   268
			print("AktionsNr =",Akt_Num)
			if message.note == 76:
				Bef_Key[76]=False
				Bef_Key[84]=True
				mn = 129
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 269
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 269:        # ===============================================   269
			print("AktionsNr =",Akt_Num)
			if message.note == 84:
				Bef_Key[84]=False
				Bef_Key[29]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 270
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 270:       # ===============================================   270
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				Bef_Key[29]=False
				Bef_Key[81]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 271
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 271:       # ===============================================   271
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key[81]=False
				Bef_Key[31]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 272
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 272:       # ===============================================   272
			print("AktionsNr =",Akt_Num)
			if message.note == 31:
				Bef_Key[31]=False
				Bef_Key[32]=True
				mn = 130
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 273
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 273:       # ===============================================   273
			print("AktionsNr =",Akt_Num)
			if message.note == 32:
				Bef_Key[32]=False
				Bef_Key[88]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 274
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 274:       # ===============================================   274
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key[88]=False
				Bef_Key[29]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 275
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 275:       # ===============================================   275
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				Bef_Key[29]=False
				Bef_Key[79]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 276
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 276:       # ===============================================   276
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[34]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 277
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 277:       # ===============================================   277
			print("AktionsNr =",Akt_Num)
			if message.note == 34:
				Bef_Key[34]=False
				Bef_Key[60]=True
				mn = 131
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 278
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 278:       # ===============================================   278
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				Bef_Key[60]=False
				Bef_Key[94]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 279
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 279:       # ===============================================   279
			print("AktionsNr =",Akt_Num)
			if message.note == 94:
				Bef_Key[94]=False
				Bef_Key[28]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 280
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 280:       # ===============================================   280
			print("AktionsNr =",Akt_Num)
			if message.note == 28:
				Bef_Key[28]=False
				Bef_Key[29]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 281
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 281:       # ===============================================   281
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				Bef_Key[29]=False
				Bef_Key[70]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 282
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 282:       # ===============================================   282
			print("AktionsNr =",Akt_Num)
			if message.note == 70:
				Bef_Key[70]=False
				Bef_Key[79]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 283
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 283:       # ===============================================   283
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[72]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 284
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 284:       # ===============================================   284
			print("AktionsNr =",Akt_Num)
			if message.note == 72:
				Bef_Key[72]=False
				Bef_Key[60]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 285
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 285:       # ===============================================   285
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				Bef_Key[60]=False
				Bef_Key[62]=True
				mn = 132
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 286
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 286:       # ===============================================   286
			print("AktionsNr =",Akt_Num)
			if message.note == 62:
				Bef_Key[62]=False
				Bef_Key[59]=True
				mn = 133
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 287
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 287:       # ===============================================   287
			print("AktionsNr =",Akt_Num)
			if message.note == 59:
				Bef_Key[59]=False
				Bef_Key[56]=True
				mn = 134
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 288
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 288:       # ===============================================   288
			print("AktionsNr =",Akt_Num)
			if message.note == 56:
				Bef_Key[56]=False
				Bef_Key[57]=True
				mn = 135
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 289
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 289:       # ===============================================   289
			print("AktionsNr =",Akt_Num)
			if message.note == 57:
				Bef_Key[57]=False
				Bef_Key[30]=True
				mn = 136
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 290
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 290:       # ===============================================   290
			print("AktionsNr =",Akt_Num)
			if message.note == 30:
				Bef_Key[30]=False
				Bef_Key[72]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 291
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 291:       # ===============================================   291
			print("AktionsNr =",Akt_Num)
			if message.note == 72:
				Bef_Key[72]=False
				Bef_Key[69]=True
				mn = 137
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 292
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 292:       # ===============================================   292
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[65]=True
				mn = 138
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 293
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 293:       # ===============================================   293
			print("AktionsNr =",Akt_Num)
			if message.note == 65:
				Bef_Key[65]=False
				Bef_Key[74]=True
				mn = 139
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 294
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 294:       # ===============================================   294
			print("AktionsNr =",Akt_Num)
			if message.note == 74:
				Bef_Key[74]=False
				Bef_Key[70]=True
				mn = 140
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 295
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 295:       # ===============================================   295
			print("AktionsNr =",Akt_Num)
			if message.note == 70:
				Bef_Key[70]=False
				Bef_Key[68]=True
				mn = 141
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 296
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 296:       # ===============================================   296
			print("AktionsNr =",Akt_Num)
			if message.note == 68:
				Bef_Key[68]=False
				Bef_Key[69]=True
				mn = 142
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 297
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 297:       # ===============================================   297
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[84]=True
				mn = 143
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 298
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 298:       # ===============================================   298
			print("AktionsNr =",Akt_Num)
			if message.note == 84:
				Bef_Key[84]=False
				Bef_Key[34]=True
				mn = 144
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 299
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 299:       # ===============================================   299
			print("AktionsNr =",Akt_Num)
			if message.note == 34:
				Bef_Key[34]=False
				Bef_Key[29]=True
				mn = 145
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
		mn = 122
	
		Bef_Key[43] = True
		msg = "/action/launchColumn"
		#SENDING OSC MESSAGES
		client.send_message(msg, mn) 
		print("msg=",msg,"n=",mn)
		#print("AktNr =",Akt_Num, ' passed',end='')
		Akt_Num = 261
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


