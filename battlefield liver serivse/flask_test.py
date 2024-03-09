
import random
import account
from account import Global

from flask import Flask, render_template, request
app = Flask(__name__)


texty = []
random_text = ['no way', 'thats fine', 'right', 'cool text']
accounts = []


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
    return render_template('text.html', text_box = texty)

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

    #new_text = random.choice(random_text)
    if len(new_text) > 0:
        texty.append(new_text)
        while len(texty) > 10:
            texty.remove(texty[0])

    return render_template('text.html', text_box = texty)


if __name__=='__main__': 
   app.debug = True
   app.run()
