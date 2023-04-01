from flask import Flask, request, render_template
from bokeh.resources import CDN
import requests

app = Flask(__name__)

# Replace YOUR_API_KEY with your OpenWeatherMap API key
API_KEY = 'bd5e378503939ddaee76f12ad7a97608'

# '99f19be90a6c0bdaef5f8c9f8aad4186'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def forecast():
    if request.method == 'POST':
        # User submits zip code
        zip_code = request.form['zip_code']

        # Make API call to OpenWeatherMap
        # url = f"https://api.openweathermap.org/data/2.5/forecast?zip={zip_code}&units=imperial&appid={API_KEY}"
        # response = requests.get(url)
        # data = response.json()

        # Extract 10 day forecast data
        forecast = []
        for i in range(0, 10):
            date = data["list"][i]["dt_txt"]
            temp = data["list"][i]["main"]["temp"]
            desc = data["list"][i]["weather"][0]["description"]
            forecast.append({'date': date, 'temp': temp, 'desc': desc})

        cdn_js = CDN.js_files[0]

        # Render forecast template with forecast data
        return render_template('forecast.html', forecast=forecast, cdn_js=cdn_js)

    # Render home template if no zip code submitted
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
