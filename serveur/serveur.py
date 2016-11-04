import requests
import time
import os

from flask import Flask, request
app = Flask(__name__)


from jinja2 import Environment, PackageLoader
jinja_env = Environment(loader=PackageLoader('serveur','views'))







@app.route("/")
def hello():
    data = requests.get('https://api.smartcitizen.me/v0/devices/3743')
    dataJ = data.json()

    for sensor in dataJ['data']['sensors']:
        if sensor['description']=='Temperature':
            tempv = sensor['value']
        elif sensor['description']=='Humidity':
            humidity = sensor['value']
        elif sensor['description']=='NO2':
            pollution = sensor['value']
    for sensor in dataJ['data']['sensors']:
        if sensor['description']== "Electret microphone with envelope follower sound pressure sensor (noise)":
            noiseV = sensor['value']
            noiseU = sensor['unit']

    base = jinja_env.get_template('base.html')
    return base.render(temp_value = tempv, humidity_value = humidity, pollution_value = pollution, noise_value = noiseV, noise_unit = noiseU)



@app.route("/temperature")
def temperature():
    import requests

    data = requests.get('https://api.smartcitizen.me/v0/devices/1616')
    dataJ = data.json()

    for sensor in dataJ['data']['sensors']:
        if sensor['id']==4:
            temperature = sensor['value']
    return str(temperature)


@app.route("/clak")
def livehoney():
    time.sleep (10)
    return "YES"


    # Upload snapshot
@app.route("/shot", methods=['POST'])
def beebeeliotheque():
   if request.method == 'POST':
       # check if the post request has the file part
       if 'image' not in request.files:
           return 'ERROR: No file..'

       file = request.files['image']
       if not file or file.filename == '':
           return 'ERROR: Wrong file..'        # Save Snapshot with Timestamp

       filepath = os.path.join(os.path.dirname(os.path.abspath(__file__))+'/static/upload/', "usershot.jpg")
       file.save(filepath)
       return 'SUCCESS'

   return 'ERROR: You\'re lost Dave..'


if __name__ == "__main__":
    app.run (port=11000)
