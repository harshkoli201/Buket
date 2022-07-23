from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import false
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bucket.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class bucket(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable = False)
    description = db.Column(db.String(500),nullable = False)
    date = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    

@app.route('/')
def helloworld():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)