import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

wharehouse = [
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
    return '''<h1>Wharehouse Control API</h1>
<p>A prototype API for reading and updating remote wharehouses</p>'''


@app.route('/api/v1/wharehouse/all', methods=['GET'])
def api_all():
    return jsonify(wharehouse)


@app.route('/api/v1/wharehouse', methods=['GET'])
def api_id():
    query_parameters = request.args

    id = query_parameters.get('id')
    zone_1 = query_parameters.get('zone_1')
    zone_2 = query_parameters.get('zone_2')
    zone_3 = query_parameters.get('zone_3')

    results = []

    for w in wharehouse:
        if w['id'] == id:
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
