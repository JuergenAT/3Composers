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
MIDI_filename = 'MIDI-B1-' + str(datetime.datetime.now().date()) + '-' + str(datetime.datetime.now().time()).replace(':', '')
MIDI_filename = MIDI_filename.replace('.','')


print("55555555555555")


# Функция для обработки MIDI-сообщений
def process_midi_message(message):
	global mn, Akt_Num, Bef_Key, BExit
	if message.type == 'note_on':
		print(f"MIDI Note On: {message.note}")
		if Akt_Num == 1:          # ===============================================   001
			print("AktionsNr =",Akt_Num)
			Bef_Key[62] = True
			print("AktNr =",Akt_Num, ' passed',end='')
			Akt_Num = 2
			print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 2:        # ===============================================   002
			print("AktionsNr =",Akt_Num)
			if message.note == 62:
				Bef_Key[62]=False
				Bef_Key[79]=True
				mn = 2
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 3
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 3:        # ===============================================   003
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[69]=True
				mn = 3
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 4
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 4:        # ===============================================   004
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[38]=True
				mn = 4
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 5
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 5:        # ===============================================   005
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key[38]=False
				Bef_Key[88]=True
				Bef_Key[51]=True
				mn = 5
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 6
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 6:        # ===============================================   006
			print("AktionsNr =",Akt_Num)
			if message.note == 51:
				Bef_Key[51]=False
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 7
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 7:        # ===============================================   007
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key[88]=False
				Bef_Key[90]=True
				mn = 6
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 8
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 8:        # ===============================================   008
			print("AktionsNr =",Akt_Num)
			if message.note == 90:
				Bef_Key[90]=False
				Bef_Key[88]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 9
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 9:        # ===============================================   009
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key[88]=False
				Bef_Key[87]=True
				Akt_Num = 10
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 10:       # ===============================================   010
			print("AktionsNr =",Akt_Num)
			if message.note == 87:
				Bef_Key[87]=False
				Bef_Key[88]=True
				Akt_Num = 11
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 11:       # ===============================================   011
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key[88]=False
				Bef_Key[52]=True
				Bef_Key[83]=True
				mn = 7
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 12
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 12:       # ===============================================   012
			print("AktionsNr =",Akt_Num)
			if message.note == 52:
				Bef_Key[52]=False
				mn = 8
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 13
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 13:       # ===============================================   013
			print("AktionsNr =",Akt_Num)
			if message.note == 83:
				Bef_Key[83]=False
				Bef_Key[82]=True
				Akt_Num = 14
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 14:       # ===============================================   014
			print("AktionsNr =",Akt_Num)
			if message.note == 82:
				Bef_Key[82]=False
				Bef_Key[35]=True
				mn = 9
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 15
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 15:       # ===============================================   015
			print("AktionsNr =",Akt_Num)
			if message.note == 35:
				Bef_Key[35]=False
				Bef_Key[42]=True
				Akt_Num = 16
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 16:       # ===============================================   016
			print("AktionsNr =",Akt_Num)
			if message.note == 42:
				Bef_Key[42]=False
				Bef_Key[37]=True
				Akt_Num = 17
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 17:       # ===============================================   017
			print("AktionsNr =",Akt_Num)
			if message.note == 37:
				Bef_Key[37]=False
				Bef_Key[80]=True
				Bef_Key[90]=True
				mn = 10
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 18
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 18:       # ===============================================   018
			print("AktionsNr =",Akt_Num)
			if message.note == 80:
				Bef_Key[80]=False
				Bef_Key[68]=True
				mn = 11
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 19
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 19:       # ===============================================   019
			print("AktionsNr =",Akt_Num)
			if message.note == 68:
				Bef_Key[68]=False
				Bef_Key[80]=True
				Akt_Num = 20
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 20:       # ===============================================   020
			print("AktionsNr =",Akt_Num)
			if message.note == 80:
				Bef_Key[80]=False
				Bef_Key[83]=True
				mn = 12
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 21
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 21:       # ===============================================   021
			print("AktionsNr =",Akt_Num)
			if message.note == 83:
				Bef_Key[83]=False
				mn = 13
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 22
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 22:       # ===============================================   022
			print("AktionsNr =",Akt_Num)
			if message.note == 90:
				Bef_Key[90]=False
				Bef_Key[69]=True
				Akt_Num = 23
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 23:       # ===============================================   023
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[62]=True
				Akt_Num = 24
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 24:       # ===============================================   024
			print("AktionsNr =",Akt_Num)
			if message.note == 62:
				Bef_Key[62]=False
				Bef_Key[79]=True
				mn = 14
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 25
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 25:       # ===============================================   025
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[69]=True
				Akt_Num = 26
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 26:       # ===============================================   026
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[38]=True
				Akt_Num = 27
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 27:       # ===============================================   027
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key[38]=False
				Bef_Key[88]=True
				Akt_Num = 28
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 28:       # ===============================================   028
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key[88]=False
				Bef_Key[90]=True
				print("AktNr =",Akt_Num, ' passed', end='')
				Akt_Num = 29
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 29:       # ===============================================   029
			print("AktionsNr =",Akt_Num)
			if message.note == 90:
				Bef_Key[90]=False
				Bef_Key[88]=True
				Akt_Num = 30
			pass
		elif Akt_Num == 30:       # ===============================================   030
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key[88]=False
				Bef_Key[87]=True
				Akt_Num = 31
			pass
		elif Akt_Num == 31:       # ===============================================   031
			print("AktionsNr =",Akt_Num)
			if message.note == 87:
				Bef_Key[87]=False
				Bef_Key[88]=True
				Akt_Num = 32
			pass
		elif Akt_Num == 32:       # ===============================================   032
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key[88]=False
				Bef_Key[52]=True
				Bef_Key[83]=True
				Akt_Num = 33
			pass
		elif Akt_Num == 33:       # ===============================================   033
			print("AktionsNr =",Akt_Num)
			if message.note == 52:
				Bef_Key[52]=False
				Akt_Num = 34
			pass
		elif Akt_Num == 34:       # ===============================================   034
			print("AktionsNr =",Akt_Num)
			if message.note == 83:
				Bef_Key[83]=False
				Bef_Key[82]=True
				Akt_Num = 35
			pass
		elif Akt_Num == 35:       # ===============================================   035
			print("AktionsNr =",Akt_Num)
			if message.note == 82:
				Bef_Key[82]=False
				Bef_Key[35]=True
				Akt_Num = 36
			pass
		elif Akt_Num == 36:       # ===============================================   036
			print("AktionsNr =",Akt_Num)
			if message.note == 35:
				Bef_Key[35]=False
				Bef_Key[42]=True
				Akt_Num = 37
			pass
		elif Akt_Num == 37:       # ===============================================   037
			print("AktionsNr =",Akt_Num)
			if message.note == 42:
				Bef_Key[42]=False
				Bef_Key[37]=True
				Akt_Num = 38
			pass
		elif Akt_Num == 38:       # ===============================================   038
			print("AktionsNr =",Akt_Num)
			if message.note == 37:
				Bef_Key[37]=False
				Bef_Key[90]=True
				Akt_Num = 39
			pass
		elif Akt_Num == 39:       # ===============================================   039
			print("AktionsNr =",Akt_Num)
			if message.note == 90:
				Bef_Key[90]=False
				Bef_Key[69]=True
				Akt_Num = 40
			pass
		elif Akt_Num == 40:       # ===============================================   040
			print("AktionsNr =",Akt_Num)
			if message.note == 69:
				Bef_Key[69]=False
				Bef_Key[81]=True
				Akt_Num = 41
			pass
		elif Akt_Num == 41:       # ===============================================   041
			print("AktionsNr =",Akt_Num)
			if message.note == 81:
				Bef_Key[81]=False
				Bef_Key[86]=True
				mn = 15
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 42
			pass
		elif Akt_Num == 42:       # ===============================================   042
			print("AktionsNr =",Akt_Num)
			if message.note == 86:
				Bef_Key[86]=False
				Bef_Key[88]=True
				mn = 16
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 43
			pass
		elif Akt_Num == 43:       # ===============================================   043
			print("AktionsNr =",Akt_Num)
			if message.note == 88:
				Bef_Key[88]=False
				Bef_Key[62]=True
				Akt_Num = 44
			pass
		elif Akt_Num == 44:       # ===============================================   044
			print("AktionsNr =",Akt_Num)
			if message.note == 62:
				Bef_Key[62]=False
				Bef_Key[57]=True
				Akt_Num = 45
			pass
		elif Akt_Num == 45:       # ===============================================   045
			print("AktionsNr =",Akt_Num)
			if message.note == 57:
				Bef_Key[57]=False
				Bef_Key[62]=True
				Akt_Num = 46
			pass
		elif Akt_Num == 46:       # ===============================================   046
			print("AktionsNr =",Akt_Num)
			if message.note == 62:
				Bef_Key[62]=False
				Bef_Key[93]=True
				Akt_Num = 47
			pass
		elif Akt_Num == 47:       # ===============================================   047
			print("AktionsNr =",Akt_Num)
			if message.note == 93:
				Bef_Key[93]=False
				Bef_Key[91]=True
				Akt_Num = 48
			pass
		elif Akt_Num == 48:       # ===============================================   048
			print("AktionsNr =",Akt_Num)
			if message.note == 91:
				Bef_Key[91]=False
				Bef_Key[60]=True
				Akt_Num = 49
			pass
		elif Akt_Num == 49:       # ===============================================   049
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				Bef_Key[60]=False
				Bef_Key[93]=True
				Akt_Num = 50
			pass
		elif Akt_Num == 50:       # ===============================================   050
			print("AktionsNr =",Akt_Num)
			if message.note == 93:
				Bef_Key[93]=False
				Bef_Key[83]=True
				Akt_Num = 51
			pass
		elif Akt_Num == 51:       # ===============================================   051
			print("AktionsNr =",Akt_Num)
			if message.note == 83:
				Bef_Key[83]=False
				Bef_Key[91]=True
				Akt_Num = 52
			pass
		elif Akt_Num == 52:       # ===============================================   052
			print("AktionsNr =",Akt_Num)
			if message.note == 91:
				Bef_Key[91]=False
				Bef_Key[42]=True
				mn = 17
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 53
			pass
		elif Akt_Num == 53:       # ===============================================   053
			print("AktionsNr =",Akt_Num)
			if message.note == 42:
				Bef_Key[42]=False
				Bef_Key[37]=True
				mn = 18
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 54
			pass
		elif Akt_Num == 54:       # ===============================================   054
			print("AktionsNr =",Akt_Num)
			if message.note == 37:
				Bef_Key[37]=False
				Bef_Key[59]=True
				Akt_Num = 55
			pass
		elif Akt_Num == 55:       # ===============================================   055
			print("AktionsNr =",Akt_Num)
			if message.note == 59:
				Bef_Key[59]=False
				Bef_Key[79]=True
				mn = 19
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 56
			pass
		elif Akt_Num == 56:       # ===============================================   056
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[60]=True
				mn = 20
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 57
			pass
		elif Akt_Num == 57:       # ===============================================   057
			print("AktionsNr =",Akt_Num)
			if message.note == 60:
				Bef_Key[60]=False
				Bef_Key[79]=True
				mn = 21
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 58
			pass
		elif Akt_Num == 58:       # ===============================================   058
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[86]=True
				mn = 22
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				Akt_Num = 59
			pass
		elif Akt_Num == 59:       # ===============================================   059
			print("AktionsNr =",Akt_Num)
			if message.note == 86:
				Bef_Key[86]=False
				Bef_Key[85]=True
				Akt_Num = 60
			pass
		elif Akt_Num == 60:       # ===============================================   060
			print("AktionsNr =",Akt_Num)
			if message.note == 85:
				Bef_Key[85]=False
				BExit = True
				#Bef_Key[86]=True
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
		Akt_Num = 1
		print("AktionsNr =",Akt_Num)

		#initializing midi-key flags - list of 100 Befel Keys
		Bef_Key = [False]*100

		#number of Milumin Column
		mn = 0

		Bef_Key[62] = True
		Akt_Num = 2

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


