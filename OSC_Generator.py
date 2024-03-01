import time
import mido
import keyboard
from pythonosc.udp_client import SimpleUDPClient


#initializing ip, port for OSC-commands
ip = "127.0.0.1"
port = 5000

client = SimpleUDPClient(ip, port)  # Create client


#initializing m-key flags

#initialize command Nr



"""
client.send_message("/some/address", 123)   # Send float message
client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string
"""


# Идентификатор инструмента для отслеживания (замените на нужное значение)
TARGET_INSTRUMENT = 0

# Функция для обработки MIDI-сообщений
def process_midi_message(message):
    if message.type == 'note_on' and message.channel == TARGET_INSTRUMENT:
        print(f"MIDI Note On: {message.note}")
    elif message.type == 'note_off' and message.channel == TARGET_INSTRUMENT:
        print(f"MIDI Note Off: {message.note}")
    # Другие проверки, если необходимо

# Функция для обработки событий клавиатуры
def process_keyboard_event(event):
    print(f"Keyboard: {event.name}")

# Открываем виртуальный MIDI-вход для чтения сообщений
input_port = mido.open_input('VirtualMIDISynth Port 1')  # Замените на имя вашего виртуального MIDI-устройства








#number of Milumin Column
mn = 0


#SENDING OSC MESSAGES
# Запускаем цикл для обработки онлайн MIDI-сообщений
try:
	for message in input_port:
		process_midi_message(message)

		# Проверяем события клавиатуры при каждом MIDI-сообщении
		if keyboard.is_pressed('q'):
			print("Exit requested. Stopping...")
			break
        
	mn += 1
	msg = "/action/launchColumn"
	client.send_message(msg, mn) 
	print("msg=",msg,"n=",mn)
	#time.sleep(3)
        
except KeyboardInterrupt :
	pass     

finally:
	print ("\nClosing OSCClient")
	#close OSC-port
	client.close()
	print ("Done. Closing MIDI-port")
	input_port.close()  # Важно закрыть порт после использования
	print ("\nMIDI-port closed")


