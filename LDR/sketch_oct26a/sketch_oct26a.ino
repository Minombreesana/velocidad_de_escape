const int ldrPin = A0;  // Pin analógico donde está conectado el LDR

void setup() {
  Serial.begin(9600);  // Inicializar la comunicación serial a 9600 baudios
}

void loop() {
  int ldrValue = analogRead(ldrPin);  // Leer el valor del LDR
  Serial.println(ldrValue);           // Enviar el valor por el puerto serial
  delay(500);                         // Pausa entre lecturas
}