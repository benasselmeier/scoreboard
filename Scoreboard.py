# import gpiozero
# from gpiozero import MotionSensor
# from playsound import playsound
# import os
# import random
from threading import current_thread
from flask import Flask, redirect, render_template

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
def newGame():
    
    scoreboard.currentGame = 1
    print(scoreboard.currentGame)
    scoreboard.blackScore = 0
    scoreboard.yellowScore = 0

    print(str(scoreboard.currentGame) + ' < cg yw > ' + str(scoreboard.yellowWins))



    return render_template('/scoreboard.html', blackScore = scoreboard.blackScore)

@app.route('/goal')
def goal():
    blackScore = scoreboard.blackScore + 1
    return

    
    

if __name__ == '__main__':
    app.run()