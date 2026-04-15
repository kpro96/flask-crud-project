from flask import Flask
from flask_sqlalchemy import SQLAIchemy 
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db= SQLAIchemy(app)

class User(db.Model):
    id= db.Column(db.integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    with  app.app_context():
        db.create_all()
@app.route('/')
def hello():
    return "Database connection!" 
if__name__== "__main__":app.run(debug=True)   