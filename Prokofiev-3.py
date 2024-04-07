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
#MIDI_filename = 'MIDI-P3-' + str(datetime.datetime.now().date()) + '-' + str(datetime.datetime.now().time()).replace(':', '')
#MIDI_filename = MIDI_filename.replace('.','')


print("55555555555555")


# Функция для обработки MIDI-сообщений
def process_midi_message(message):
	global mn, Akt_Num, Bef_Key, BExit
	if message.type == 'note_on':
		print(f">>>>>>>>>>>>>>>>>>>>>>>>>>MIDI Note On: {message.note}")
		if Akt_Num == 304:          # ===============================================   304
			print("AktionsNr =",Akt_Num)
			if message.note == 36:
				Bef_Key[36]=False
				Bef_Key[91]=True
				mn = 147
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 305
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 305:        # ===============================================   305
			print("AktionsNr =",Akt_Num)
			if message.note == 91:
				Bef_Key[91]=False
				Bef_Key[51]=True
				mn = 148
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 306
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 306:        # ===============================================   306
			print("AktionsNr =",Akt_Num)
			if message.note == 51:
				Bef_Key[51]=False
				Bef_Key[77]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 307
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 307:        # ===============================================   307
			print("AktionsNr =",Akt_Num)
			if message.note == 77:
				Bef_Key[77]=False
				Bef_Key[37]=True
				mn = 149
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 308
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 308:        # ===============================================   308
			print("AktionsNr =",Akt_Num)
			if message.note == 37:
				Bef_Key[37]=False
				Bef_Key[52]=True
				mn = 150
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 309
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 309:        # ===============================================   309
			print("AktionsNr =",Akt_Num)
			if message.note == 52:
				Bef_Key[52]=False
				Bef_Key[58]=True
				mn = 151
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 310
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 310:        # ===============================================   310
			print("AktionsNr =",Akt_Num)
			if message.note == 58:
				Bef_Key[58]=False
				Bef_Key[91]=True
				mn = 152
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 311
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 311:        # ===============================================   311
			print("AktionsNr =",Akt_Num)
			if message.note == 91:
				Bef_Key[91]=False
				Bef_Key[87]=True
				mn = 153
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 312
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 312:        # ===============================================   312
			print("AktionsNr =",Akt_Num)
			if message.note == 87:
				Bef_Key[87]=False
				Bef_Key[89]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 313
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 313:       # ===============================================   313
			print("AktionsNr =",Akt_Num)
			if message.note == 89:
				Bef_Key[89]=False
				Bef_Key[96]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 314
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 314:       # ===============================================   314
			print("AktionsNr =",Akt_Num)
			if message.note == 96:
				Bef_Key[96]=False
				Bef_Key[35]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 315
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 315:       # ===============================================   315
			print("AktionsNr =",Akt_Num)
			if message.note == 35:
				Bef_Key[35]=False
				Bef_Key[92]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 316
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 316:       # ===============================================   316
			print("AktionsNr =",Akt_Num)
			if message.note == 92:
				Bef_Key[92]=False
				Bef_Key[82]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 317
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 317:       # ===============================================   317
			print("AktionsNr =",Akt_Num)
			if message.note == 82:
				Bef_Key[82]=False
				Bef_Key[73]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 318
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 318:       # ===============================================   318
			print("AktionsNr =",Akt_Num)
			if message.note == 73:
				Bef_Key[73]=False
				Bef_Key[37]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 319
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 319:       # ===============================================   319
			print("AktionsNr =",Akt_Num)
			if message.note == 37:
				Bef_Key[37]=False
				Bef_Key[44]=True
				mn = 154
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 320
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 320:       # ===============================================   320
			print("AktionsNr =",Akt_Num)
			if message.note == 44:
				Bef_Key[44]=False
				Bef_Key[46]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 321
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 321:       # ===============================================   321
			print("AktionsNr =",Akt_Num)
			if message.note == 46:
				Bef_Key[46]=False
				Bef_Key[70]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 322
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 322:       # ===============================================   322
			print("AktionsNr =",Akt_Num)
			if message.note == 70:
				Bef_Key[70]=False
				Bef_Key[44]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 323
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 323:       # ===============================================   323
			print("AktionsNr =",Akt_Num)
			if message.note == 44:
				Bef_Key[44]=False
				Bef_Key[46]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 324
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 324:       # ===============================================   324
			print("AktionsNr =",Akt_Num)
			if message.note == 46:
				Bef_Key[46]=False
				Bef_Key[82]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 325
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 325:       # ===============================================   325
			print("AktionsNr =",Akt_Num)
			if message.note == 82:
				Bef_Key[82]=False
				Bef_Key[64]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 326
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 326:       # ===============================================   326
			print("AktionsNr =",Akt_Num)
			if message.note == 64:
				Bef_Key[64]=False
				Bef_Key[85]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 327
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 327:       # ===============================================   327
			print("AktionsNr =",Akt_Num)
			if message.note == 85:
				Bef_Key[85]=False
				Bef_Key[37]=True
				mn = 155
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 328
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 328:       # ===============================================   328
			print("AktionsNr =",Akt_Num)
			if message.note == 37:
				Bef_Key[37]=False
				Bef_Key[93]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 329
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 329:       # ===============================================   329
			print("AktionsNr =",Akt_Num)
			if message.note == 93:
				Bef_Key[93]=False
				Bef_Key[33]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 330
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 330:       # ===============================================   330
			print("AktionsNr =",Akt_Num)
			if message.note == 33:
				Bef_Key[33]=False
				Bef_Key[38]=True
				mn = 156
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 331
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 331:       # ===============================================   331
			print("AktionsNr =",Akt_Num)
			if message.note == 38:
				Bef_Key[38]=False
				Bef_Key[33]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 332
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 332:       # ===============================================   332
			print("AktionsNr =",Akt_Num)
			if message.note == 33:
				Bef_Key[33]=False
				Bef_Key[61]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 333
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 333:       # ===============================================   333
			print("AktionsNr =",Akt_Num)
			if message.note == 61:
				Bef_Key[61]=False
				Bef_Key[62]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 334
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 334:       # ===============================================   334
			print("AktionsNr =",Akt_Num)
			if message.note == 62:
				Bef_Key[62]=False
				Bef_Key[72]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 335
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 335:       # ===============================================   335
			print("AktionsNr =",Akt_Num)
			if message.note == 72:
				Bef_Key[72]=False
				Bef_Key[36]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 336
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 336:       # ===============================================   336
			print("AktionsNr =",Akt_Num)
			if message.note == 36:
				Bef_Key[36]=False
				Bef_Key[41]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 337
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 337:       # ===============================================   337
			print("AktionsNr =",Akt_Num)
			if message.note == 41:
				Bef_Key[41]=False
				Bef_Key[36]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 338
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 338:       # ===============================================   338
			print("AktionsNr =",Akt_Num)
			if message.note == 36:
				Bef_Key[36]=False
				Bef_Key[41]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 339
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 339:       # ===============================================   339
			print("AktionsNr =",Akt_Num)
			if message.note == 41:
				Bef_Key[41]=False
				Bef_Key[36]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 340
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 340:       # ===============================================   340
			print("AktionsNr =",Akt_Num)
			if message.note == 36:
				Bef_Key[36]=False
				Bef_Key[29]=True
				mn = 157
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 341
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 341:       # ===============================================   341
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				mn = 158
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 342
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 342:       # ===============================================   342
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 343
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 343:       # ===============================================   343
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 344
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 344:       # ===============================================   344
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 345
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 345:       # ===============================================   345
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 346
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 346:       # ===============================================   346
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 347
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 347:       # ===============================================   347
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				Bef_Key[29]=False
				Bef_Key[37]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34701
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34701:       # ===============================================   34701
			print("AktionsNr =",Akt_Num)
			if message.note == 37:
				Bef_Key[37]=False
				Bef_Key[39]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34702
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34702:       # ===============================================   34702
			print("AktionsNr =",Akt_Num)
			if message.note == 39:
				Bef_Key[39]=False
				Bef_Key[44]=True
				mn = 159
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34703
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34703:       # ===============================================   34703
			print("AktionsNr =",Akt_Num)
			if message.note == 44:
				Bef_Key[44]=False
				Bef_Key[46]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34704
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34704:       # ===============================================   34704
			print("AktionsNr =",Akt_Num)
			if message.note == 46:
				Bef_Key[46]=False
				Bef_Key[44]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34705
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34705:       # ===============================================   34705
			print("AktionsNr =",Akt_Num)
			if message.note == 44:
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34706
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34706:       # ===============================================   34706
			print("AktionsNr =",Akt_Num)
			if message.note == 44:
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34707
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34707:       # ===============================================   34707
			print("AktionsNr =",Akt_Num)
			if message.note == 44:
				mn = 160
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34708
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34708:       # ===============================================   34708
			print("AktionsNr =",Akt_Num)
			if message.note == 44:
				Bef_Key[44]=False
				Bef_Key[46]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34709
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34709:       # ===============================================   34709
			print("AktionsNr =",Akt_Num)
			if message.note == 46:
				Bef_Key[46]=False
				Bef_Key[44]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34710
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34710:       # ===============================================   34710
			print("AktionsNr =",Akt_Num)
			if message.note == 44:
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34711
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34711:       # ===============================================   34711
			print("AktionsNr =",Akt_Num)
			if message.note == 44:
				Bef_Key[44]=False
				Bef_Key[53]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34712
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34712:       # ===============================================   34712
			print("AktionsNr =",Akt_Num)
			if message.note == 53:
				Bef_Key[53]=False
				Bef_Key[72]=True
				mn = 161
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 348
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 348:       # ===============================================   348
			print("AktionsNr =",Akt_Num)
			if message.note == 72:
				Bef_Key[72]=False
				Bef_Key[51]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 34801
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 34801:       # ===============================================   34801
			print("AktionsNr =",Akt_Num)
			if message.note == 51:
				Bef_Key[51]=False
				Bef_Key[29]=True
				mn = 162
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 349
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 349:       # ===============================================   349
			print("AktionsNr =",Akt_Num)
			if message.note == 29:
				Bef_Key[29]=False
				Bef_Key[86]=True
				mn = 163
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 350
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 350:       # ===============================================   350
			print("AktionsNr =",Akt_Num)
			if message.note == 86:
				Bef_Key[86]=False
				Bef_Key[85]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 351
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 351:       # ===============================================   351
			print("AktionsNr =",Akt_Num)
			if message.note == 85:
				Bef_Key[85]=False
				Bef_Key[36]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 352
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 352:       # ===============================================   352
			print("AktionsNr =",Akt_Num)
			if message.note == 36:
				Bef_Key[36]=False
				Bef_Key[67]=True
				mn = 164
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 353
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 353:       # ===============================================   353
			print("AktionsNr =",Akt_Num)
			if message.note == 67:
				Bef_Key[67]=False
				Bef_Key[86]=True
				mn = 165
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 354
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 354:       # ===============================================   354
			print("AktionsNr =",Akt_Num)
			if message.note == 86:
				Bef_Key[86]=False
				Bef_Key[91]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 365
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 365:       # ===============================================   365
			print("AktionsNr =",Akt_Num)
			if message.note == 91:
				Bef_Key[91]=False
				Bef_Key[86]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 366
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 366:       # ===============================================   366
			print("AktionsNr =",Akt_Num)
			if message.note == 86:
				Bef_Key[86]=False
				Bef_Key[77]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 367
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 367:       # ===============================================   367
			print("AktionsNr =",Akt_Num)
			if message.note == 77:
				Bef_Key[77]=False
				Bef_Key[74]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 374
				print(", New AktNr =",Akt_Num)
			pass
		#elif Akt_Num == 368:       # ===============================================   368
		#	print("AktionsNr =",Akt_Num)
		#	if message.note == 74:
		#		Bef_Key[74]=False
		#		Bef_Key[86]=True
		#		print("AktNr =",Akt_Num, ' passed',end='')
		#		Akt_Num = 369
		#		print(", New AktNr =",Akt_Num)
		#	pass
		#elif Akt_Num == 369:       # ===============================================   369
		#	print("AktionsNr =",Akt_Num)
		#	if message.note == 86:
		#		Bef_Key[86]=False
		#		Bef_Key[89]=True
		#		print("AktNr =",Akt_Num, ' passed',end='')
		#		Akt_Num = 370
		#		print(", New AktNr =",Akt_Num)
		#	pass
		#elif Akt_Num == 370:       # ===============================================   370
		#	print("AktionsNr =",Akt_Num)
		#	if message.note == 89:
		#		Bef_Key[89]=False
		#		Bef_Key[74]=True
		#		print("AktNr =",Akt_Num, ' passed',end='')
		#		Akt_Num = 371
		#		print(", New AktNr =",Akt_Num)
		#	pass
		#elif Akt_Num == 371:       # ===============================================   371
		#	print("AktionsNr =",Akt_Num)
		#	if message.note == 74:
		#		Bef_Key[74]=False
		#		Bef_Key[86]=True
		#		print("AktNr =",Akt_Num, ' passed',end='')
		#		Akt_Num = 372
		#		print(", New AktNr =",Akt_Num)
		#	pass
		#elif Akt_Num == 372:       # ===============================================   372
		#	print("AktionsNr =",Akt_Num)
		#	if message.note == 86:
		#		Bef_Key[86]=False
		#		Bef_Key[89]=True
		#		print("AktNr =",Akt_Num, ' passed',end='')
		#		Akt_Num = 373
		#		print(", New AktNr =",Akt_Num)
		#	pass
		#elif Akt_Num == 373:       # ===============================================   373
		#	print("AktionsNr =",Akt_Num)
		#	if message.note == 89:
		#		Bef_Key[89]=False
		#		Bef_Key[74]=True
		#		print("AktNr =",Akt_Num, ' passed',end='')
		#		Akt_Num = 374
		#		print(", New AktNr =",Akt_Num)
		#	pass
		elif Akt_Num == 374:       # ===============================================   374
			print("AktionsNr =",Akt_Num)
			if message.note == 74:
				Bef_Key[74]=False
				Bef_Key[84]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 375
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 375:       # ===============================================   375
			print("AktionsNr =",Akt_Num)
			if message.note == 84:
				Bef_Key[84]=False
				Bef_Key[86]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 376
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 376:       # ===============================================   376
			print("AktionsNr =",Akt_Num)
			if message.note == 86:
				Bef_Key[86]=False
				Bef_Key[75]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 377
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 377:       # ===============================================   377
			print("AktionsNr =",Akt_Num)
			if message.note == 75:
				Bef_Key[75]=False
				Bef_Key[79]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 378
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 378:       # ===============================================   378
			print("AktionsNr =",Akt_Num)
			if message.note == 79:
				Bef_Key[79]=False
				Bef_Key[77]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 379
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 379:       # ===============================================   379
			print("AktionsNr =",Akt_Num)
			if message.note == 77:
				Bef_Key[77]=False
				Bef_Key[74]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 380
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 380:       # ===============================================   380
			print("AktionsNr =",Akt_Num)
			if message.note == 74:
				Bef_Key[74]=False
				Bef_Key[51]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 381
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 381:       # ===============================================   381
			print("AktionsNr =",Akt_Num)
			if message.note == 51:
				Bef_Key[51]=False
				Bef_Key[70]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 382
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 382:       # ===============================================   382
			print("AktionsNr =",Akt_Num)
			if message.note == 70:
				Bef_Key[70]=False
				Bef_Key[50]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 383
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 383:       # ===============================================   383
			print("AktionsNr =",Akt_Num)
			if message.note == 50:
				Bef_Key[50]=False
				Bef_Key[24]=True
				mn = 166
				msg = "/action/launchColumn"
				#SENDING OSC MESSAGES
				client.send_message(msg, mn) 
				print("msg=",msg,"n=",mn)
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 384
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 384:       # ===============================================   384
			print("AktionsNr =",Akt_Num)
			if message.note == 24:
				Bef_Key[24]=False
				Bef_Key[97]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 385
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 385:       # ===============================================   385
			print("AktionsNr =",Akt_Num)
			if message.note == 97:
				Bef_Key[97]=False
				Bef_Key[24]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 386
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 386:       # ===============================================   386
			print("AktionsNr =",Akt_Num)
			if message.note == 24:
				Bef_Key[24]=False
				Bef_Key[72]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 387
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 387:       # ===============================================   387
			print("AktionsNr =",Akt_Num)
			if message.note == 72:
				Bef_Key[72]=False
				Bef_Key[48]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 388
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 388:       # ===============================================   388
			print("AktionsNr =",Akt_Num)
			if message.note == 48:
				Bef_Key[48]=False
				Bef_Key[24]=True
				print("AktNr =",Akt_Num, ' passed',end='')
				Akt_Num = 399
				print(", New AktNr =",Akt_Num)
			pass
		elif Akt_Num == 399:       # ===============================================   399
			print("AktionsNr =",Akt_Num)
			if message.note == 24:
				Bef_Key[24]=False
				mn = 167
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
		#Akt_Num = 197
		#print("AktionsNr =",Akt_Num)

		#initializing midi-key flags - list of 100 Befel Keys
		Bef_Key = [False]*100

		#number of Milumin Column
		mn = 146
	
		Bef_Key[36] = True
		msg = "/action/launchColumn"
		#SENDING OSC MESSAGES
		client.send_message(msg, mn) 
		print("msg=",msg,"n=",mn)
		#print("AktNr =",Akt_Num, ' passed',end='')
		Akt_Num = 304
		print(", New AktNr =",Akt_Num)

		BReRun = False
		# Запускаем цикл для обработки онлайн MIDI-сообщений
		while True:
			message = input_port.poll()
			if message:
				#track.append(message)
				process_midi_message(message)
				#if message.type == 'note_on' or message.type == 'note_off':
					#print("message=", message)
					#track.append(mido.Message('note_on', note = message.note, velocity=64, time=64))
					#track.append(mido.Message('note_off', note = message.note, velocity=64, time=128))
				#	pass
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


