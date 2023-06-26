from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

from lights import Light
from ip import IP

app = FastAPI()
light = Light()
ip = IP().get_ip()
mainurl = "http://iphonevonabdullah.local:8000/app"


@app.get("/light-1-on", response_class=RedirectResponse)
def light1on():
    print(light.light1on())
    return RedirectResponse(mainurl)

@app.get("/light-1-off", response_class=RedirectResponse)
def light1off():
    print(light.light1off())
    return RedirectResponse(mainurl)

@app.get("/light-2-on", response_class=RedirectResponse)
def light2on():
    print(light.light2on())
    return RedirectResponse(mainurl)

@app.get("/light-2-off", response_class=RedirectResponse)
def light2off():
    print(light.light2off())
    return RedirectResponse(mainurl)

@app.get("/ip")
def returnip():
    return ip

@app.get("/app", response_class=HTMLResponse)
async def serve_app():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mobile Website</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f2f2f2;
      margin: 0;
      padding: 0;
    }

    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    .button {
      width: 200px;
      height: 50px;
      margin: 10px;
      background-color: #4CAF50;
      border: none;
      color: white;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      border-radius: 5px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="container">
    <a href="%s" class="button">Hoch an</a>
    <a href="%s" class="button">Hoch stopp</a>
    <a href="%s" class="button">Runter an</a>
    <a href="%s" class="button">Runter stopp</a>
  </div>
</body>
</html>

    """ % (f"http://{ip}:8000/light-1-on", f"http://{ip}:8000/light-1-off", f"http://{ip}:8000/light-2-on", f"http://{ip}:8000/light-2-off")
