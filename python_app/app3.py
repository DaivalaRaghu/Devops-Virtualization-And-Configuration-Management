from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def form():
    return '''
    <h2>College Registration Form</h2>
    <form method="POST" action="/submit">
        Name:<br>
        <input type="text" name="name"><br><br>

        Course:<br>
        <input type="text" name="course"><br><br>

        Email:<br>
        <input type="email" name="email"><br><br>

        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    course = request.form['course']
    email = request.form['email']

    return f'''
    <h2>Registration Successful</h2>
    Name: {name} <br>
    Course: {course} <br>
    Email: {email}
    '''

app.run(host='0.0.0.0', port=5000)