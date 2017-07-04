from flask import Flask, request, redirect, render_template
import cgi

# TODOS:
#       -add regex validation (optional)

app = Flask(__name__)
app.config['DEBUG'] = True

def validate_input(input):
    ''' validates all user inputs and returns True/False based on requirements met '''
    if len(input) < 3 or len(input) > 20:
        return False
    for c in input:
        if c == " ":
            return False
    return True

def check_user(username):
    ''' returns username/error values after validation '''
    if validate_input(username) == False:
        username_error = "That's not a valid username, please enter a username between 3-20 characters."
        username = ""
    else:
        username_error = ''
    return username, username_error

def check_pass1(pass1):
    ''' returns initial password error message after validation '''
    if validate_input(pass1) == False:
        password1_error = "That's not a valid password, password must be between 3-20 characters."
    else: 
        password1_error = ''
    return password1_error

def check_pass2(pass2, pass1):
    ''' validates second password field and returns second password error message '''
    if pass2 != pass1:
        password2_error = "Passwords don't match, please try again."
    else:
        password2_error = ''
    return password2_error 

def check_email(email):
    ''' validates non-empty email fields and returns email/error message values '''
    req_values = 0

    if len(email) == 0:
        email_error = ''
    
    for c in email:
        if c == '@' or c == '.':
            req_values += 1

    if validate_input(email) == False or req_values != 2:
        email = ''
        email_error = "Please enter a valid email (between 3-20 characters, no spaces, contains @ and .)"
    
    if req_values == 2:
        email_error = ''   
    
    return email, email_error

@app.route("/", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        ''' displays initial signup screen '''
        return render_template('signup.html')
    
    if request.method == "POST":
        ''' validates all user inputs on signup screen '''
        username, username_error = check_user(username = request.form['username'])
        password1_error = check_pass1(pass1 = request.form['pass1'])
        password2_error = check_pass2(pass2 = request.form['pass2'], pass1 = request.form['pass1'])
        email, email_error = check_email(email = request.form['email'])
        error_messages = username_error + password1_error + password2_error + email_error
        
        if len(error_messages) > 0:
            return render_template('signup.html', 
            username = username, username_error = username_error, 
            pass1_error = password1_error, pass2_error = password2_error,
            email = email, email_error = email_error)
        else:
            return render_template('welcome.html', username = username)

app.run()