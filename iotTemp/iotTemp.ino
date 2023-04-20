#include <WiFi.h>
#include <HTTPClient.h>

int temp = 8;
float tempValue;

const char* ssid = "Jamienenz";
const char* = "nenz626666";

void setup() {
  pinMode(temp, INPUT);
  Serial.begin(115200);

  // connect to the wifi
  WiFi.begin(ssid, pwd);
  while(WiFi.status != WL_CONNECTED){
    delay(1000);
    Serial.print("connecting...");
  }
  Serial.print("wifi connected");
}

void loop() {
  tempValue = analogRead(temp);
  if(WiFi.status == WL_CONNECTED){
    
    HTTPClient http;
    http.begin("127.168.0.1/sendData"); // the web endpoint
    http.addHeader("content-type", "text/plain");
    int httpResponse = http.POST(tempValue);

    if(httpResponse > 0){
      String response = getString();
      Serial.print("httpResponse: ");
      Serial.println(httpResponse);
      Serial.print("response: ");
      Serial.println(response);
    }else{
      Serial.println("Error Posting");
      Serial.print("httpResponse: ");
      Serial.println(httpResponse);
    }
    http.end();
  }else{
  Serial.println("Error connecting to wifi");  
  }
 delay(5000); // send data every 5 mins 
}
