import dhtreader
import web
import json

dhtPin = 4
dhtreader.init()
        
urls = (
    '/', 'atmo_server',
    '/json', 'render_json'
)
app = web.application(urls, globals())

render = web.template.render('templates/')

#temperature = 2
#humidity = 4

class atmo_server:        
    def GET(self):
        return render.index()

class render_json:        
    def GET(self):
        temperature, humidity = (0,0)
        try:
            temperature, humidity = dhtreader.read(22, dhtPin)
        except:
            print('Error reading sensor')
        if temperature and humidity:
            jsonData = json.dumps({'temperature': float('{0:.2f}'.format(temperature)), 'humidity': float('{0:.2f}'.format(humidity))})
            return jsonData
        else:
            return

if __name__ == "__main__":
    app.run()
