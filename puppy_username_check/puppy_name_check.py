from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/username_check')
def username_check():
    username = request.args.get('username')
    requirements = [
        'Must have an upper case letter somewhere',
        'Must have a lower case letter somewhere',
        'Must have a number at the end'
        ]
    check = check_reqs(username)
    if check[0] or check[1] or check[2]:
        return render_template('fail.html', username=username, requirements=list(zip(check,requirements)))
    else:
        return render_template('pass.html', username=username)
    

    



def check_reqs(username):
    check = [True, True, not username[-1] in '0123456789']
    for letter in username:
        if letter == letter.upper() and letter not in '0123456789':
            check[0] = False
        if letter == letter.lower() and check[1]:
            check[1] = False
        if not check[0] and not check[1]:
            break
    return check



if __name__ == '__main__':
    app.run(debug=True)