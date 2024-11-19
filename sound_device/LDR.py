import numpy as np
import sounddevice as sd
import serial

# Configura el puerto serial
ser = serial.Serial('COM5', 9600)

# Parámetros de audio
samplerate = 44100
duration = 0.1  # Reducir la duración del tono

# Función para generar una onda sinusoidal con una frecuencia dada
def generate_tone(frequency, duration, samplerate):
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    return np.sin(2 * np.pi * frequency * t)

while True:
    if ser.in_waiting > 0:  # Si hay datos en el buffer serial
        line = ser.readline().decode('utf-8').rstrip()  # Leer una línea del puerto serial
        try:
            ldr_value = int(line)  # Convertir el valor a número entero
            # Mapear el valor del LDR a una frecuencia
            frequency = max(100, min(2000, ldr_value * 2))
            print(f"LDR Value: {ldr_value}, Frecuencia: {frequency}")
            
            # Generar el tono basado en el valor del LDR
            tone = generate_tone(frequency, duration, samplerate)
            
            # Reproducir el tono sin bloquear
            sd.play(tone, samplerate, blocking=False)
        except ValueError:
            pass  # Ignorar si no se puede convertir a número
