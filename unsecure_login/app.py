from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = 'mysecret'  # In production, use a secure and unique secret key

# This is a dummy user store for the sake of demonstration. In real life, you'd use a database.
users = {'username': {'password': 'password123'}}  # This is for a user named 'username' with a password 'password123'

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
        if users.get(username) == None:
            return "Invalid username", 401
        if users[username]['password'] == password:
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('main'))
        return "Incorrect password", 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/pw_reset', methods=['GET', 'POST'])
def pw_reset():

    if request.method == 'POST':
        username = request.form['username']

        # Check if the username exists in your database or user storage
        if username_exists(username):  # Replace with your own function or database check
            # Implement the password reset functionality here.
            # This could involve generating a reset token and sending an email with a reset link, or other logic as per your requirements.

            flash('Password reset instructions sent to your email!', 'success')

            return redirect(url_for('login'))  # Redirecting to a hypothetical 'login' route
        else:
            flash('Username does not exist!', 'danger')

    return render_template('password_reset.html')

def username_exists(username):
    # Implement a check for the existence of a username in your user storage/database.
    # Return True if exists, otherwise False.

    # print(username)

    if username in users:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True, port=5001)