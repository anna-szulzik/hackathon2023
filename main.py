from flask import Flask

from src.app.config.config import db
from src.app.routes import init_routes


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/hackathon'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    init_routes(app)
    return app


app = create_app()

# Run Server
if __name__ == '__main__':
    app.run(port=8000, debug=True)


