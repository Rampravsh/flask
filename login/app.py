from flask import Flask, request, redirect, url_for, session, render_template
app = Flask(__name__)
app.secret_key = 'rampravesh kumar'

# homepage login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == '123':
            session['user'] = username
            return redirect(url_for('welcome'))
        else:
            return render_template('invalid.html')
        
    return render_template('login.html')

# welcome page 
@app.route("/welcome")
def welcome():
    if 'user' in session:
        return render_template('welcome.html', user=session['user'])
    return redirect(url_for('login'))

# logout route 
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)