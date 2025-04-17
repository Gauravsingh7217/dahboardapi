from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from .models import Distributor, Agent, Transaction
        db.create_all()

        # ✅ Seed database only if empty
        if not Distributor.query.first():
            db.session.add_all([
                Distributor(name="Dist A"),
                Distributor(name="Dist B"),
                Distributor(name="Dist C")
            ])

        if not Agent.query.first():
            db.session.add_all([
                Agent(name="Agent 1", status="active"),
                Agent(name="Agent 2", status="inactive"),
                Agent(name="Agent 3", status="active")
            ])

        if not Transaction.query.first():
            db.session.add_all([
                Transaction(amount=50000000),
                Transaction(amount=50000000)
            ])

        db.session.commit()

    from .routes import main
    app.register_blueprint(main)

    return app
