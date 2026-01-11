from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Yeh mera Flask backend hai."

@app.route('/about')
def about():
    return "Yeh ek simple Flask application hai jo basic routing demonstrate karta hai." 


@app.route('/contact')
def contact():
     return "Aap humse contact kar sakte hain at example@email.com" 

@app.route('/services')
def services():
    return "Humari services mein web development, mobile app development, aur data analysis shamil hain." 

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"Thank you, {name}! We have received your message."
    return 'hello'
if __name__ == '__main__':
    app.run(debug=True)