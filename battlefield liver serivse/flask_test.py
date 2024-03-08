
import random
import account

from flask import Flask, render_template
app = Flask(__name__)

text = ['','','','','']

random_text = ['no way', 'thats fine', 'right', 'cool text']

accounts = {}


@app.route('/')
def join():
    
    new_account = account.Account(None)

    accounts.append(new_account)

    return new_account.print_info()

@app.route('/l')
def helo():

    new_text = random.choice(random_text)
    text.append(new_text)
    while len(text) > 5:
        text.remove(text[0])
    return text

@app.route('/k')
def main():
    return render_template('text.html', text_box = text)

@app.route('/gg')
def test():

    return render_template('test.html')


@app.route('/lll')
def mm():

    return render_template()

if __name__=='__main__': 
   app.run( debug=True )



