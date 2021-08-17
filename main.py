# import gpiozero
# from gpiozero import MotionSensor
# from playsound import playsound
import os
import random
# from self import self
from flask import Flask, redirect, render_template, request, render_template_string
from Scoreboard import Scoreboard

app = Flask(__name__)


scoreboard = Scoreboard()

def index():

    scoreboard.display()

    return render_template('index.html',
    teamAScore = scoreboard.teamAScore,
    teamBScore = scoreboard.teamBScore,
    teamAWins = scoreboard.teamAWins,
    teamBWins = scoreboard.teamBWins,
    currentGame = scoreboard.currentGame,
    teamASide = scoreboard.teamASide,
    teamBSide = scoreboard.teamBSide,
    )

def scoreMatch():
    while scoreboard.teamAWins < 2 and scoreboard.teamBWins < 2:
        scoreboard.display()
        waitForGoal()
        

def waitForGoal():
    goalScored = input('input y or b for a goal')
    if(goalScored == 'b'):
        scoringTeam = 'Black'
        scoreboard.addGoal(scoringTeam)
        scoreboard.playSoundEffect('Goal')
        scoreboard.checkGameWin()
        scoreboard.checkMatchWin()
    return render_template('index.html',
    teamAScore = scoreboard.teamAScore,
    teamBScore = scoreboard.teamBScore,
    teamAWins = scoreboard.teamAWins,
    teamBWins = scoreboard.teamBWins,
    currentGame = scoreboard.currentGame,
    teamASide = scoreboard.teamASide,
    teamBSide = scoreboard.teamBSide,
    )


app.run()