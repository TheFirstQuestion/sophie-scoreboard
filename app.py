from flask import Flask, render_template, g, redirect, url_for
import sqlite3

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html', data=getAllFromDb())

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='images/favicon.ico'), code=302)


# Database stuff
# http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
DATABASE = 'sophie-scoreboard.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def getAllFromDb():
    return query_db('SELECT * FROM people')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
