from flask import render_template
from app import app

#The decorators associate the specified URLs to the view function.
#This registers view function as callback for certain events.
@app.route('/')
@app.route('/index')
def index():
    #Define a user variable.
    user = {'username': 'Gerardo'}
    #Define a list of posts.
    posts = [
    {
        'author':'Pepe',
        'body':'Esto es un mensaje de prueba!'
    },
    {   'author':'Guarumo',
        'body':'Woof woof! Soy un perro?'
    },
    {
        'author':'Genaro',
        'body':'Buscando trabajo de dev!'
    }
    ]
    #Function render_Template from flask renders an HTML file and assign the arguments.
    return render_template('index.html', user=user, posts=posts)

@app.route('/contact')
def contact():
    info = {'admin':'Gerardo Mantecon',
            'mail':'gerardo@mail.com',
            'phone':'1234567',
            'address':'666 Fake St, Ontario, Canada.'}
    return render_template('contact.html', info=info)
