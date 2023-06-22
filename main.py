from fastapi import FastAPI
from lights import Light

app = FastAPI()
light = Light()

@app.get("/light-1-on")
def light1on():
    print(light.light1on())
    return {"status" : 200}

@app.get("/light-1-off")
def light1off():
    print(light.light1off())
    return {"status" : 200}

@app.get("/light-2-on")
def light2on():
    print(light.light2on())
    return {"status" : 200}

@app.get("/light-2-off")
def light2off():
    print(light.light2off())
    return {"status" : 200}

