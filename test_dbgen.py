import dbgen
import pytest

#Unit Tests
#iso format ip, Full name matches first name and last name
# email matches name
#in correct format
def test_faker_generation():
    for key, dtype in dbgen.valid_dtypes:
        print(f'')

def test_data_generate():
    test_schema = {
    "email_address": "email",
    "local_ip": "ip",
    "destination_ip": "ip"
    }
    schema_id = "test_id"
    test_n_docs = 4
    result = dbgen.data_generate(test_schema, test_n_docs)
    assert len(result) == test_n_docs
    assert all(set(doc.keys()) == {"email_address", "local_ip", "destination_ip"} for doc in result)

def test_data_generate_incorrect_n_docs():
    test_schema = {
    "email_address": "email",
    "local_ip": "ip",
    "destination_ip": "ip"
    }
    schema_id = "test_id"
    test_n_docs = -4
    result = dbgen.data_generate(test_schema, test_n_docs)
    assert len(result) == 0
    assert result == []

'''
def test_data_generate_incorrect_schema_format():
    test_schema = {
    "email_address": "email",
    "local_ip": "ip",
    "destination_ip": "ip"
    }
    schema_id = "test_id"
    test_n_docs = -4
    result = dbgen.data_generate(test_schema, test_n_docs)
    assert len(result) == 0
    assert result == []
'''
'''
def test_usr_num_docs

def test_usr_schema_build_duplicate_key_id():
    test_schema = {
    "email_address": "email",
    "local_ip": "ip",
    "destination_ip": "ip"
    }
    schema_id = "test_id"
    test_n_docs = -4
    result = dbgen.data_generate(test_schema, test_n_docs)
    assert len(result) == 0
    assert result == []
'''
