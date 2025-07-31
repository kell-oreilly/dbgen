from faker import Faker
import json

# import json
# from flask import Flask, request

# app = Flask(__name__)

faker = Faker()


#def init():  # pragma: no cover
#    print('Welcome to the Database Generator!!\n')  # pragma: no cover
#    u_instructions()  # pragma: no cover

# Add email, add consideration of generation restraints, PEP8,
# User instructions call
# Allow user to go back if mistake made
# Consder data format (string,int), return empty file for 0 docs
# Up to us to decide 0 docs - consider user story
# Seperate first/last name entries - allow option but not if full name used
# Add specification of output format (json, xml)


# Call during init, and be recallable whenever user needs
<<<<<<< HEAD:dbgen.py
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
=======
#def u_instructions():  # pragma: no cover
#    print('When prompted')  # pragma: no cover
#    print('Input schema key_name and datatype for documents')  # pragma: no cover
#    #dtype_instructions()
#    print('Then input the number of documents to generate\n')  # pragma: no cover


#def dtype_instructions():  # pragma: no cover
#    print('Available datatypes:')  # pragma: no cover
#    print('-- Identification [id]')  # pragma: no cover
#    print('-- Name [f_name]')  # pragma: no cover
#    print('-- Birthdate [dob]')  # pragma: no cover
#    print('-- IP Address [ip]')  # pragma: no cover
#    print('-- email Address [email]')  # pragma: no cover
#    # print('-- Home Address [address]')  # pragma: no cover
#    print('Use exact spelling (case sensitive).')  # pragma: no cover
>>>>>>> origin/dbgen_w_parameters:databasegen/dbgen.py


# TODO Add arguments, nested dictionary where lambda funcs are, have terminal
valid_dtypes = {
<<<<<<< HEAD:dbgen.py
    'id': None,
    'name': lambda: faker.name(),  # TODO Add options for f/l name
    'dob': lambda: faker.date(),  # birthdate({mode: 'age', min: 18, max: 65}),
    'ip': lambda: faker.ipv4(),
    'email': lambda: faker.email()  # TODO Make email name consistent across
                                    # name and email
}


=======
    'id': lambda i, opts={}: i + 1,
    'f_name': lambda i, opts={}: faker.first_name(),
    'l_name': lambda i, opts={}: faker.last_name(),
    'date': lambda i, opts={}: faker.date_between(
        start_date=opts.get('start_date', '-30y'),
        end_date=opts.get('end_date', 'now')
    ).isoformat(),
    'ip': lambda i, opts={}: faker.ipv4(
        network=opts.get('network', 'False'),
        address_class=opts.get('address_class', 'None'),
        private=opts.get('private', 'None')
    ),
    'email': lambda i, opts={}: f"{opts.get('first', faker.first_name())}.{opts.get('last', faker.last_name())}@{faker.free_email_domain()}".lower(),
    'country_code': lambda i, opts={}: faker.country_code(representation="alpha-2"),
    'price': lambda i, opts={}: f"{opts.get('currency', '$')}{random.uniform(opts.get('min', 0), opts.get('max', 1000)):.{opts.get('dec', 2)}f}",
    'para': lambda i, opts={}: faker.paragraph(nb_sentences=opts.get('sentences', 3)),
    'bool': lambda i, opts={}: bool(random.getrandbits(1)),
    'job': lambda i, opts={}: faker.job(),
    'company': lambda i, opts={}: faker.company()
    #file type (mp3,wav...)
    #address - connected to country code possibly
    #gender
    #prefix - connected to gender, fname,lname
    #date_time
    #member since- make greater than sme dob value
    #actions
    #'int': lambda i, opts={}:,
    #'string': lambda i, opts={}:,
    #'set': lambda i, opts={}: random.choice(opts.get('list', []))
}


# convert options input into dictionary format
def convert_opts(opt_str):
    try:
        return dict(
            (k.strip(), int(v) if v.strip().isdigit() else v.strip())
            for k, v in (pair.split("=") for pair in opt_str.split(","))
        )
    except Exception:
        print("Please use valid options format: key=value, key2=value2...")
        print("For 'set', use  'list', as key and [item1,item2...] as value")

        return None


>>>>>>> origin/dbgen_w_parameters:databasegen/dbgen.py
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
<<<<<<< HEAD:dbgen.py
            usr_schema[key] = dtype
            break
        # TODO SELECTING DTYPE OPTIONS HERE, ADD to inschema as tuple,
        # Print user options for dtype etc
        # Consider if multiple while loops best method
        # Add ability to redo datatype if mistake
        # Possibly just confirm keyname with datatype and options before
        # moving to next key
=======

            while True:
                print("Please use valid options format: key=value, key2=value2...")
                print("For 'set', use  'list', as key and [item1,item2...] as value")
                opts_input = input(f'Enter {key} options or type "none" or "reselect": ').strip()

                if opts_input.lower() == 'none':
                    opts = {}
                    break
                elif opts_input.lower() == 'reselect':
                    break  # reselect dtype
                else:
                    opts = convert_opts(opts_input)
                    if opts is not None:
                        break

            if opts_input.lower() == 'reselect':
                continue

            usr_schema['fields'][key] = {'type': dtype, 'options': opts}
            break

>>>>>>> origin/dbgen_w_parameters:databasegen/dbgen.py
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
<<<<<<< HEAD:dbgen.py
        for key, dtype in schema.items():
            if dtype == 'id':
                doc[key] = i + 1
            else:
                doc[key] = valid_dtypes[dtype]()
=======
        temp_email = {}

        for dname, dtype_w_opts in schema["fields"].items():
            dtype, opts = dtype_w_opts['type'], dtype_w_opts['options']

            if dtype in ['f_name', 'l_name']:
                generated = valid_dtypes[dtype](i, opts)
                temp_email[dtype] = generated
                doc[dtype] = generated
            elif dtype == 'email':
                email_opts = {
                    "first": temp_email.get('f_name', faker.first_name()),
                    "last": temp_email.get('l_name', faker.last_name())
                }
                doc[dname] = valid_dtypes[dtype](i, email_opts)
            else:
                doc[dname] = valid_dtypes[dtype](i, opts)
>>>>>>> origin/dbgen_w_parameters:databasegen/dbgen.py
        gen_data.append(doc)

    return gen_data


def main():  # pragma: no cover
#    init()  # pragma: no cover

    # MainGeneration
    schema = usr_schema_build()  # pragma: no cover
    # TODO Save schema to json file
    num_docs = usr_num_docs()  # pragma: no cover
    generated_data = data_generate(schema, num_docs)  # pragma: no cover

<<<<<<< HEAD:dbgen.py
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
=======
    json_schema = json.dumps(schema, indent=2)  # pragma: no cover
    print(f'Schema:\n{json_schema}')  # pragma: no cover
    print('\nData:')  # pragma: no cover
    for doc in generated_data:  # pragma: no cover
        print(json.dumps(doc))  # pragma: no cover


if __name__ == "__main__":  # pragma: no cover
    main()  # pragma: no cover
>>>>>>> origin/dbgen_w_parameters:databasegen/dbgen.py
