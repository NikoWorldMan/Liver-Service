import sqlite3
import random
import account
from battlefield import iterate_game
from account import Global
from battlefield.player import Player

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = "Wu7&epk#@£@]9ee9009o340£$]}@}OI=)=!"

player = Player('Magus Supremus', 4, 100, 100, 100, 100, 100, 5, 50, 5, 5, 10, 0, 100)
player.states = [iterate_game.Game.State.IDLE]

test = {"test": "wow"}

class Glob:   
    texty = []


accounts = []


@app.route('/uid/')
def uid():
    session["uid"] = Global.assign_uid()
    redirect(url_for("base"))


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
    return render_template('text.html', text_box = Glob.texty)

@app.route('/', methods=['CHAT']) # Unfiltered chat
def update_chat():
    text = request.form['chat']
    text.upper()

    Global.chat.append(text)

    return render_template('text.html')


@app.route('/', methods=['POST'])
def base_post():
    text = request.form['text']
    new_text = text.upper()
    prev_text = Glob.texty

    if len(new_text) > 0:
        if new_text == '/CLEAR':
            prev_text = ['CLEARED ALL TEXT...']
        #new_text = random.choice(random_text)

        else:
            game_output = iterate_game.Game.iterate(player, new_text)

            for i in game_output:
                prev_text.append(i)

            while len(Glob.texty) > 15:
                Glob.texty.remove(Glob.texty[0])

        Glob.texty = prev_text
        return render_template('text.html', text_box = Glob.texty)


if __name__=='__main__': 
   app.debug = True
   app.run()
