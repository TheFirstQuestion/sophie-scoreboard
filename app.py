from flask import Flask, render_template, g, redirect, url_for, request
import sqlite3

app = Flask(__name__)

# Database stuff
conn = sqlite3.connect('sophie-scoreboard.db')

def getAllFromDb():
    return conn.execute('SELECT * FROM people').fetchall();




@app.route("/")
def main():
    return render_template('index.html', people=getAllFromDb())

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='images/favicon.ico'), code=302)


# Backend processing
@app.route('/addPerson', methods=['POST', 'GET'])
def addPerson():
    # Get values from AJAX request
    name = request.form["name"]
    points = request.form["points"]
    # Insert new user into database
    conn.execute('INSERT INTO people VALUES (?, ?);', [name, points])
    conn.commit()
    # Redirect to /
    return "/"

@app.route('/addPoints', methods=['POST', 'GET'])
def addPoints():
    # Get values from AJAX request
    name = request.form["name"]
    points = request.form["points"]
    # Get user current points
    person = conn.execute('SELECT * FROM people WHERE name = (?)', (name,)).fetchall();
    currentPoints = person[0][1]
    # Update new point value
    newPoints = currentPoints + int(points)
    conn.execute('UPDATE people SET score = (?) WHERE name = (?)', (newPoints, name))
    conn.commit()
    # Redirect to /
    return "/"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
