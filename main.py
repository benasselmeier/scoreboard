# import gpiozero
# from gpiozero import MotionSensor
from flask.templating import render_template_string
# from playsound import playsound
import os
import random
# from self import self
from flask import Flask, redirect, render_template, request, render_template_string
import Scoreboard

app = Flask(__name__)


scoreboard = Scoreboard()

@app.route('/')
def renderView():
    return render_template('index.html',
    teamAScore = scoreboard.teamAScore,
    teamBScore = scoreboard.teamBScore,
    teamAWins = scoreboard.teamAWins,
    teamBWins = scoreboard.teamBWins,
    currentGame = scoreboard.currentGame,
    teamASide = scoreboard.teamASide,
    teamBSide = scoreboard.teamBSide,
    )


    # while scoreboard.teamAWins < 2 and scoreboard.teamBWins < 2:
    #     if scoreboard.teamAScore == 6 or scoreboard.teamBScore == 6:
    #         print("Game Point!")
    #     if (scoreboard.teamAScore > 0 or scoreboard.teamBScore > 0):
    #         if(scoreboard.teamAScore < 7 or scoreboard.teamBScore < 7):
                # scoreboard.display()
                # return render_template('index.html',
                # teamAScore = scoreboard.teamAScore,
                # teamBScore = scoreboard.teamBScore,
                # teamAWins = scoreboard.teamAWins,
                # teamBWins = scoreboard.teamBWins,
                # currentGame = scoreboard.currentGame,
                # teamASide = scoreboard.teamASide,
                # teamBSide = scoreboard.teamBSide,
                # )
def doTheScoringThing(bob):
    # sensorBlack.wait_for_motion()
    if(bob == 'b'):
        # scoreboard.goalSound()
        scoreboard.blackGoal()
        if scoreboard.teamAScore == 7:
            if scoreboard.teamAWins == 2:
                print(scoreboard.teamASide + ' wins the match!')
                # scoreboard.matchWinSound()
            else: scoreboard.newGame('Black')
        elif scoreboard.teamBScore == 7:
            if scoreboard.teamBWins == 2:
                print(scoreboard.teamBSide + ' wins the match!')
                # scoreboard.gameWinSound()
            else: scoreboard.newGame('Black')
    if(bob == 'y'):
        # scoreboard.goalSound()
        scoreboard.yellowGoal()
        if scoreboard.teamAScore == 7:
            if scoreboard.teamAWins == 2:
                scoreboard.winner('Yellow')
                # scoreboard.matchWinSound()
            else: scoreboard.newGame('Yellow')
        elif scoreboard.teamBScore == 7:
            if scoreboard.teamBWins == 2:
                scoreboard.winner('Black')
                # scoreboard.gameWinSound()
            else: scoreboard.newGame('Black')

while scoreboard.teamAWins < 2 and scoreboard.teamBWins < 2:
    if(scoreboard.teamAScore < 7 or scoreboard.teamBScore < 7):
        scoreboard.display()
        bob = input('y or b')
        doTheScoringThing(bob)

app.run()