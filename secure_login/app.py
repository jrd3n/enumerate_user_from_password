from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import datetime

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = 'mysecret'  # In production, use a secure and unique secret key

# This is a dummy user store for the sake of demonstration. In real life, you'd use a database.
users = {'username': 
                    {'password': 'password123',
                    'next_login_attempt' : None}}  # This is for a user named 'username' with a password 'password123'

LOGIN_DELAY = datetime.timedelta(seconds=6)  # 6 seconds delay between login attempts

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    user = User()
    user.id = username
    return user

@app.route('/')
@login_required
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_data = users.get(username)

        print(user_data)

        # If the user does not exist
        if user_data is None:
            #return "Invalid username", 401
            return render_template('login.html', message='Login not successful!')

        # If the user has a delay set and it has not yet passed
        current_time = datetime.datetime.now()
        if user_data['next_login_attempt'] and current_time < user_data['next_login_attempt']:
            remaining_time = (user_data['next_login_attempt'] - current_time).seconds

            return render_template('login.html', message=f"Please wait {remaining_time} seconds before trying again.")

        # If the password matches
        if user_data['password'] == password:
            # Reset the next_login_attempt
            user_data['next_login_attempt'] = None
            
            # Here's where you would handle successful authentication
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('main'))

        # If the password doesn't match, set the next_login_attempt
        users[username]['next_login_attempt'] = current_time + LOGIN_DELAY

        render_template('login.html', message='Login not successful!')

    message = request.args.get('message')  # Getting the message from URL parameter

    return render_template('login.html', message=message)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/pw_reset', methods=['GET', 'POST'])
def pw_reset():

    if request.method == 'POST':
        username = request.form['username']

        user_data = users.get(username)
        
        if user_data is not None:

            return redirect(url_for('login', message="reset email sent to user!"))  # Redirecting to a hypothetical 'login' route

        else:

            return redirect(url_for('login', message="reset email sent to user!"))  # Redirecting to a hypothetical 'login' route

    return render_template('password_reset.html', message= "")

if __name__ == '__main__':
    app.run(debug=True, port=5000)