// Emre Guzel
// March 24, 2026
// Sonar program

// Setting the pins 
const int trigPin = 3;
const int echoPin = 2;

// Setting the distance 
float duration, distance;

// Setting the pin modes and speed
void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

// Setting the loop for delays after working   
void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Setting the calculations 
  duration = pulseIn(echoPin, HIGH);
  distance = (duration * 0.0343) / 2;
  
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(100);
}