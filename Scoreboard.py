# import gpiozero
# from gpiozero import MotionSensor
from playsound import playsound
import os
import random
from self import self

class Scoreboard():

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
    # sensorBlack = MotionSensor(4)
    # sensorYellow = MotionSensor(17)
    teamAside = 'black'
    teamBSide = ''

    def ready():
        print(
            '|----------Foosball----------|\n'
            '|Black                 Yellow|\n'
            '|Pts:'+self.blackScore+'----|----------|----Pts:'+self.yellowScore+'|\n'
            '|Wins:'+self.blackWins+'---|----------|---Wins:'+self.yellowWins+'|\n'
            '|-----------Game '+self.currentGame+'-----------|\n'

        )

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

    def blackGoal():
        print('Black team goal!')
        blackScore = Scoreboard.blackScore + 1
        setattr(self, 'blackScore', blackScore)

    def yellowGoal():
        print('Yellow team goal!')
        yellowScore = self.yellowScore + 1
        setattr(self, 'yellowScore', yellowScore)

    def newGame(team):
        newGame = self.currentGame + 1
        setattr(self, 'blackScore', 0)
        setattr(self, 'yellowScore', 0)
        setattr(self, 'currentGame', newGame)
        if(team == 'black'):
            newBlackWins = self.blackWins + 1
            setattr(self, 'blackWins', newBlackWins)
        if(team == 'yellow'):
            newYellowWins = self.yellowWins + 1
            setattr(self, 'yellowWins', newYellowWins)




    while blackWins < 2 and yellowWins < 2:
        if blackScore == 6 or yellowScore == 6:
            print("Game Point!")
        if blackScore > 0 or yellowScore > 0:
            print ("Game Score:\nBlack Team: " + str(blackScore) + "\nYellow Team: " + str(yellowScore))

        bob = input('y or b bitchhhhhhhh')

        # sensorBlack.wait_for_motion()
        if(bob == 'b'):
            goalSound()
            blackGoal()
            if blackScore == 7:
                if blackWins == 2:
                    print("Black team wins the match!")
                    matchWinSound()
                else:
                    gameWinSound()
                    newGame()
            ready()

        if(bob == 'y'):
            goalSound()
            yellowGoal()
            if yellowScore == 7:
                if yellowWins == 2:
                    print("Yellow team wins the match!")
                    matchWinSound()
                else:
                    gameWinSound()
                    newGame()
            ready()
