import flask
from flask import request, jsonify

from flask_cors import CORS
app = flask.Flask(__name__)
app.config["DEBUG"] = True
# fix the CORS issue of same port accessing
CORS(app)
#  replace with a database or cython files pulling info off the sensors
warehouse = [
    {'id': 0,
     'title': 'Tool and Dye',
     'owner': 'John Smith',
     'zone_1_temp': 34.5,
     'zone_2_temp': 36.5,
     'zone_3_temp': 46.5,
     },
    {'id': 1,
     'title': 'Hill Street Steel',
     'owner': 'Andrew Jackson',
     'zone_1_temp': 54.5,
     'zone_2_temp': 46.5,
     'zone_3_temp': 43.5,
     }

]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Warehouse Control API</h1>
<p>A prototype API for reading and updating remote warehouses</p>'''


@app.route('/api/v1/warehouse/all', methods=['GET'])
def api_all():
    return jsonify(warehouse)


@app.route('/api/v1/warehouse', methods=['GET'])
def api_id():
    query_parameters = request.args

    id = query_parameters.get('id')
    zone_1 = query_parameters.get('zone_1')
    zone_2 = query_parameters.get('zone_2')
    zone_3 = query_parameters.get('zone_3')
    

    results = []

    for w in warehouse:
        if w['id'] == int(id):
            results.append(w)
        if zone_1 and w['zone_1_temp'] > int(zone_1):
            results.append(w)
        if zone_2 and w['zone_2_temp'] > int(zone_2):
            results.append(w)
        if zone_3 and w['zone_3_temp'] > int(zone_3):
            results.append(w)

    return jsonify(results)

if __name__ == "__main__":
    app.run()
