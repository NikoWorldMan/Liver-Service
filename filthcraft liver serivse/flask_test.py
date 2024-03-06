
import random
from flask import Flask, render_template
app = Flask(__name__)

text = ['','','','','']

random_text = ['no way', 'thats fine', 'right', 'cool text']




@app.route('/lolo')
def helo():

    new_text = random.choice(random_text)

    text.append(new_text)

    while len(text) > 5:
        text.remove(text[0])

    return text

@app.route('/')
def main():
    return render_template('text.html', text_box = text)


if __name__=='__main__': 
   app.run( debug=True )



