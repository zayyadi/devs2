from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgres://ytdbqumpjfscjt:4b4e292afc9f625ba372a26ce5dde8b7020df316e91a4f81faea27a93accbb3e@ec2-54-147-54-83.compute-1.amazonaws.com:5432/dnbg4eods0163'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()