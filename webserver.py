from sht1x.Sht1x import Sht1x as SHT1x
import web

dataPin = 11
clkPin = 7
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)
        
urls = (
    '/', 'atmo_server'
)
app = web.application(urls, globals())

render = web.template.render('templates/')

class atmo_server:        
    def GET(self):
        temperature = sht1x.read_temperature_C()
        humidity = '{0:.2f}'.format(sht1x.read_humidity())
        return render.index(temperature, humidity)

if __name__ == "__main__":
    app.run()