import flask
from models import Epost


#app can be anything
app = flask.Flask("app")

@app.route("/login")
def login():
    return flask.render_template("login.html")

@app.route("/auth") #flask request args get. html to python
def auth():
    #old/in the back = flask.request.form.get("username")
    #new/frontend = flask.request.args.get("username")
    username = flask.request.args.get("username")
    password = flask.request.args.get("password")

    # test if it works
    #return f"{username} : {password}"

    if not username.lower() == "admin":
        flask.abort(403) # Other outputs: -User does not exist
    if not password == "123":
        flask.abort(403) # Other outputs: -Wrong password

    # TODO: this is a reminder to potentially sett session to "Logged in" = True
    #  Krever oppsett av Flask-Session (Google it)

    #return f"welcome {username}! conglatsulations a winner is you."
    return flask.redirect("/")

# '/' == Root, home
@app.route('/')
def get_index():
    return flask.render_template('index.html')

@app.route('/chapter2')
def get_index_page2():
    return 'delicious'

# <> blir et parameter
@app.route('/Hello/<name>')
def get_hello(name): #when name turned white it was used.
    return 'Hello ' + name

@app.route('/sandbox')
def get_sandbox():
    return flask.render_template('sandbox.html')

@app.route('/calc/<num1>/<op>/<num2>')
def calc_sum(num1, op, num2):
    number1 = int(num1)
    number2 = int(num2)

    match op:
        case '+':
            return str(number1 + number2)
        case '-':
            return str(number1 - number2)
        case '*':
            return str(number1 * number2)
        case ':':
            return str(number1 / number2)
        case _:
            return 'Please input valid operation'

@app.route('/epost/<epost>')
def gyldig_epost(epost):
    try:
        return str(Epost(epost))
    except ValueError:
        return 'error ugyldig e-post'


from src import jokes


@app.route('/joke/random')
def joke_random():
    joke = jokes.get_random()
    return flask.render_template('joke.html', joke=joke)

@app.route('/joke/<search>')
def joke_search(search):
    joke = jokes.get_search(search)
    return flask.render_template('joke.html', joke=joke)
#how?
@app.route('/joke/category/<category>')
def joke_category(category):
    joke = jokes.get_category(catagory)
    return flask.render_template('joke.html', joke=joke)


app.debug = True

app.run()
print('too fast you crash')
