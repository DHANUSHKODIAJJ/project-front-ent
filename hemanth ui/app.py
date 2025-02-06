from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html') 
  
@app.route('/login')
def login():
    return render_template('login.html') 

@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/teacherlog')
def teacher():
    return render_template('teach.html')

@app.route('/studentlog')
def student():
    return render_template('stud.html')

@app.route('/teachreg')
def teachreg():
    return render_template('teachreg.html')

@app.route('/studreg')
def studreg():
    return render_template('studentreg.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     # Retrieve data from the form
#     mobile = request.form['mobile']
#     email = request.form['email']
#     password = request.form['password']
    
#     # Do something with the data (e.g., print it)
#     print(f"Username: {mobile}")
#     print(f"Email: {email}")
#     print(f"Password: {password}")
    
#     return f"Received: Username - {mobile}, Email - {email} and Password - {password}"

if __name__ == '__main__':
    app.run(debug=True)