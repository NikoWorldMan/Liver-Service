import sqlite3
import random
import account
from battlefield import iterate_game
from account import Global
from battlefield.player import Player
from datetime import timedelta

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = "whatthefucisaflask"
app.permanent_session_lifetime = timedelta(days=2)

player = Player('Magus Supremus', 4, 100, 100, 100, 100, 100, 5, 50, 15, 5, 500, 0, 100)
player.states = [iterate_game.Game.State.IDLE]

test = {"test": "wow"}

class Glob:   
    texty = []


accounts = []

@app.route('/sus/')
def sus():
    session.pop("uid", None)
    return redirect(url_for("base"))

@app.route('/uid/')
def uid():
    if not "uid" in session:
        session.permanent = True
        session["uid"] = Global.assign_uid()
    return redirect(url_for("base"))


@app.route('/ca') # Currently test, supposed to create account
def join():
    
    new_account = account.Account(None)
    accounts.append(new_account)
    return new_account.print_info()

@app.route('/main-test') # Test site, will probably not be used
def main_test():

    return render_template('main.html')

@app.route('/')
def base():
    if "uid" in session:
        return render_template('text.html', text_box = Glob.texty)
    else:
        return redirect(url_for("uid"))



@app.route('/', methods=['POST'])
def base_post():

    print(session["uid"])
    
    text = request.form['text']
    new_text = text.upper()
    prev_text = Glob.texty

    if len(new_text) > 0:
        if new_text == '/CLEAR':
            prev_text = ['CLEARED ALL TEXT...']
        #new_text = random.choice(random_text)

        else:
            game_output: list[str] = [f'', f'', f'/ - - > -']
            game_output.extend(iterate_game.Game.iterate(player, new_text))

            for i in game_output:
                prev_text.append(i)

            while len(Glob.texty) > 24:
                Glob.texty.remove(Glob.texty[0])

        Glob.texty = prev_text


    text = []
    return render_template('text.html', text_box = Glob.texty)
    


@app.route('/', methods=['CHAT']) # Unfiltered chat
def update_chat():
    text = request.form['chat']
    text.upper()

    Global.chat.append(text)

    return render_template('text.html')



if __name__=='__main__': 
   app.debug = True
   app.run()
