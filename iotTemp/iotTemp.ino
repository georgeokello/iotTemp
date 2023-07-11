#include <WiFi.h>
#include <HTTPClient.h>

int temp = 8;
float tempValue;

const char* ssid = "Jamienenz";
const char* pwd = "nenz626666";

const char* serverUrl = "http://django-server-address/";
const char* endpoint = "receiveData/";
const char* token = "iot_token";

void setup() {
  pinMode(temp, INPUT);
  Serial.begin(115200);

  // connect to the wifi
  WiFi.begin(ssid, pwd);
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.print(".");
  }
  Serial.print("Connected to wifi");
}

void loop() {
  tempValue = analogRead(temp);
  
  if(WiFi.status() == WL_CONNECTED){
    WiFiClient wifiClient;
    HTTPClient http;
    
    // POST request URL
    String url = serverUrl;
    url += endpoint;
    url += "?token=";
    url += token;

   // POST request body
   String requestBody = "temp=";
   requestBody += tempValue;

   // Send the POST request to the Django server
   http.begin(wifiClient, url);
   http.addHeader("Content-Type", "application/x-www-form-urlencoded");
   int httpResponseCode = http.POST(requestBody);
   http.end();

   // Print the response code and temperature reading
  Serial.print("HTTP Response code: ");
  Serial.println(httpResponseCode);
  Serial.print("Temperature: ");
  Serial.println(tempValue); 
  }else{
  Serial.println("Error connecting to wifi");  
  }
 delay(10000); // send data every 10 seconds 
}
