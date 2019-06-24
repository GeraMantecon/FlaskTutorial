from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    # Method validate_on_submit returns false if GET and true if POST.
    # Since we want to receive data we expect a POST.
    if form.validate_on_submit():
        flash('Login requested for {} , remember me {}'.format(
            form.username.data,
            form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Log In',form=form)
