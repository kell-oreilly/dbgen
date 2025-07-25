#import json
from flask import Flask, request
from dbgen import data_generate
from faker import Faker
#import random

app = Flask(__name__)

faker = Faker()

# TODO Store schemas using sqlite 3 to prevent reset
# TODO Catch more exceptions
schemas = {}

# schemas/schema_id/schema
# schemas/schema_id/data/dataid?doc

# Endpoints appcontext/version/recourse?parameter
# Add correctly formatted output to all three
# TODO use header to match schema_name in json file to schema id here
@app.post('/schemas/<string::schema_id>/schema')
def create_schema(schema_id):
    # TODO check schema format is correct, some instances
    # where flask does valid, configure flask to use json instead
    # return errors as json instead of html
    # generate error decorator possibly
    # TODO Fix this
    try:
        schema = request.get_json()
    except ValueError:
        return {
            'error': 'Incorrectly formatted json file'
        }, 400

    # Handle exception url schema id does not match schema name - maybe not could just be redundant

    schema_id = schema['schema_name']
    # Exception schema_id already exists 400
    if schema_id in schemas.keys():
        return {
            'error': f'Schema ID: {schema_id} taken'
        }, 400
    schemas[schema_id] = schema
    return schema, 201  # created

# TODO Delete schema


# TODO Put schema to replace schema


# TODO Patch schema for minor schema edits


@app.get('/schemas')
def get_schemas():
    return schemas, 200  # General ok

# TODO ../schema_idcreateschema
@app.get('/schemas/<string:schema_id>')
def get_data(schema_id):
    n_docs = request.args.get('n_docs', default=3, type=int)
    # Raise requested recourse does not exist 404

    # Exception: n_docs not positive interger

    # 201 if data saved to recourse - store somewhere
    return data_generate(schemas[schema_id], n_docs), 200


# TODO Post generated data


# TODO Post generated data


# TODO PUT modify generated data
