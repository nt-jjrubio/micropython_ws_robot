import network
from microdot import Microdot
from websocket import with_websocket

# Nos conectamos a la red
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("SSID","PASSWORD")

print("Start...")
while not sta_if.isconnected():
    pass

print("Connected to WiFi")

# Levantamos el servidor con Microdot
app = Microdot()
#Endpoint de prueba
@app.route('/')
async def index(request):
    print("Entra por /")
    return 'Hello world!'
#Endpoint de websocket 
@app.route('/ws')
@with_websocket
async def echo(request, ws):
    print("Connected ", ws) 
    ws.send('Connected...')
    while True:
        data = await ws.receive()
        if data == 'u':
            print("Up")
        elif data == 'd':
            print("Down")
        elif data == 'l':
            print("Left")
        elif data == 'r':
            print("Right")
          
app.run(port=3000, debug=True)


       
