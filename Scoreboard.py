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



    def winner(self, team):
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

    def playSoundEffect(self, type):
        if(type != null):
            sounds = os.listdir('./Sounds/' + type + '/')
            soundToPlay = str('/Sounds/' + type + '/' + random.choice(sounds))
        else:
            print("Something went wrong when trying to play a sound...")

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
        currentGame = self.currentGame + 1
        if(self.teamAWins < 2 and self.teamBWins < 2):
            print('Game ' + str(currentGame) + ' starting. Switch sides!')
        if(self.teamAWins == 2):
            return scoreboard.winner(self.teamASide)
        if(self.teamBWins == 2):
            return scoreboard.winner(self.teamBSide)
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