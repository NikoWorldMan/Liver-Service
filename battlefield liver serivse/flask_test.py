
import random
import account
from account import Global

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = "Wu7&epk#@£@]9ee9009o340£$]}@}OI=)=!"



test = {"test": "wow"}

class Glob:   
    texty = []

random_text = ['no way', 'thats fine', 'right', 'cool text']
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

    if new_text == '/CLEAR':
        prev_text = ['CLEARED ALL TEXT...']
    else:
        #new_text = random.choice(random_text)
        if len(new_text) > 0:
            prev_text.append(new_text)
            while len(prev_text) > 10:
                prev_text.remove(prev_text[0])

    Glob.texty = prev_text
    return render_template('text.html', text_box = Glob.texty)


if __name__=='__main__': 
   app.debug = True
   app.run()
