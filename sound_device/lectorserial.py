import numpy as np
import sounddevice as sd
import serial

# Configura el puerto serial (cambia 'COM5' según tu sistema)
ser = serial.Serial('COM5', 9600)  # En Windows, usa 'COMx'. En Linux/macOS, usa '/dev/ttyUSBx'

# Parámetros de audio
samplerate = 44100  # Frecuencia de muestreo
duration = 0.4     # Duración del tono en segundos

# Función para generar una onda sinusoidal con una frecuencia dada
def generate_tone(frequency, duration, samplerate):
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    return np.sin(2 * np.pi * frequency * t)

while True:
    if ser.in_waiting > 0:  # Si hay datos en el buffer serial
        line = ser.readline().decode('utf-8').rstrip()  # Leer una línea del puerto serial
        try:
            distance = float(line)  # Convertir el valor a número
            frequency = max(50, min(4000, distance * 10))  # Mapear la distancia a una frecuencia
            print(f"Distancia: {distance}, Frecuencia: {frequency}")
            
            # Generar el tono basado en la distancia
            tone = generate_tone(frequency, duration, samplerate)
            
            # Reproducir el tono
            sd.play(tone, samplerate)
            sd.wait()  # Esperar hasta que el audio termine
        except ValueError:
            pass  # Ignorar si no se puede convertir a número