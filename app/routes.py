from flask import render_template
#from time import datetime
from app import myapp_obj

@myapp_obj.route('/')
# view functions
def hello():
    return '<h1>hello world</h1>'

# http://127.0.0.1:5000/members/Carlie/
@myapp_obj.route('/members/<string:name>/')
def member(name):
    return render_template('member.html', name=name)

@myapp_obj.route('/home')
def greeting():
    daytimeGreeting = ['Hello!', 'Morning!', 'Afternoon!', 'Evening!', 'Night!']
    greetings = daytimeGreeting[3]
    ''''
    if(datetime.now().hour < 12):
        greeting = daytimeGreeting[1] #morning
    elif(datetime.now().hour < 17):
        greeting = daytimeGreeting[2] #afternoon
    elif(datetime.now().hour < 20):
        greeting = daytimeGreeting[3] #evening
    elif(datetime.now().hour <=24):
        greeting = daytimeGreeting[4] #night
    '''
    
    return render_template('home.html', Greeting=greetings)
    
@myapp_obj.route('/login')
def login():
    abc = {'name':'Carlie'}
    return render_template('login.html', users=abc)

