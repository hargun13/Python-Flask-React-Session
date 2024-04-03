from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user credentials
users = {
    'ROHIT': 'C123'
}

# List to store posts
posts = []

# Route for the home page
@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', posts=posts, username=session['username'])
    else:
        return redirect(url_for('login'))

# Route for logging in
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message='Invalid username or password.')
    return render_template('login.html', message='')

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# Route for submitting a post
@app.route('/submit', methods=['POST'])
def submit_post():
    if 'username' in session:
        post_content = request.form['post_content']
        posts.append(post_content)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
