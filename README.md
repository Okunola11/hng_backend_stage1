# Simple API
A simple API project for Stage 1 of the HNG11 Internship. The task is to return the IP address, location, weather condition, and optionally, a given name parameter for a requesting user to the GET endpoint.

Deployed to: https://abd1.pythonanywhere.com/api/hello/

### Tools Used
- Python 3.12.4
- Django Rest Framework
- OpenWeather API
- IPinfo API
  
### Endpoints
GET /api/hello/

Query Parameters:

_visitor_name_ (optional): The name to include in the greeting message.

Response: 
```json
"client_ip": "127.0.0.1", // The IP address of the requester
"location": "New York" // The city of the requester
"greeting": "Hello, Mark!, the temperature is 11 degrees Celcius in New York"
```
