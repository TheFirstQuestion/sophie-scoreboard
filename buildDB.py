import sqlite3

conn = sqlite3.connect('sophie-scoreboard.db')

conn.execute(
    '''
    CREATE TABLE people (
    name    VARCHAR     NOT NULL,
    score   INT         NOT NULL
    );
    '''
)

conn.commit()
conn.close()

if __name__ == "__main__":
    conn = sqlite3.connect('sophie-scoreboard.db')
    conn.execute('INSERT INTO people VALUES ("Sophie 1", 133);')
    conn.execute('INSERT INTO people VALUES ("Sophie 2.2", 133);')
    conn.commit()
    conn.close()
