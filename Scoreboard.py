# import gpiozero
# from gpiozero import MotionSensor
from flask.scaffold import F
from playsound import playsound
import os
import random
from self import self
# from flask import Flask, redirect, render_template, request

# app = Flask(__name__)

class Scoreboard():

    print(
            '''
            Scoreboard started! Get to foosin'!
            '''
        )
    def __init__(self):
        self.currentGame = 1
        self.teamAScore = 0
        self.teamBScore = 0
        self.teamAWins = 0
        self.teamBWins = 0
        self.teamASide = 'Black'
        self.teamBSide = 'Yellow'
        # self.sensorBlack = MotionSensor(4)
        # self.sensorYellow = MotionSensor(17)

    def display(self):
            print(
                    '|Team A----Foosball----Team B|\n'
                    '|'+ self.teamASide + '                 ' + self.teamBSide +'|\n'
                    '|Pts:'+str(self.teamAScore)+'----|----------|--Pts:'+str(self.teamBScore)+'|\n'
                    '|Wins:'+str(self.teamAWins)+'---|----------|-Wins:'+str(self.teamBWins)+'|\n'
                    '|-----------Game '+str(self.currentGame)+'-----------|\n'
                )
            # return render_template('scoreboard.html',
            #     teamASide = self.teamASide,
            #     teamBSide = self.teamBSide,
            #     teamAScore = self.teamAScore,
            #     teamBScore = self.teamBScore,
            #     teamAWins = self.teamAWins,
            #     teamBWins = self.teamBWins,
            #     currentGame = self.currentGame)

    def goalSound(self):
        sounds = os.listdir('./Sounds/Goal/')
        soundToPlay = str('./Sounds/Goal/' + random.choice(sounds))
        print(soundToPlay)
        playsound(soundToPlay)

    def gameWinSound(self):
        sounds = os.listdir('./Sounds/Gamewin/')
        soundToPlay = str('./Sounds/Gamewin/' + random.choice(sounds))
        playsound(soundToPlay)

    def matchWinSound(self):
        sounds = os.listdir('./Sounds/Matchwin/')
        soundToPlay = str('./Sounds/Matchwin/' + random.choice(sounds))
        playsound(soundToPlay)

    def funModeSound(self):
        sounds = os.listdir('./Sounds/Funmode/')
        soundToPlay = str('./Sounds/Funmode/' + random.choice(sounds))
        playsound(soundToPlay)

    def blackGoal(self):
        print('Black team goal!')
        if(self.teamASide == 'Black'):
            setattr(self, 'teamAScore', self.teamAScore + 1)
        else:
            teamBScore = self.teamBScore + 1
            setattr(self, 'teamBScore', teamBScore)

    def yellowGoal(self):
        print('Yellow team goal!')
        if(self.teamASide == 'Yellow'):
            teamAScore = self.teamAScore + 1
            setattr(self, 'teamAScore', teamAScore)
        else:
            teamBScore = self.teamBScore + 1
            setattr(self,'teamBScore', teamBScore)

    def newGame(self, team):
        currentGame = self.currentGame + 1
        if(currentGame <= 3):
            print('Game ' + str(currentGame) + ' starting. Switch sides!')
        if(team == 'Black'):
            if(self.teamASide == team):
                teamAWins = scoreboard.teamAWins + 1
                setattr(self, 'teamAWins', teamAWins)
            if(self.teamBSide == team):
                teamBWins = scoreboard.teamBWins + 1
                setattr(self,'teamBWins', teamBWins)
        if(team == 'Yellow'):
            if(self.teamASide == team):
                teamAWins = scoreboard.teamAWins + 1
                setattr(self, 'teamAWins', teamAWins)
            if(self.teamBSide == team):
                teamBWins = scoreboard.teamBWins + 1
                setattr(self,'teamBWins', teamBWins)
        if(self.teamAWins == 2 or self.teamBWins == 2):
            print('match over nerds')
            return
        else:
            setattr(self, 'teamAScore', 0)
            setattr(self, 'teamBScore', 0)
            setattr(self, 'currentGame', currentGame)
            if(self.currentGame == 1 or self.currentGame == 3):
                setattr(self, 'teamASide', 'Black')
                setattr(self, 'teamBSide', 'Yellow')
            if(self.currentGame == 2):
                setattr(self, 'teamASide', 'Yellow')
                setattr(self, 'teamBSide', 'Black')
            scoreboard.display()



scoreboard = Scoreboard()

while scoreboard.teamAWins < 2 and scoreboard.teamBWins < 2:
    if scoreboard.teamAScore == 6 or scoreboard.teamBScore == 6:
        print("Game Point!")
    if (scoreboard.teamAScore > 0 or scoreboard.teamBScore > 0):
        if(scoreboard.teamAScore < 7 or scoreboard.teamBScore < 7):
            scoreboard.display()
    bob = input('y or b ')
    # sensorBlack.wait_for_motion()
    if(bob == 'b'):
        scoreboard.goalSound()
        scoreboard.blackGoal()
        if scoreboard.teamAScore == 7:
            if scoreboard.teamAWins == 2:
                print(scoreboard.teamASide + ' wins the match!')
                scoreboard.matchWinSound()
            else: scoreboard.newGame('Black')
        elif scoreboard.teamBScore == 7:
            if scoreboard.teamBWins == 2:
                print(scoreboard.teamBSide + ' wins the match!')
                scoreboard.gameWinSound()
            else: scoreboard.newGame('Black')
    if(bob == 'y'):
        scoreboard.goalSound()
        scoreboard.yellowGoal()
        if scoreboard.teamAScore == 7:
            if scoreboard.teamAWins == 2:
                print(scoreboard.teamASide + ' wins the match!')
                scoreboard.matchWinSound()
            else: scoreboard.newGame('Yellow')
        elif scoreboard.teamBScore == 7:
            if scoreboard.teamBWins == 2:
                print(scoreboard.teamBSide + ' wins the match!')
                scoreboard.gameWinSound()
            else: scoreboard.newGame('Black')

# app.run()