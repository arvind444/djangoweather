from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	if request.method == "POST":
		city = request.POST['city']
		api_result = requests.get('https://api.weatherapi.com/v1/forecast.json?key=1ab3a5f55b954b848b692717210807&q='+ city +'&days=1&aqi=yes&alerts=yes')

		try:
			api = json.loads(api_result.content)
			aqi = api['current']['air_quality']['us-epa-index']
			astro = api['forecast']['forecastday'][0]['astro']
			temperature = api['forecast']['forecastday'][0]['day']
		except Exception as e:
			api = "Error Occured"
			aqi = "Error Occured"
			astro = "Error Occured"
			temperature = "Error Occured"

		return render(request, 'home.html', {'api': api, 'aqi': aqi, 'astro' : astro, 'temperature' : temperature})
		
	else:

		api_result = requests.get('https://api.weatherapi.com/v1/forecast.json?key=1ab3a5f55b954b848b692717210807&q=delhi&days=1&aqi=yes&alerts=yes')

		try:
			api = json.loads(api_result.content)
			aqi = api['current']['air_quality']['us-epa-index']
			astro = api['forecast']['forecastday'][0]['astro']
			temperature = api['forecast']['forecastday'][0]['day']
			wind = api['forecast']['forecastday'][0]['hour'][0]
		except Exception as e:
			api = "Error Occured"
			aqi = "Error Occured"
			astro = "Error Occured"
			temperature = "Error Occured"
			wind = "Error Occured"

		return render(request, 'home.html', {'api': api, 'aqi': aqi, 'astro' : astro, 'temperature' : temperature, 'wind' : wind})

def about(request):
	return render(request, 'about.html', {})