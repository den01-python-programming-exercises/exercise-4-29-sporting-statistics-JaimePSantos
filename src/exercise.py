import csv
def main():
    #write your code below this line
    fileName = input("File:")
    teamName = input("Team:")
    games = 0
    wins = 0
    losses = 0
    with open(fileName) as f:
      reader = csv.reader(f,delimiter=',')

      for team in reader:
        if(teamName==team[0]):
          games+=1
          if(int(team[2])>int(team[3])):
            wins+=1
          if(int(team[3])>int(team[2])):
            losses+=1
            # print("HomeTeamLoss")

        if(teamName==team[1]):
          games+=1
          if(int(team[3])>int(team[2])):
            wins+=1
          if(int(team[2])>int(team[3])):
            losses+=1
            # print("AwayTeamLoss")

    
      print("Games: %s"%games)
      print("Wins: %s"%wins)
      print("Losses: %s"%losses)


if __name__ == '__main__':
    main()
