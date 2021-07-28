# import gpiozero
# from gpiozero import MotionSensor
from playsound import playsound
import os
import random
from threading import current_thread
from flask import Flask, redirect, render_template, request
app = Flask(__name__)
app.config['DEBUG'] = True
class Scoreboard():

    currentGame = 0
    blackScore = 0
    yellowScore = 0
    blackWins = 0
    yellowWins = 0

    # sensorBlack = MotionSensor(4)
    # sensorYellow = MotionSensor(17)

    def __init__(self):
        print(
        '''
        Scoreboard ready. \n
        Default mode.
        '''
    )


scoreboard=Scoreboard()


@app.route('/')
def index():

    scoreboard.currentGame = 1
    print(scoreboard.currentGame)
    scoreboard.blackScore = 0
    scoreboard.yellowScore = 0
    return render_template('/scoreboard.html',
    blackScore = scoreboard.blackScore,
    yellowScore = scoreboard.yellowScore,
    blackWins = scoreboard.blackWins,
    yellowWins = scoreboard.yellowWins,
    currentGame = scoreboard.currentGame)

@app.route('/goal')
def goal():
    # goalSound()
    team = request.args.get('team')
    if(team == 'black'):
        newBlackScore = scoreboard.blackScore + 1
        if(newBlackScore == 7):
            newBlackScore = 0
            newGame(team)
        setattr(scoreboard, 'blackScore', newBlackScore)
        return render_template('/scoreboard.html',
        blackScore = newBlackScore,
        yellowScore = scoreboard.yellowScore,
        blackWins = scoreboard.blackWins,
        yellowWins = scoreboard.yellowWins,
        currentGame = scoreboard.currentGame
        )

    if(team == 'yellow'):
        newYellowScore = scoreboard.yellowScore + 1
        if(newYellowScore == 7):
            newYellowScore = 0
            newGame(team)
        setattr(scoreboard, 'yellowScore', newYellowScore)
        return render_template('/scoreboard.html',
        blackScore = scoreboard.blackScore,
        yellowScore = newYellowScore,
        blackWins = scoreboard.blackWins,
        yellowWins = scoreboard.yellowWins,
        currentGame = scoreboard.currentGame
        )

def newGame(team):
    if(team == 'yellow'):
        newYellowWins = scoreboard.yellowWins + 1
        print(newYellowWins)
        if(newYellowWins < 2):
            setattr(scoreboard, 'yellowWins', newYellowWins)
            setattr(scoreboard, 'yellowScore', 0)
            setattr(scoreboard, 'blackScore', 0)
            newGame = scoreboard.currentGame + 1
            setattr(scoreboard, 'currentGame', newGame)
            print('Yellow Team Wins!')
            return render_template('/scoreboard.html',
            blackScore = scoreboard.blackScore,
            yellowScore = scoreboard.yellowScore,
            blackWins = scoreboard.blackWins,
            yellowWins = scoreboard.yellowWins,
            currentGame = newGame)
        else:
            print('fish')
            return matchWin(team)

    if(team == 'black'):
        newBlackWins = scoreboard.blackWins + 1
        print(str(newBlackWins))
        if(newBlackWins <2 ):
            setattr(scoreboard, 'blackWins', newBlackWins)
            setattr(scoreboard, 'yellowScore', 0)
            setattr(scoreboard, 'blackScore', 0)
            newGame = scoreboard.currentGame + 1
            setattr(scoreboard, 'currentGame', newGame)
            print('Black Team Wins!')
            return render_template('/scoreboard.html',
            blackScore = scoreboard.blackScore,
            yellowScore = scoreboard.yellowScore,
            blackWins = scoreboard.blackWins,
            yellowWins = scoreboard.yellowWins,
            currentGame = newGame)

def matchWin(team):
    if(team == 'black'):
        print('Black team wins the match')
        return render_template('/winner.html', winner = team)
    if(team == 'yellow'):
        print('Yellow team wins the match')
        return render_template('/winner.html', winner = team)

def goalSound():
    sounds = os.listdir('./Sounds/Goal/')
    soundToPlay = str('./Sounds/Goal/' + random.choice(sounds))
    print(soundToPlay)
    playsound(soundToPlay)
def gameWinSound():
    sounds = os.listdir('./Sounds/Gamewin/')
    soundToPlay = str('./Sounds/Gamewin/' + random.choice(sounds))
    playsound(soundToPlay)
def matchWinSound():
    sounds = os.listdir('./Sounds/Matchwin/')
    soundToPlay = str('./Sounds/Matchwin/' + random.choice(sounds))
    playsound(soundToPlay)
def funModeSound():
    sounds = os.listdir('./Sounds/Funmode/')
    soundToPlay = str('./Sounds/Funmode/' + random.choice(sounds))
    playsound(soundToPlay)






if __name__ == '__main__':
    app.run()