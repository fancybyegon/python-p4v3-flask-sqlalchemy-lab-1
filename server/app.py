# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from flask import Flask, jsonify
from models import db, Earthquake


from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    try:
        quake = Earthquake.query.get(id)

        if quake:
            return jsonify(
                id=quake.id,
                location=quake.location,
                magnitude=quake.magnitude,
                year=quake.year
            ), 200
        else:
            return jsonify(message=f"Earthquake {id} not found."), 404
    except Exception as e:
        # Log error to help debug
        return jsonify(message="Internal Server Error", error=str(e)), 500

    
@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    
    quakes_data = [
        {
            "id": quake.id,
            "location": quake.location,
            "magnitude": quake.magnitude,
            "year": quake.year
        } for quake in quakes
    ]

    return jsonify(
        count=len(quakes_data),
        quakes=quakes_data
    ), 200




if __name__ == '__main__':
    app.run(port=5555, debug=True)