from sht1x.Sht1x import Sht1x as SHT1x
import web

dataPin = 11
clkPin = 7
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

html = '''<html>
  <head>
    <script type='text/javascript' src='https://www.google.com/jsapi'></script>
    <script type='text/javascript'>
      google.load('visualization', '1', {{packages:['gauge']}});
      google.setOnLoadCallback(drawChart);
      function drawChart() {{
        var data = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['Temp', {0}],
          ['Humidity', {1:10.2f}]
        ]);

        var options = {{
          width: 400, height: 120,
          redFrom: 90, redTo: 100,
          yellowFrom:75, yellowTo: 90,
          minorTicks: 5
        }};

        var chart = new google.visualization.Gauge(document.getElementById('chart_div'));
        chart.draw(data, options);
      }}
    </script>
  </head>
  <body>
    <div id='chart_div'></div>
  </body>
</html>'''

class hello:        
    def GET(self, name):
        return html.format(sht1x.read_temperature_C(), sht1x.read_humidity())

if __name__ == "__main__":
    app.run()