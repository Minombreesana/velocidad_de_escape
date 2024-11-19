#define LASER 2        // Pin de control para el láser
#define LDR_PIN A0     // Pin de entrada para el LDR

const int threshold = 500; // Umbral para encender/apagar el láser (ajusta este valor según el entorno)

void setup() {
  pinMode(LASER, OUTPUT);       // Configura el pin del láser como salida
  pinMode(LDR_PIN, INPUT);      // Configura el pin del LDR como entrada
  Serial.begin(9600);           // Inicia la comunicación serial (opcional para depuración)
}

void loop() {
  int ldrValue = analogRead(LDR_PIN);  // Lee el valor del LDR
  Serial.println(ldrValue);            // Envía el valor del LDR al monitor serial

  if (ldrValue < threshold) {          // Si el valor está por debajo del umbral
    digitalWrite(LASER, LOW);          // Apaga el láser
  } else {
    digitalWrite(LASER, HIGH);         // Enciende el láser
  }

  delay(50); // Pausa breve para evitar lecturas demasiado rápidas
}
