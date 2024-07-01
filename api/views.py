# Create your views here.

import re
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class WeatherView(APIView):
    # To get the requesting client IP address:
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    # Getting the location of the IP using IPINFO API 
    def get_location(self, ip):
        # The API key is stored as an environment variable and extracted in settings.py
        api_key = settings.IPINFO_API_KEY
        response = requests.get(f'https://ipinfo.io/{ip}?token={api_key}')
        if response.status_code == 200:
            data = response.json()
            # Getting the city of the IP with unknown as a fallback
            return data.get('city', 'Unknown')
            return city
        return 'Unknown'

    # Getting the current weather condition of the location using Openweather API
    def get_weather(self, city):
        # The API key is extracted in settings.py
        api_key = settings.WEATHER_API_KEY
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
        if response.status_code == 200:
            weather_data = response.json()
            temp = weather_data['main']['temp']
            return temp
        return None

    # Function to state the data to be returned for the GET request
    def get(self, request):
        ip = self.get_client_ip(request)
        location = self.get_location(ip)
        temp = self.get_weather(location)
        greeting = f"Hello, Mark!, the temperature is {temp} degrees Celsius in {location}"

        # Extracting the visitor_name query parameter and using Mark as a fallback
        visitor_name = request.query_params.get('visitor_name', 'Mark')
        # Regex to remove quotes from query parameter
        visitor_name = re.sub(r'["\']', '', visitor_name)

        greeting = f"Hello, {visitor_name}!, the temperature is {temp} degrees Celsius in {location}"

        data = {
            "client_ip": ip,
            "location": location,
            "greeting": greeting
        }
        return Response(data, status=status.HTTP_200_OK)
