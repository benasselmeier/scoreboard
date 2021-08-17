import gpiozero
from gpiozero import MotionSensor
from playsound import playsound
import RPi.GPIO as GPIO
import os
import random

GPIO.setmode(GPIO.BCM)

class Scoreboard():

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

    def addGoal(self, team):
        print (team + ' team scored!')
        if(team == 'Black'):
            if(self.teamASide == team):
                setattr(self, 'teamAScore', self.teamAScore + 1)
            if(self.teamBSide == team):
                setattr(self, 'teamBScore', self.teamBScore + 1)
        if(team == 'Yellow'):
            if(self.teamASide == team):
                setattr(self, 'teamAScore', self.teamAScore + 1)
            if(self.teamBSide == team):
                setattr(self, 'teamBScore', self.teamBScore + 1)

    def playSoundEffect(self, type):
        print
        if(type != ''):
            sounds = os.listdir('./Sounds/' + type + '/')
            soundToPlay = str('/Sounds/' + type + '/' + random.choice(sounds))
        else:
            print("Something went wrong when trying to play a sound...")


    def checkGameWin(self):
        if(self.teamAScore == 7):
            teamAWins = self.teamAWins + 1
            setattr(self, 'teamAWins', teamAWins)
            self.checkMatchWin()
            return self.newGame()
        if(self.teamBScore == 7):
            teamBWins = self.teamBWins + 1
            setattr(self, 'teamBWins', teamBWins)
            self.checkMatchWin()
            return self.newGame()

    def checkMatchWin(self):
        if(self.teamAWins == 2):
            return self.declareWinner(self.teamASide)
        if(self.teamBWins == 2):
            return self.declareWinner(self.teamBSide)

        
    def newGame(self):
        currentGame = self.currentGame + 1
        if(self.teamAWins < 2 and self.teamBWins < 2):
            print('Game ' + str(currentGame) + ' starting. Switch sides!')
            setattr(self, 'teamAScore', 0)
            setattr(self, 'teamBScore', 0)
            setattr(self, 'currentGame', currentGame)
            if(self.currentGame == 1 or self.currentGame == 3):
                setattr(self, 'teamASide', 'Black')
                setattr(self, 'teamBSide', 'Yellow')
            if(self.currentGame == 2):
                setattr(self, 'teamASide', 'Yellow')
                setattr(self, 'teamBSide', 'Black')


    def declareWinner(self, team):
        if team == 'Black':
            print('''
                  ____  _            _      _____                     __        ___           _
                 | __ )| | __ _  ___| | __ |_   _|__  __ _ _ __ ___   \ \      / (_)_ __  ___| |
                 |  _ \| |/ _` |/ __| |/ /   | |/ _ \/ _` | '_ ` _ \   \ \ /\ / /| | '_ \/ __| |
                 | |_) | | (_| | (__|   <    | |  __/ (_| | | | | | |   \ V  V / | | | | \__ \_|
                 |____/|_|\__,_|\___|_|\_\   |_|\___|\__,_|_| |_| |_|    \_/\_/  |_|_| |_|___(_)
            ''')

        if team == 'Yellow':
            print('''
                 __   __   _ _                 _____                     __        ___           _
                 \ \ / /__| | | _____      __ |_   _|__  __ _ _ __ ___   \ \      / (_)_ __  ___| |
                  \ V / _ \ | |/ _ \ \ /\ / /   | |/ _ \/ _` | '_ ` _ \   \ \ /\ / /| | '_ \/ __| |
                   | |  __/ | | (_) \ V  V /    | |  __/ (_| | | | | | |   \ V  V / | | | | \__ \_|
                   |_|\___|_|_|\___/ \_/\_/     |_|\___|\__,_|_| |_| |_|    \_/\_/  |_|_| |_|___(_)
            ''')