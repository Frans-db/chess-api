from chessapi import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f'Todo<{self.id}>'