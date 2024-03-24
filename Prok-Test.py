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
				#track.append(message)
				#track.append(message)
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

			time.sleep(0.05)
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


