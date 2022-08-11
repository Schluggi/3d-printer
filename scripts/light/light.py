from fastapi import FastAPI, Request,Body
from pydantic import BaseModel
import RPi.GPIO as GPIO
from time import sleep

app = FastAPI()

LED = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, GPIO.HIGH)
sleep(1)
GPIO.output(LED, GPIO.LOW)

@app.post('/light')
async def light_set(request: Request):
    light = await request.json()
    GPIO.output(LED, light['state'])
    return await light_get()

@app.get('/light')
async def light_get():
    return {"state": int(GPIO.input(LED))}
