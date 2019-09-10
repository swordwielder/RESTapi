import json, os
from flask import Flask, request, render_template,jsonify


app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/team', methods=['PUT','GET'])
def displayteam():
    if request.method=='GET':
        return jsonify(teams)

@app.route('/team/<int:id>', methods=['PUT','GET'])
def addtoteam(id):
    newcity = request.args.get('city')
    if request.method=='GET':
        for team in teams:
            if team['id']==id:
                return jsonify(team)
    if request.method=='PUT':
        if newcity:
            for team in teams:
                team['city']=newcity
                return jsonify(team)
    if request.method=='DELETE':
        for team in teams:
            if team['id']==id:
                teams.remove(team)
                return jsonify(teams)
    if request.method=='POST':
        return None


@app.route('/player',methods=['PUT','GET'])
def displayplayer():
    if request.method=='GET':
        return jsonify(players)
    if request.method=='PUT':
        return None

@app.route('/player/<int:id>',methods=['PUT','GET'])
def addtoplayer(id):
    newplayer = request.args.get('name')
    if request.method=='GET':
        for player in players:
            if player['id']==id:
                return jsonify(player)
    if request.method=='PUT':
        if newplayer:
            for player in players:
                player['name']=newplayer
                return jsonify(player)
    if request.method=='POST':
        return None


class Team:
    def __init__(self,id,name,city,fullname,abbrev):
        self.id=id
        self.name=name
        self.city=city
        self.fullname=fullname
        self.abbrev=abbrev

    def __str__(self):
        return f'{self.id},{self.name},{self.city},{self.fullname},{self.abbrev}'


class Player:
    def __init__(self,id,name,team_id):
        self.id=id
        self.name=name
        self.team_id=team_id

    def __str__(self):
        return f'{self.id},{self.name},{self.team_id}'

class Game:
    def __init__(self,id,home_team_id,away_team_id,date):
        self.id=id
        self.home_team_id=home_team_id
        self.away_team_id=away_team_id

    def __str__(self):
        return f'{self.id},{self.home_team_id},{self.away_team_id}'

class Player_Stats:
    def __init__(self,id,game_id,player_id,team_id,points,assists,rebounds,nerd):
        self.id=id
        self.game_id=game_id
        self.player_id=player_id
        self.team_id=team_id
        self.points=points
        self.assists=assists
        self.rebounds=rebounds
        self.nerd=nerd

    def __str__(self):
        return f'{self.id},{self.game},{self.player_id},{self.team_id},{self.team_id},{self.points},{self.assists},{self.rebounds},{self.nerd}'

class Game_State:
    def __init__(self,id,game_id,home_team_score,away_team_score,broadcast,quarter,time_left_in_quarter,game_status):
        self.id=id
        self.game_id=game_id
        self.home_team_score=home_team_score
        self.away_team_score=away_team_score
        self.broadcast=broadcast
        self.quarter=quarter
        self.time_left_in_quarter=time_left_in_quarter
        self.game_status=game_status

    def __str__(self):
        return f'{self.id},{self.game_id},{self.home_team_score},{self.away_team_score},{self.broadcast},{self.quarter},{self.time_left_in_quarter},{self.game_status}'


with open(os.getcwd()+'/data.json' ,'r') as jsonfile:
    data = jsonfile.read()
    jsonfile.close()

jsondata = json.loads(data)
teams_list=jsondata['Teams']
players_list=jsondata['Players']
games_list=jsondata['Games']

print("GAMES LIST", games_list)
teams = []
players=[]
for team in teams_list:
    teams.append(Team(team['id'],team['name'],team['city'],team['full_name'],team['abbrev']).__dict__)

for player in players_list:
    players.append(Player(player['id'],player['name'],player['team_id']).__dict__)



if __name__ == '__main__':
    app.run(debug=True)




