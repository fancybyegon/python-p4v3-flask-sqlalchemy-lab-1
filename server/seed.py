from app import app, db
from models import Earthquake

with app.app_context():
    db.drop_all()
    db.create_all()

    e1 = Earthquake(magnitude=9.5, location="Chile", year=1960)
    e2 = Earthquake(magnitude=9.2, location="Alaska", year=1964)

    db.session.add_all([e1, e2])
    db.session.commit()

    print("Database seeded!")
