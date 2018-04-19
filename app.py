#!flask/bin/python
import os
import uuid
from glob import iglob
from json import loads, dumps
from os.path import basename

from dateutil.parser import parse
from flask import Flask, jsonify
from flask import json
from flask import request
from flask_cors import CORS
from flask_graphql import GraphQLView
from flask_restful import Api, reqparse
from werkzeug.utils import secure_filename

from core.database import Database
from core.schema import schema
from core.sql_queries import *
from core.templates import *
from core.utils import combine_files, extract_files

app = Flask(__name__)
api = Api(app)

db = Database()

CORS(app)

parser = reqparse.RequestParser()

rows_to_insert = 10000

UPLOAD_FOLDER = '/Users/carapai/Projects/ugandaemr-openmrs-server/data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def convert_datetime_columns(data, columns):
    selected_element = data[0]
    keys = list(selected_element.keys())

    intersection = set(keys).intersection(columns)

    for d in data:
        d.update((k, parse(v).date().strftime('%Y-%m-%d %H:%M:%S')) for k, v in d.iteritems() if
                 k in intersection and v is not None)
    return data


def convert_boolean_columns(data, columns):
    selected_element = data[0]
    keys = list(selected_element.keys())

    intersection = set(keys).intersection(columns)

    for d in data:
        d.update((k, True if v == 'true' else False) for k, v in d.iteritems() if
                 k in intersection and v is not None)
    return data


def convert_array_to_byte(data, columns):
    selected_element = data[0]
    keys = list(selected_element.keys())

    intersection = set(keys).intersection(columns)

    for d in data:
        d.update((k, v.decode('utf-8')) for k, v in d.iteritems() if
                 k in intersection and v is not None)
    return data


def to_dict(input_ordered_dict):
    return loads(dumps(input_ordered_dict))


def check_registered_facility(facility_uuid):
    facility = db.query_one("select * from facility where uuid = '" + facility_uuid + "'")
    if facility:
        return True
    return False


@app.route('/api/facility', methods=['POST'])
def get_facility():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        facility_name = data['name']
        facility_id = str(uuid.uuid4())
        if facility_name:
            db.insert(add_facility, {'name': facility_name, 'uuid': facility_id})
            return jsonify({
                "response": "Successful",
                'uuid': facility_id
            })
        else:
            return jsonify({
                "response": "Unsuccessful",
                'message': 'You have not supplied the facility name'
            })
    else:
        return "415 Unsupported Media Type ;)"


@app.route('/api/files', methods=['POST'])
def post_file():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return jsonify({
        "response": "Successful",
        'file': filename
    })


@app.route('/api/process', methods=['GET'])
def process_files():
    file_name = request.args.get('file_name')
    if file_name is not None:
        files_combined = combine_files(os.path.join(app.config['UPLOAD_FOLDER']), file_name)
        if files_combined:
            extract_files(os.path.join(app.config['UPLOAD_FOLDER']) + '/' + file_name + '-data.zip',
                          os.path.join(app.config['UPLOAD_FOLDER']) + '/' + file_name + '-data')

            files = [f for f in
                     iglob(
                         os.path.join(os.path.join(app.config['UPLOAD_FOLDER']) + '/' + file_name + '-data', '*.json'))]

            for f in files:
                table = basename(f).split('.')[0]
                query = None
                template = None
                if table == 'obs':
                    template = obs_template
                    query = add_obs
                elif table == 'encounters':
                    template = encounter_template
                    query = add_encounter
                elif table == 'providers':
                    template = provider_template
                    query = add_provider
                elif table == 'person_names':
                    template = person_name_template
                    query = add_person_name
                elif table == 'person_addresses':
                    template = person_address_template
                    query = add_person_address
                elif table == 'person_attributes':
                    template = person_attribute_template
                    query = add_person_attribute
                elif table == 'patients':
                    template = patient_template
                    query = add_patient
                elif table == 'patient_identifiers':
                    template = patient_identifier_template
                    query = add_patient_identifier
                elif table == 'visits':
                    template = visit_template
                    query = add_visit
                elif table == 'encounter_providers':
                    template = encounter_provider_template
                    query = add_encounter_provider
                elif table == 'encounter_roles':
                    template = encounter_role_template
                    query = add_encounter_role

                with open(f) as data_file:
                    data = json.load(data_file)
                    print(len(data))
                    data_chunks = [data[x:x + rows_to_insert] for x in range(0, len(data), rows_to_insert)]

                    for d in data_chunks:
                        if template is not None and table is not None:
                            final_data = [dict(template, **x) for x in d]
                            db.insert_bulk(query, final_data)

            return jsonify({
                "response": "Successful",
                "files": files
            })
        else:
            return jsonify({
                "response": "Unsuccessful",
            })


app.add_url_rule('/api/query', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
