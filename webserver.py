import web
import json

urls = (
    '/', 'atmo_server',
    '/json', 'render_json'
)
app = web.application(urls, globals())

render = web.template.render('templates/')

class atmo_server:        
    def GET(self):
        return render.index()

class render_json:        
    def GET(self):
        temperature, humidity = (None, None)
        while (temperature is None and humidity is None):
            try:
                with open('TEMP', 'r') as t:
                    temperature = float(t.read())
                with open('HUMIDITY', 'r') as h:
                    humidity = float(h.read())
            except:
                pass

        if temperature and humidity:
            jsonData = json.dumps({'temperature': float('{0:.2f}'.format(temperature)), 'humidity': float('{0:.2f}'.format(humidity))})
            return jsonData
        else:
            return

if __name__ == "__main__":
    app.run()
