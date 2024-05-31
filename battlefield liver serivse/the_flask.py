import sqlite3
import random
import account
from battlefield import iterate_game
from account import Global
#import battlefield.player as player
from battlefield.player import SetClasses
from datetime import timedelta
from battlefield.entity import Stat

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = " 'lag en enkel app' :)Åæ "
app.permanent_session_lifetime = timedelta(hours=32, seconds=1)


#
@app.route('/uid/')
def uid():
    if not "uid" in session:
        session.permanent = True    
        session["uid"] = Global.assign_uid()
        Global.create_account(session["uid"])

    return redirect(url_for("base"))


@app.route('/')
def base():
    
    if "uid" in session:  
        if len(Global.accounts) < 1:
            session.clear()
            return redirect(url_for("uid"))

        for i in Global.accounts:
            if i.uid == int(session["uid"]):
                user = i

        try:
            if user == '':
                pass
        except:
            session.clear()
            return redirect(url_for("uid"))

        stats = []
        if user.player == None or user.name == None:
            stats.append(f'- - -')
        else:
            for i in user.player.list_stats():
                stats.append(i)
        return render_template('main.html', text_box = user.texty, chat_box = Global.chat, player_stats = stats)
    else:
        return redirect(url_for("uid"))


@app.route('/', methods=['POST'])
def base_post():
    game_output: list[str] = [f'', f'', f'/ - - > -']

    if len(Global.accounts) < 1:
        session.clear()
        return redirect(url_for("uid"))

    for i in Global.accounts:
        if i.uid == session["uid"]:
            user = i
            the_player = user.player

    print(f'Action detected from player with UID: {session["uid"]}')

    text = request.form['text']
    input = text.upper()
    previous_text = user.texty

    if len(input) > 0:
        if input == '/UID':
            session.clear()
            return redirect(url_for("uid"))

        if input == '/CLEAR':
            previous_text = ['CLEARED ALL TEXT...']
        #input = random.choice(random_text)
        
        if user.name == None:
            if the_player == None:
                game_output.extend(account.Account.choose_player_class_iteration(user, input))

            if not user.player == None:
                game_output.extend(account.Account.set_name(user, input))

            if not user.player == None and not user.name == None:
                game_output.extend(iterate_game.Game.state_info(user.player, []))

        else:
            game_output.extend(iterate_game.Game.iterate(the_player, input))


        for i in game_output:
            previous_text.append(i)

        while len(user.texty) > 23:
            user.texty.remove(user.texty[0])

        user.texty = previous_text


    text = []
    return redirect(url_for("base"))
    


@app.route('/', methods=['CHAT']) # Unfiltered chat
def update_chat():
    text = request.form['chat']
    text.upper()

    Global.chat.append(text)

    return render_template('text.html')



if __name__=='__main__': 
   app.debug = True
   app.run()
