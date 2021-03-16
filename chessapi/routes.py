from flask import render_template
from chessapi.models import Todo
from chessapi import app, db

@app.route('/')
def index():
    test = Todo()
    test.content = "test"
    db.session.add(test)
    db.session.commit()

    return render_template('index.html')