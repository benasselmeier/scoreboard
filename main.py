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



while True:
    if GPIO.input(sensorBlackPin):
        # scoringTeam = 'Black'
        # scoreboard.addGoal(scoringTeam)
        # scoreboard.playSoundEffect('Goal')
        # scoreboard.checkGameWin()
        # scoreboard.checkMatchWin()
        print('beam unbroken')
    else: print('beam broken!')
    time.sleep(0.5)


scoreboard = Scoreboard()

# @app.route('/')
# def render():
#     return render_template('index.html',
#     teamAScore = scoreboard.teamAScore,
#     teamBScore = scoreboard.teamBScore,
#     teamAWins = scoreboard.teamAWins,
#     teamBWins = scoreboard.teamBWins,
#     currentGame = scoreboard.currentGame,
#     teamASide = scoreboard.teamASide,
#     teamBSide = scoreboard.teamBSide,
#     )

        

# def waitForGoal():
#     goalScored = input('input y or b for a goal')
#     if(goalScored == 'b'):
#         scoringTeam = 'Black'
#         scoreboard.addGoal(scoringTeam)
#         scoreboard.playSoundEffect('Goal')
#         scoreboard.checkGameWin()
#         scoreboard.checkMatchWin()
#     return render_template('index.html',
#     teamAScore = scoreboard.teamAScore,
#     teamBScore = scoreboard.teamBScore,
#     teamAWins = scoreboard.teamAWins,
#     teamBWins = scoreboard.teamBWins,
#     currentGame = scoreboard.currentGame,
#     teamASide = scoreboard.teamASide,
#     teamBSide = scoreboard.teamBSide,
#     )


# if scoreboard.teamAWins < 2 and scoreboard.teamBWins < 2:
#     scoreboard.display()
#     waitForGoal()
#     render()
# else:
#     scoreboard.declareWinner('Black')
#     render_template('winner.html')

# app.run()
