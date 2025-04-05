import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

def get_db():
    """Create a new database connection for each request."""
    connection = sqlite3.connect("birthdays.db")
    connection.row_factory = sqlite3.Row  # This makes rows behave like dictionaries
    return connection

@app.route('/', methods=['GET', 'POST'])
def AddBirthday():
    if request.method == 'POST':
        name = request.form.get('name')
        month = request.form.get('month')
        day = request.form.get('day')
        
        if not name or not month or not day:
            return "Name, Month and Day are required."
        
        db = get_db()
        db.execute('INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)', (name, month, day))
        db.commit()
        db.close()
        return redirect('/')
    birthdays = get_birthdays()
    return render_template('index.html', birthdays=birthdays, body_id='indexpage')

def get_birthdays():
    db = get_db()
    birthdays = db.execute('SELECT * FROM birthdays').fetchall()
    db.close()
    return birthdays

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_birthday(id):
    db = get_db()
    if request.method == 'POST':
        name = request.form.get('name')
        month = request.form.get('month')
        day = request.form.get('day')
        
        if not name or not month or not day:
            return "Name, Month and Day are required."
        
        db.execute('UPDATE birthdays SET name = ?, month = ?, day = ? WHERE id = ?', (name, month, day, id))
        db.commit()
        return redirect('/')
    
    birthday = db.execute('SELECT * FROM birthdays WHERE id = ?', (id,)).fetchone()
    db.close()
    return render_template('edit.html', birthday=birthday, body_id='editpage')


@app.route('/delete/<int:id>', methods=['POST'])
def delete_birthday(id):
    db = get_db()
    db.execute('DELETE FROM birthdays WHERE id = ?', (id,))
    db.commit()
    db.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)