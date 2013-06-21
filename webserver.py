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
        return render.index(sht1x.read_temperature_C(), sht1x.read_humidity())

if __name__ == "__main__":
    app.run()