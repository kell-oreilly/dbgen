from faker import Faker
import json
from flask import Flask, request

app = Flask(__name__)

faker = Faker()


def init():
    print('Welcome to the Database Generator!!\n')
    u_instructions()

# Add email, add consideration of generation restraints, PEP8,
# User instructions call
# Allow user to go back if mistake made
# Consder data format (string,int), return empty file for 0 docs
# Up to us to decide 0 docs - consider user story
# Seperate first/last name entries - allow option but not if full name used
# Add specification of output format (json, xml)


# Call during init, and be recallable whenever user needs
def u_instructions():
    print('When prompted')
    print('Input schema key_name and datatype for documents')
    print('Available datatypes:')
    print('-- Identification [id]')  # Format
    print('-- Name [f_name]')  # Name origin
    print('-- Birthdate [dob]')  # Birthdate range
    print('-- IP Address [ip]')
    print('-- email Address [email]')
    # print('-- Home Address [address]')
    print('Use exact spelling (case sensitive).')
    print('Then input the number of documents to generate\n')


# TODO Add arguments, nested dictionary where lambda funcs are, have terminal
valid_dtypes = {
    'id': None,
    'name': lambda: faker.name(),  # TODO Add options for f/l name
    'dob': lambda: faker.date(),  # birthdate({mode: 'age', min: 18, max: 65}),
    'ip': lambda: faker.ipv4(),
    'email': lambda: faker.email()  # TODO Make email name consistent across
                                    # name and email
}


# Taking input, generating schema bp
def usr_schema_build():
    usr_schema = {}

    # Schema Blueprint - Add u_instructions help
    while True:
        key = input('Enter key name or type "finished": ')
        while key in usr_schema.keys():
            print('Duplicate key name found\nEnter an original key name')
            key = input('Enter key name or type "finished": ')
            if key == 'finished':
                break
        if key == 'finished':
            break

        while True:
            dtype = input(f'Enter {key} datatype or type "rename": ')
            if dtype == 'rename':
                break
            if dtype not in valid_dtypes.keys():
                print('\nPlease enter a valid datatype')
                continue
            usr_schema[key] = dtype
            break
        # TODO SELECTING DTYPE OPTIONS HERE, ADD to inschema as tuple,
        # Print user options for dtype etc
        # Consider if multiple while loops best method
        # Add ability to redo datatype if mistake
        # Possibly just confirm keyname with datatype and options before
        # moving to next key
    return usr_schema


# Taking in number docs
def usr_num_docs():
    while True:
        try:
            usr_n_docs = int(input('How many documents would you like?: '))
            if usr_n_docs <= 0:
                print('\nPlease enter a positive integer number')
                continue
        except ValueError:
            print('\nPlease enter a positive integer number')
            continue
        break
    return usr_n_docs


def data_generate(schema, n_docs):
    gen_data = []

    for i in range(n_docs):
        doc = {}
        for key, dtype in schema.items():
            if dtype == 'id':
                doc[key] = i + 1
            else:
                doc[key] = valid_dtypes[dtype]()
        gen_data.append(doc)

    return gen_data


def main():
    init()

    # MainGeneration
    schema = usr_schema_build()
    # TODO Save schema to json file
    num_docs = usr_num_docs()
    generated_data = data_generate(schema, num_docs)

    # json_schema = json.dumps(schema, indent=2)
    # print(f'Schema:\n{json_schema}')
    print('\nData:')
    for doc in generated_data:
        print(json.dumps(doc))


if __name__ == "__main__":
    main()


# TODO Store schemas using sqlite 3 to prevent reset
# TODO Catch more exceptions
schemas = {}


# Endpoints appcontext/version/recourse?parameter
# Add correctly formatted output to all three
@app.post('/schemas/<string:schema_id>')
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