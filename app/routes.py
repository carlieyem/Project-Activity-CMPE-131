from flask import render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app import myapp_obj

class HomeForm(FlaskForm):
    submit = SubmitField('Login')
    submit = SubmitField('Button2')
    submit = SubmitField('Button3')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')


@myapp_obj.route('/')
# view functions
def hello():
    return '<h1>hello world</h1>'

# http://127.0.0.1:5000/members/Carlie/
@myapp_obj.route('/members/<string:name>/')
def member(name):
    return render_template('member.html', name=name)

@myapp_obj.route('/home', methods=['GET', 'POST'])
def greeting():
    form = HomeForm()
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
    if form.validate_on_submit('Login'):
        return redirect('login')
    return render_template('home.html', Greeting=greetings, form=form)
    
@myapp_obj.route('/login')
def login():
    form = LoginForm()
    abc = {'name':'Carlie'}
    if form.validate_on_submit('Submit'):
        return redirect('/members/' + abc)
    return render_template('login.html', users=abc, form=form)

