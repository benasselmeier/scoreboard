import gpiozero
from gpiozero import MotionSensor
from playsound import playsound
import os
import random

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
    sensorBlack = MotionSensor(4)
    sensorYellow = MotionSensor(17)

    def goalSound():
        sounds = os.listdir('./Sounds/Goal/')
        soundToPlay = str('./Sounds/Goal/' + random.choice(sounds))
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



    while blackWins < 2 and yellowWins < 2:
        if blackScore == 6 or yellowScore == 6:
            print("Game Point!")
        if blackScore > 0 or yellowScore > 0:
            print ("Game Score:\nBlack Team: " + str(blackScore) + "\nYellow Team: " + str(yellowScore))


    #if testValue == "b":
        sensorBlack.wait_for_motion()
        print("Black team scored!")
        blackScore = blackScore + 1
        goalSound()
        if blackScore == 7:
            blackScore = 0
            yellowScore = 0
            blackWins = blackWins + 1
            if blackWins == 2:
                print("Black team wins the match!")
                matchWinSound()
            else:
                print("Black team wins game " + str(currentGame) + "!")
                currentGame = currentGame + 1
                gameWinSound()
    #if testValue == "y":
        sensorYellow.wait_for_motion()
        print("Yellow team scored!")
        yellowScore = yellowScore + 1
        goalSound()
        if yellowScore == 7:
            blackScore = 0
            yellowScore = 0
            yellowWins = yellowWins + 1
            if yellowWins == 2:
                print("Yellow team wins the match!")
                matchWinSound()
            else:
                print("Yellow team wins game " + str(currentGame) + "!")
                currentGame = currentGame + 1
                gameWinSound()
