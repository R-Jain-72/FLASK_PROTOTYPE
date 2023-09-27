from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

# create a route decorator

#def index():
#    return "<h1> Hello World</h1>"

def index():
    f_name = 'Crypto'
    stuff = 'This is bold: <strong> BOLD </strong> '
    to_do_list = ['Work','Cook','Play']
    return render_template('index.html', f_name = f_name, stuff = stuff, to_do_list = to_do_list)

# Localhost:5000/user/jj

@app.route('/user/<name>')
#def user(name):
#    return "<h1> Hello {}</h1>".format(name)
def user(name):
    return render_template('user.html', user_name=name)

# create a custom error page

#for invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#for an internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500