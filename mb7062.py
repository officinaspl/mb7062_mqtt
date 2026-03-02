import serial
import time
import paho.mqtt.client as mqtt

# Configurazione porta seriale
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Configurazione MQTT
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'home/sonar/mb7062'

# Connessione MQTT
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Connessione seriale
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
print("Inizio lettura MB7062...")

try:
    while True:
        line = ser.readline().decode('ascii', errors='ignore').strip()
        if line.startswith("R"):
            distanza_mm = int(line[1:])
            distanza_cm = distanza_mm / 10.0
            client.publish(MQTT_TOPIC, f"{distanza_cm:.1f}")
            print(f"Distanza: {distanza_cm:.1f} cm")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Interrotto dall'utente.")
finally:
    ser.close()
    client.disconnect()