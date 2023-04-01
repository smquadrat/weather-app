from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # User submits location
        if 'location' not in request.form:
            return render_template('index.html', error='Please enter a location')
        location = request.form['location']

        # Make API call to OpenMeteo geocoding API
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&language=en&count=1&format=json"
        response = requests.get(url)
        data = response.json()

        # Extract latitude and longitude coordinates from response
        lat = str(data['results'][0]['latitude'])
        lon = str(data['results'][0]['longitude'])

        # Make API call to OpenMeteo weather API to get forecast data
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation_probability,uv_index&current_weather=true&temperature_unit=fahrenheit&timezone=America%2FNew_York"
        response = requests.get(url)
        data = response.json()

        print(data)

        # Extract 10 day forecast data
        forecast = []
        for i in range(len(data['hourly']['time'])):
            date = data['hourly']['time'][i]
            temp = data['hourly']['temperature_2m'][i]
            precip = data['hourly']['precipitation_probability'][i]
            uv = data['hourly']['uv_index'][i]
            forecast.append({'date': date, 'temp': temp, 'precip': precip, 'uv': uv})

        # Render forecast template with forecast data
        return render_template('forecast.html', forecast=forecast)

    # Render home template if no location submitted
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)