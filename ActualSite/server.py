from flask import Flask, render_template, url_for, request
import os
import time
import sys
import whoosh
import os
import csv
import json
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser
import uuid

sys.path.append("./") # Any imports below this will come from the PikaPedia directory

app = Flask(__name__)


def readtextfile(x):
    Teams = {}
    with open(x,'r') as inf:
        Teams = eval(inf.read())
    return Teams


#############################################################################
# Page 1:
@app.route('/', methods=['GET', 'POST'])
def Homepage():
    if request.method == 'POST':
        data = request.form
    else:
        data = request.args

    sportList = ['Soccer','Footbal','Baseball','Hockey','kickball']

    return render_template('Homepage.html', sportList=sportList)

#############################################################################
# Page 2:
@app.route('/Gamepage', methods=['GET', 'POST', 'sport'])
def Gamepage():
    data = request.args

    sport = data.get('sport')
    GamesList = ['game1','game2','game3']

    return render_template('Gamepage.html', sport=sport, GamesList=GamesList)

#############################################################################
# Page 3:
@app.route('/Teampage', methods=['GET', 'POST', 'team1', 'team2', 'game', 'sport'])
def Teampage():
    data = request.args

    game = data.get('game')
    team1 = data.get('team1')
    team2 = data.get('team2')
    sport = data.get('sport')

    return render_template('Teampage.html', team1=team1, team2=team2, game=game, sport=sport)

#############################################################################
# Bet Page:
@app.route('/Betpage', methods=['GET', 'POST', 'team', 'game', 'sport'])
def Betpage():
    data = request.args

    game = data.get('game')
    team = data.get('team')
    sport = data.get('sport')

    pub_key = uuid.uuid4().hex

    return render_template('Betpage.html', team=team, game=game, sport=sport, pub_key=pub_key)


#lets you make changes and view in browser.
#Found at URL: http://flask.pocoo.org/snippets/40/
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
	app.run(debug=True)

'''
#Loads Search Page for pokemon
#
@app.route('/', methods=['GET', 'POST'])
def TeamDisplayHomepage():
	if request.method == 'POST':
		data = request.form
	else:
		data = request.args

	#Game Variables
	# GameArray: Array of current games  for the week.

	week = ('week'+str(1)+'Bare.out')
	filename = './static/Storage/weeks/'+(week)

	Games = readtextfile(filename)

	hashArray = []
	for num in range(len(Games)*2):
		hashArray.append(num+1)

	print(Games)
	return render_template('TeamDisplayHomepage.html',
	#VFariables passed into HTML go here
	 Games=Games,
	 hashArray=hashArray)

#Loads Single Page for individule pokemon
#
@app.route('/SinglePokemonLoadPage', methods=['GET', 'POST', 'pokemonInfo', 'query'])
def SinglePokemonLoadPage():
    if request.method == 'POST':
        data = request.form
    else:
        data = request.args

	#String passed into funciton form Homepage
    info = data.get('pokemonInfo')


    lengthInfo = len(info)

    info = json.loads(info.replace("'", '"'))

	#Stores variables that will later be passed into the page
    name = info['name']
    id = info['id']
    idInt = int(id)
    type_1 = info['type_2']
    type_2 = info['type_1']
    ability_1 = info['ability_1']
    ability_2 = info['ability_2']
    moves = info['moves']
    first_form = info['first_form']
    second_forms = info['second_forms']
    third_forms = info['third_forms']
    pokemonEvo2Length = len(second_forms)
    pokemonEvo3Length = len(third_forms)

    return render_template('SinglePokemonLoadPage.html',
    #Variables for web page
        name=name,
        id=id,
        type_1=type_1,
        type_2=type_2,
        hp = info['hp'],
        attack = info['attack'],
        defense = info['defense'],
        sp_atk = info['sp_atk'],
        sp_def = info['sp_def'],
        speed = info['speed'],
        height = int(info['height']),
        weight = int(info['weight']),
        ability_1=ability_1,
        ability_2=ability_2,
        hidden_ability=info['ability_hidden'],
        moves=moves,
        first_form=first_form,
        second_forms=second_forms,
        third_forms=third_forms,
        idInt=idInt,    #used for Counter in HTML
        moveList=moves, #Holds Moves List
        pokemonEvo2Length=pokemonEvo2Length,
        pokemonEvo3Length=pokemonEvo3Length)
'''
