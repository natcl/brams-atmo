from sht1x.Sht1x import Sht1x as SHT1x
import web
import json

dataPin = 11
clkPin = 7
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)
        
urls = (
    '/', 'atmo_server',
    '/json', 'render_json'
)
app = web.application(urls, globals())

render = web.template.render('templates/')

class atmo_server:        
    def GET(self):
        temperature = '{0:.2f}'.format(sht1x.read_temperature_C())
        humidity = '{0:.2f}'.format(sht1x.read_humidity())
        return render.index(temperature, humidity)

class render_json:        
    def GET(self):
        temperature = '{0:.2f}'.format(sht1x.read_temperature_C())
        humidity = '{0:.2f}'.format(sht1x.read_humidity())
        jsonData = json.dumps({'temperature': temperature, 'humidity': humidity})
        return jsonData

if __name__ == "__main__":
    app.run()