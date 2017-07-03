from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

def check_user(username):
    if len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username, please enter a username between 3-20 characters."
        username = ""
    else:
        username_error = ''
    return username, username_error

def check_pass1(pass1, pass2):
    if len(pass1) < 3 or len(pass1) > 20:
        password1_error = "That's not a valid password, password must be between 3-20 characters."
        password1 = ''
        password2 = ''
    else: 
        password1_error = ''
    return password1, password1_error

def check_pass2(pass2, pass1):
    if pass2 != pass1:
        password2_error = "Passwords don't match, please try again."
        password2 = ''
        password1 = ''
    else:
        password2_error = ''
    return password2, password2_error 

# def check_email

@app.route("/", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        ''' displays initial signup screen '''
        return render_template('signup.html')
    
    if request.method == "POST":
        ''' validates all user inputs on signup screen '''
        username, username_error = check_user(username = request.form['username'])
        password1, password1_error = check_pass1(pass1 = request.form['pass1'], pass2 = request.form['pass2'])
        password2, password2_error = check_pass2(pass2 = request.form['pass2'], pass1 = password1)
        # email, email_error = check_email(email = request.form('email'))
        email = request.form['email']
        email_error = ''
        error_messages = username_error + password1_error + password2_error 
        # + email_error
        
        if len(error_messages) > 0:
            return render_template('signup.html', 
            username = username, username_error = username_error, 
            pass1_error = password1_error, pass2_error = password2_error,
            email = email, email_error = email_error)
        else:
            return render_template('welcome.html', username = username)

# @app.route('/welcome', methods=["GET",'POST'])
# def welcome_user():
#     username = request.form['username']
#     return render_template('welcome.html', name = username)

app.run()

# pass1 = password1,