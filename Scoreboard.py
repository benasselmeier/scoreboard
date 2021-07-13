#from gpiozero import MotionSensor
from flask import Flask, flash, redirect, render_template, request, session
from playsound import playsound
import os
import random

app = Flask(__name__)

class Scoreboard():
    # sensorBlack = MotionSensor()
    # sensorYellow = MotionSensor()

    def __init__():
        print(
            '''
            Scoreboard started! Get to foosin'!
            '''
        )
    currentGame = 1
    blackScore = 0
    yellowScore = 0
    blackWins = 0
    yellowWins = 0
    def goalSound():
        sounds = os.listdir('./Sounds/')
        soundToPlay = str('./Sounds/' + random.choice(sounds))
        playsound(soundToPlay)


    while blackWins < 2 and yellowWins < 2:
        if blackScore == 6 or yellowScore == 6:
            print("Game Point!")
        testValue = input("Jank testing suite - input 'y' for yellow goals and 'b' for black goals. \n")
        if testValue == "b":
            #sensorBlack.wait_for_motion()
            print("Black team scored!")
            blackScore = blackScore + 1
            print ("Game Score:\nBlack Team: " + str(blackScore) + "\nYellow Team: " + str(yellowScore))
            goalSound()
        if blackScore == 7:
            print("Black team wins game " + str(currentGame) + "!")
            blackWins = blackWins + 1
            if blackWins == 2:
                print("Black team wins the match!")
            else:
                print("Match Score: \n"
                "Black team: " + str(blackWins) + "\n"
                "Yellow team: " + str(yellowWins) + "\n"
                )
                currentGame = currentGame + 1
                blackScore = 0
                yellowScore = 0
        if testValue == "y":
            #sensorYellow.wait_for_motion()
            print("Yellow team scored!")
            yellowScore = yellowScore + 1
            print ("Game Score:\nBlack Team: " + str(blackScore) + "\nYellow Team: " + str(yellowScore))
            goalSound()
        if yellowScore == 7:
            print("Yellow Team wins game " + str(currentGame) + "!")
            yellowWins = yellowWins + 1
            if yellowWins == 2:
                print("Yellow team wins the match!")
            else:
                print("Match Score: \n"
                "Black team: " + str(blackWins) + "\n"
                "Yellow team: " + str(yellowWins) + "\n"
                )
                currentGame = currentGame + 1
                blackScore = 0
                yellowScore = 0

@app.route('/')
def index():

    yellowScore
    blackScore
    currentGame
    yellowWins
    blackWins

    return render_template(yellowScore, blackScore, currentGame, yellowWins, blackWins, 'index.html', title = "Scoreboard")
