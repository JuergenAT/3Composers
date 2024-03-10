import time
import mido
from pynput import keyboard
from pythonosc.udp_client import SimpleUDPClient


#initializing ip, port for OSC-commands
ip = "127.0.0.1"
port = 5000


client = SimpleUDPClient(ip, port)  # Create client

#initializing midi-key flags

#initialize command Nr



"""
client.send_message("/some/address", 123)   # Send float message
client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string
"""


# Идентификатор инструмента для отслеживания (замените на нужное значение)
# TARGET_INSTRUMENT = 0

print("44444444444444")

# Функция для обработки MIDI-сообщений
def process_midi_message(message):
    #if message.type == 'note_on' and message.channel == TARGET_INSTRUMENT:
	if message.type == 'note_on':
		print(f"MIDI Note On: {message.note}")
	#elif message.type == 'note_off' and message.channel == TARGET_INSTRUMENT:
		#print(f"MIDI Note Off: {message.note}")
    # Другие проверки, если необходимо

# Функция для обработки событий клавиатуры
def on_key_press(key):
    try:
        print(f"Key {key.char} pressed")
    except AttributeError:
        print(f"Special key {key} pressed")



print("555555555555555")

#To get a list of available ports
port_List = mido.get_output_names()
print("MIDI-Ports available:", port_List)

print("666666666666666")

# Открываем виртуальный MIDI-вход для чтения сообщений
input_port = mido.open_input(port_List[0])  # Замените на имя вашего MIDI-устройства


print("777777777777")


#number of Milumin Column
mn = 0


print("8888888888888")

with keyboard.Listener(on_press=on_key_press) as listener:
#try:
	print("99999999999")
# Запускаем цикл для обработки онлайн MIDI-сообщений
	while True:
		message = input_port.poll()
		if message:
			process_midi_message(message)
			mn += 1
			msg = "/action/launchColumn"
			#SENDING OSC MESSAGES
			client.send_message(msg, mn) 
			print("msg=",msg,"n=",mn)
		#else:
			#print("mn=",mn)
			
		

		time.sleep(0.1)
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
print ("Closing MIDI-port")
input_port.close()  # Важно закрыть порт после использования
print ("\nMIDI-port closed")


