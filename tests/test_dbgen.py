from databasegen import dbgen
import pytest
import json
from unittest.mock import patch

# TODO mock schema input



def test_convert_opts():
    opt_str = "min=10, max=100"
    expected = {'min': 10, 'max': 100}
    assert dbgen.convert_opts(opt_str) == expected

def test_convert_opts_w_string():
    opt_str = "start=-50y, end=-30y"
    expected = {'start': '-50y', 'end': '-30y'}
    assert dbgen.convert_opts(opt_str) == expected

def test_convert_opts_invalid():
    opt_str = "min==100, max"
    result = dbgen.convert_opts(opt_str)
    assert result is None

def is_ndjson(text):
    lines = text.strip().split('\n')
    for line in lines:
        try:
            json.loads(line)
        except json.JSONDecodeError:
            return False
    return True

def test_data_generate():
    test_schema = {
        "schema_name": "test",
        "fields": {
            "id": {"type": "id", "options": {}},
            "country": {"type": "country_code", "options": {}},
        }
    }
    test_n_docs = 4
    result = dbgen.data_generate(test_schema, test_n_docs)
    assert len(result) == test_n_docs
    # Check the content of each generated document
    for doc in result:
        assert "id" in doc
        assert isinstance(doc["id"], int)
        assert "country" in doc
        assert isinstance(doc["country"], str)
        assert len(doc["country"]) == 2



def test_data_generate_incorrect_n_docs():
    test_schema = {
        "schema_name": "test",
        "fields": {
            "id": {"type": "id", "options": {}},
            "country": {"type": "country_code", "options": {}},
        }
    }
    schema_id = "test_id"
    test_n_docs = -4
    result = dbgen.data_generate(test_schema, test_n_docs)
    assert len(result) == 0
    assert result == []

def test_valid_dtype_email_comp():
    opts = {'first': 'Kell', 'last': 'OReilly'}
    email = dbgen.valid_dtypes['email'](0, opts)
    assert email.startswith('kell.oreilly@')
    assert '@' in email

def test_valid_dtype_price_format():
    opts = {'currency': '£', 'min': 10, 'max': 20, 'dec': 1}
    price = dbgen.valid_dtypes['price'](0, opts)
    assert price.startswith('£')
    assert float(price[1:]) >= 10
    assert float(price[1:]) <= 20

def test_data_generate_email_depends_on_name():
    schema = {
        "schema_name": "test_schema",
        "fields": {
            "f_name": {"type": "f_name", "options": {}},
            "l_name": {"type": "l_name", "options": {}},
            "email": {"type": "email", "options": {}}
        }
    }
    data = dbgen.data_generate(schema, 1)[0]
    assert 'email' in data
    assert data['f_name'].lower() in data['email']
    assert data['l_name'].lower() in data['email']

def test_usr_num_docs():
    with patch('builtins.input', side_effect=['3']):
        result = dbgen.usr_num_docs()
        assert result == 3

def test_usr_num_docs():
    with patch('builtins.input', side_effect=['3']):
        result = dbgen.usr_num_docs()
        assert result == 3

# Testing user schema build
def test_usr_schema_build():
    with patch('builtins.input', side_effect=['testschema','y','date1','date','none','finished']):
        result = dbgen.usr_schema_build()
        expected ={"schema_name": "testschema","fields": {"date1": {"type": "date",
      "options": {}}}}
        assert result == expected