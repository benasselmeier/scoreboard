# import gpiozero
# from gpiozero import MotionSensor
# from playsound import playsound
import RPi.GPIO as GPIO
import os
import random
# from flask import Flask, redirect, render_template, request, render_template_string
from Scoreboard import Scoreboard
import time

# app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.add_event_detect(4, GPIO.BOTH)

sensorBlackPin = 4

scoreboard = Scoreboard()


while scoreboard.teamAWins < 2 and scoreboard.teamBWins < 2:
    if GPIO.input(sensorBlackPin):
        print ('Waiting for goal...')
    else:
        scoreboard.addGoal('Black')
        scoreboard.playSoundEffect('Goal')
        scoreboard.checkGameWin()
        scoreboard.checkMatchWin()
        scoreboard.display()
    time.sleep(0.5)


# app.run()
