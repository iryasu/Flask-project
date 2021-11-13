from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Welcome! Go to /latin_puppy/name to see you name in puppy latin!</h1>'

@app.route('/latin_puppy/<name>')
def latin_puppy(name):
    latinName = name[:-1]+'iful' if name[-1] == 'y' else name+'y'
    return f'<h1>Hello {name} ! Your puppy latin name is {latinName}</h1>'

if __name__ == '__main__':
    app.run()