import requests

from flask import Flask
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





@app.route("/")
def news():

    base = jinja_env.get_template('base.html')
    return base.render(humidity_value = humidity)


@app.route("/temperature")
def temperature():
    import requests

    data = requests.get('https://api.smartcitizen.me/v0/devices/1616')
    dataJ = data.json()

    for sensor in dataJ['data']['sensors']:
        if sensor['id']==4:
            temperature = sensor['value']
    return str(temperature)





if __name__ == "__main__":
    app.run(host="10.23.48.210", port=10000)
