from app import app

#The decorators associate the specified URLs to the view function.
#This registers view function as callback for certain events.
@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
